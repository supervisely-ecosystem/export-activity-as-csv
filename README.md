<div align="center" markdown>
<img src="https://i.imgur.com/sfh2ILA.png" width="1900px"/>

# Download activity to CSV

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

Download activity data in project, team, labeling job or activity of team member and save it to `CSV` file.

## How To Run 

**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/import-cityscapes) if it is not there.

**Step 2**: Open context menu of project(team, labeling job, team member) -> `Report` -> `Download activity`. 

<img src="https://i.imgur.com/3ItAVU7.png"/>

## How to use

Resulting project will be placed to your current `Workspace` with the same name as the cityscapes archive. Images in datasets will have tags (`train`, `val`, or `test`) corresponding to the parent directories in which the datasets were located during import. If the `train` directories are in the input folders, but the `val` directories are not, then the images in `train` folder will be tagged with `train` and `val` tags in the ratio, exposed in the slider.

<img src="https://i.imgur.com/TMjl7Pt.png"/>

You can also access your project by clicking on it's name from `Tasks` page.

<img src="https://i.imgur.com/i0pfXRV.png">
