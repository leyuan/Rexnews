var functions = require('firebase-functions');
const http = require("http");

// exports.hourly_job =
//   functions.pubsub.topic('hourly-tick').onPublish((event) => {
//     console.log("This job is ran every hour!")
//   });


exports.crawl = functions.pubsub.topic('crawl').onPublish((event) => {

  const url = {
    host: 'ualberta.ca',
    path: '/'
  };

  http.get(url, res => {
      console.log('Just visited url ' + url.host + url.path);
  });
});