// call the packages we need
var express    = require('express');
var app        = express();
var bodyParser = require('body-parser');
var PythonShell = require('python-shell');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 3000;        // set our port

var options = {};

if(port !== 3000) {
    options = {
        pythonPath: "D:\\home\\Python27\\python.exe",
    };
}

// ROUTES FOR OUR API
var router = express.Router();

app.use('/api', router);
router.get('/', function(req, res) {

    crawlPage('spider/coin.py');
    crawlPage('spider/news.py');
    crawlPage('spider/lives.py');
    // PythonShell.run('spider/lives.py', options, function (err) {
    //     if (err) res.json(JSON.stringify(err));
    //     console.log('finished');
    //     res.json({ message: 'hooray! Finished running for Lives page' });
    // });
});

app.use(express.static('public'));

app.listen(port);
console.log('Magic happens on port ' + port);

function crawlPage(path) {
    PythonShell.run(path, options, function (err) {
        if (err) res.json(JSON.stringify(err));
        console.log('Finished');
        res.json({ message: 'hooray! Finished crawling for' + path });
    });
}
