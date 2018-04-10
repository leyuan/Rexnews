var functions = require('firebase-functions');
const http = require("http");

// exports.hourly_job =
//   functions.pubsub.topic('hourly-tick').onPublish((event) => {
//     console.log("This job is ran every hour!")
//   });


exports.crawl = functions.pubsub.topic('crawl').onPublish((event) => {

  const url = {
    host: 'rexnews.azurewebsites.net',
    path: '/api'
  };

  http.get(url, res => {
      console.log('Just visited url ' + url.host + url.path);
  });
});