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
    progress = sly.Progress("Write csv rows to file", 0)

    def print_progress(received, total):
        progress.set(received, total)

    if PROJECT_ID:
        result_act = api.project.get_activity(int(PROJECT_ID), progress_cb=print_progress)
        if len(result_act) == 0:
            app_logger.warn("No activities for current Project has been found")
        file_remote = f"/activity_data/{TASK_ID}_{PROJECT_ID}_{RESULT_FILE_NAME}"
    elif LABEL_JOB_ID:
        result_act = api.labeling_job.get_activity(TEAM_ID, int(LABEL_JOB_ID), progress_cb=print_progress) #job_id
        if len(result_act) == 0:
            app_logger.warn("No activities for current Labeling Job has been found")
        file_remote = f"/activity_data/{TASK_ID}_{LABEL_JOB_ID}_{RESULT_FILE_NAME}"
    elif MEMBER_ID:
        result_act = api.user.get_member_activity(TEAM_ID, int(MEMBER_ID), progress_cb=print_progress)
        if len(result_act) == 0:
            app_logger.warn("No activities for current Member has been found")
        file_remote = f"/activity_data/{TASK_ID}_{MEMBER_ID}_{RESULT_FILE_NAME}"
    elif TEAM_ID:
        result_act = api.team.get_activity(TEAM_ID, progress_cb=print_progress)
        if len(result_act) == 0:
            app_logger.warn("No activities for current Team has been found")
        result_act = pd.DataFrame(result_act)
        file_remote = f"/activity_data/{TASK_ID}_{TEAM_ID}_{RESULT_FILE_NAME}"

    app_logger.info(f"Remote file path: '{file_remote}'")
    if api.file.exists(TEAM_ID, file_remote):
        raise FileExistsError(f"File '{file_remote}' already exists in Team Files. Make sure you want to replace it. "
                              "Please, remove it manually and run the app again.")

    file_local = os.path.join(my_app.data_dir, file_remote.lstrip("/"))
    app_logger.info(f"Local file path: '{file_local}'")
    sly.fs.ensure_base_path(file_local)
    result_act.to_csv(file_local, index=False, header=True)

    upload_progress = []
    def _print_progress(monitor, upload_progress):
        if len(upload_progress) == 0:
            upload_progress.append(sly.Progress(message=f"Upload '{RESULT_FILE_NAME}'",
                                                total_cnt=monitor.len,
                                                ext_logger=app_logger,
                                                is_size=True))
        upload_progress[0].set_current_value(monitor.bytes_read)

    file_info = api.file.upload(TEAM_ID, file_local, file_remote, progress_cb=lambda m: _print_progress(m, upload_progress))
    api.task._set_custom_output(task_id, file_info.id, sly.fs.get_file_name_with_ext(file_remote),
                                description="CSV with reference items")

    app_logger.info("Local file successfully uploaded to team files")
    my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": TEAM_ID
    })
    my_app.run(initial_events=[{"command": "download_activity_csv"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)
