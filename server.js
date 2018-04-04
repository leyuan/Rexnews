// call the packages we need
var express    = require('express');
var app        = express();
var bodyParser = require('body-parser');
var PythonShell = require('python-shell');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 3000;        // set our port

// ROUTES FOR OUR API
var router = express.Router();

app.use('/api', router);
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });
    PythonShell.run('spider/news.py', function (err) {
        if (err) throw err;
        console.log('finished');
    });
});

app.use(express.static('public'));

app.listen(port);
console.log('Magic happens on port ' + port);
