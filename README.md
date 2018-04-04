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

## Cloud Functions

$ cd /functions-cron/appengine

$ npm install

$ firebase deploy --only functions

## Verify

[Cron Job Page](https://console.cloud.google.com/appengine/taskqueues/cron?project=rexnews-2018&tab=CRON)

[Firebase Console](https://console.firebase.google.com/u/0/project/rexnews-2018/overview)

$ firebase functions:log

## Reference

[this google blog](https://firebase.googleblog.com/2017/03/how-to-schedule-cron-jobs-with-cloud.html)