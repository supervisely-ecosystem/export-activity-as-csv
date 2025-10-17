<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48245050/182574734-33bff080-ba67-488a-bbcc-665d5dfadb9e.png"/>


# Export activity as CSV

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/export-activity-as-csv)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/export-activity-as-csv)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/export-activity-as-csv.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/export-activity-as-csv.png)](https://supervisely.com)

</div>

## Overview

Download activity data from project, team, labeling job or team member as `.csv` file.

## How To Run 

**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervisely.com/apps/export-activity-as-csv) if it is not there.

**Step 2**: Open context menu of team, project, labeling job, or team member -> `Report` -> `Export activity as csv`. 

**For Project**:

<img src="https://i.imgur.com/BFLUfuW.png" width="700px"/>

**For Team**:

<img src="https://i.imgur.com/x4yfwyY.png" width="900px"/>

**For Member**:

<img src="https://i.imgur.com/azrE2qK.png" width="900px"/>

**For Labeling Job**:

<img src="https://i.imgur.com/ozWPCXE.png" width="900px"/>

## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/eHeSzGw.png"/>

**Note:** You can also find your activity data in `Team Files`->`activity_data`->`<taskId>_<instanceId>_activity.csv`.

Where `instanceId` can be `projectId`, `teamId`, `labelingJobId` or `teamMemberId`.

<img src="https://i.imgur.com/5IJZhQ1.png">
