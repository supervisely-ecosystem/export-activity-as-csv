import os

import pandas as pd
import supervisely as sly
from dotenv import load_dotenv

import workflow as w

if sly.is_development():
    load_dotenv("debug.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TMP_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "tmp")
sly.fs.mkdir(TMP_DIRECTORY)
sly.logger.info("Temporary directory created at %s", TMP_DIRECTORY)
RESULT_FILE_NAME = "activity.csv"

# region envvars
team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id(raise_not_found=False)
job_id = os.environ.get("modal.state.slyJobId")
member_id = os.environ.get("modal.state.slyMemberId")

task_id = sly.env.task_id(raise_not_found=False)
if not task_id and sly.is_development():
    # For convenience in local development, setting TASK_ID to a random value.
    sly.logger.debug("Local development mode, setting TASK_ID to random value.")
    from random import randint

    task_id = randint(0, 1000)

# endregion

sly.logger.info(
    "Input parameters, team_id: %s, workspace_id: %s, project_id: %s, job_id: %s, member_id: %s",
    team_id,
    workspace_id,
    project_id,
    job_id,
    member_id,
)
api = sly.Api.from_env()
sly.logger.info("API initialized for server: %s", api.server_address)


@sly.timeit
def download_activity_csv():
    progress = sly.Progress("Write csv rows to file", 0)

    def print_progress(received, total):
        progress.set(received, total)

    if project_id is not None:
        result_act = api.project.get_activity(project_id, progress_cb=print_progress)
        w.workflow_input(api, project_id)
        if len(result_act) == 0:
            sly.logger.warn("No activities for current Project has been found")
        file_remote = os.path.join(
            sly.team_files.RECOMMENDED_EXPORT_PATH,
            f"activity_data/{task_id}_{project_id}_{RESULT_FILE_NAME}",
        )

    elif job_id is not None:
        result_act = api.labeling_job.get_activity(team_id, job_id, progress_cb=print_progress)
        # TODO add workflow input for labeling job
        if len(result_act) == 0:
            sly.logger.warn("No activities for current Labeling Job has been found")
        file_remote = os.path.join(
            sly.team_files.RECOMMENDED_EXPORT_PATH,
            f"activity_data/{task_id}_{job_id}_{RESULT_FILE_NAME}",
        )
    elif member_id is not None:
        result_act = api.user.get_member_activity(team_id, member_id, progress_cb=print_progress)
        if len(result_act) == 0:
            sly.logger.warn("No activities for current Member has been found")
        file_remote = os.path.join(
            sly.team_files.RECOMMENDED_EXPORT_PATH,
            f"activity_data/{task_id}_{member_id}_{RESULT_FILE_NAME}",
        )
    elif team_id is not None:
        result_act = api.team.get_activity(team_id, progress_cb=print_progress)
        if len(result_act) == 0:
            sly.logger.warn("No activities for current Team has been found")
        result_act = pd.DataFrame(result_act)
        file_remote = os.path.join(
            sly.team_files.RECOMMENDED_EXPORT_PATH,
            f"activity_data/{task_id}_{team_id}_{RESULT_FILE_NAME}",
        )

    sly.logger.info(f"Remote file path: '{file_remote}'")
    if api.file.exists(team_id, file_remote):
        raise FileExistsError(
            f"File '{file_remote}' already exists in Team Files. Make sure you want to replace it. "
            "Please, remove it manually and run the app again."
        )

    file_local = os.path.join(TMP_DIRECTORY, file_remote.lstrip("/"))
    sly.logger.info("Local file path: %s", file_local)

    sly.fs.ensure_base_path(file_local)
    result_act.to_csv(file_local, index=False, header=True)

    # In development mode, the file is not uploaded to the team files.
    # The local path will be printed to the console.
    file_info = sly.output.set_download(file_local)

    if not file_info:
        sly.logger.warning("File was not uploaded to team files, workflow output will not be set")
        return

    w.workflow_output(api, file_info)
    sly.logger.info("Local file successfully uploaded to team files at %s", file_remote)


if __name__ == "__main__":
    download_activity_csv()
