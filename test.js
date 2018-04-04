var PythonShell = require('python-shell');

var options = {
    pythonPath: "D:home\\Python27\\python.exe",
};

PythonShell.run('spider/hello.py', options, function (err) {
    if (err) res.json(JSON.stringify(err));
    console.log('finished');
    res.json({ message: 'hooray! Finished running for Lives page' });
});