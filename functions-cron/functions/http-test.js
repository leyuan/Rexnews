const http = require("http");
var port = process.env.PORT || 3000;

console.log(port);

const url = {
    host: 'rexnews.azurewebsites.net',
    path: '/api'
};

http.get(url, res => {
    console.log('Just visited url ' + url.host + url.path);
});