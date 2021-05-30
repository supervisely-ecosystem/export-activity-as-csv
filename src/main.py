import os
import supervisely_lib as sly
import pandas as pd


my_app = sly.AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = os.environ.get("modal.state.slyProjectId")
LABEL_JOB_ID = os.environ.get("modal.state.slyLabelJobId")
MEMBER_ID = os.environ.get("modal.state.slyMemberId")
TASK_ID = int(os.environ["TASK_ID"])
RESULT_FILE_NAME = 'activity.csv'
logger = sly.logger


@my_app.callback("download_activity_csv")
@sly.timeit
def download_activity_csv(api: sly.Api, task_id, context, state, app_logger):

    logger.warn('PROJECT_ID {}'.format(PROJECT_ID))
    logger.warn('LABEL_JOB_ID {}'.format(LABEL_JOB_ID))
    logger.warn('MEMBER_ID {}'.format(MEMBER_ID))
    logger.warn('TEAM_ID {}'.format(TEAM_ID))
    if PROJECT_ID:
        result_act = api.project.get_activity(int(PROJECT_ID))
        file_remote = "/activity_data/{}_{}_{}".format(TASK_ID, PROJECT_ID, RESULT_FILE_NAME)
    elif LABEL_JOB_ID:
        result_act = api.labeling_job.get_activity(int(LABEL_JOB_ID))
        file_remote = "/activity_data/{}_{}_{}".format(TASK_ID, LABEL_JOB_ID, RESULT_FILE_NAME)
    elif MEMBER_ID:
        result_act = api.user.get_member_activity(TEAM_ID, int(MEMBER_ID))
        file_remote = "/activity_data/{}_{}_{}".format(TASK_ID, MEMBER_ID, RESULT_FILE_NAME)
    elif TEAM_ID:
        result_act_list = api.team.get_activity(TEAM_ID)
        columns = result_act_list[0].keys()
        result_act = pd.DataFrame(result_act_list, columns=columns)

        file_remote = "/activity_data/{}_{}_{}".format(TASK_ID, TEAM_ID, RESULT_FILE_NAME)

    app_logger.info("Remote file path: {!r}".format(file_remote))
    if api.file.exists(TEAM_ID, file_remote):
        raise FileExistsError("File {!r} already exists in Team Files. Make sure you want to replace it. "
                              "Please, remove it manually and run the app again."
                              .format(file_remote))

    file_local = os.path.join(my_app.data_dir, file_remote.lstrip("/"))
    app_logger.info("Local file path: {!r}".format(file_local))
    sly.fs.ensure_base_path(file_local)
    result_act.to_csv(file_local, index=False, header=True)
    file_info = api.file.upload(TEAM_ID, file_local, file_remote)
    api.task._set_custom_output(task_id, file_info.id, sly.fs.get_file_name_with_ext(file_remote),
                                description="CSV with reference items")

    app_logger.info("Local file successfully uploaded to team files")

    my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": TEAM_ID,
        "WORKSPACE_ID": WORKSPACE_ID
    })
    my_app.run(initial_events=[{"command": "download_activity_csv"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)

