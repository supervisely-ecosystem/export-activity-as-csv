<div align="center" markdown>
<img src="https://i.imgur.com/zxgNNMs.png" width="1900px"/>


# Export activity as CSV

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/download-activity-csv)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/download-activity-csv&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/download-activity-csv&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/download-activity-csv&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

Download activity data from project, team, labeling job, workspace or team member as `.csv` file.

## How To Run 

**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/import-cityscapes) if it is not there.

**Step 2**: Open context menu of team, workspace, project, labeling job, or team member -> `Report` -> `Download activity`. 

<img src="https://i.imgur.com/vmxlakQ.png"/>

## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/ang6yiZ.png"/>



**Note:** You can also find your activity data in `Team Files`->`activity_data`->`<taskId>_<instanceId>_<sampleName>.csv`.

Where `instanceId` and `sampleName` can be `projectId`, `teamId`, `labeling_jobId` or `team_memberID`.

<img src="https://i.imgur.com/8eW0SLM.png">
