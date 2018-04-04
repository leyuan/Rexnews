var PythonShell = require('python-shell');

options = {
    pythonPath: "D:\\home\\Python27\\python.exe",
};

PythonShell.run('spider/hello.py', options, function (err) {
    if (err) console.log(err);

    console.log("Done");
});