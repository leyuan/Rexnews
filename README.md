# Rexnews

The following steps required to be in the **correct root folder**

## CRON

$ cd /functions-cron/appengine

Download [gcloud SDK](https://cloud.google.com/sdk/)

Install libs

$ pip install -t lib -r requirements.txt

Deploy

$ gcloud app deploy app.yaml

$ gcloud app deploy cron.yaml

ref: [this google blog](https://firebase.googleblog.com/2017/03/how-to-schedule-cron-jobs-with-cloud.html)

## Cloud Functions

$ cd /functions-cron/appengine

$ npm install

$ firebase deploy --only functions