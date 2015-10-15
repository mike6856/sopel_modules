var fs = require('fs');
var page = require('webpage').create();
var url = phantom.args[0];

page.viewportSize = { width: 1920, height: 1080 };
page.open(url);

page.onLoadFinished = function()
{
    // Output Results Immediately
    // var html = page.evaluate(function () {
        // return document.getElementsByTagName('html')[0].innerHTML;
    // });
    // fs.write("result.html", html, 'w');
    // page.render('RenderBeforeTimeout.jpeg', {format: 'jpeg', quality: '100'});
    window.setTimeout(function () {
        var html = page.evaluate(function () {
            return document.getElementsByTagName('html')[0].innerHTML;
        });
        fs.write("/home/atxbawt/.sopel/eta/result.html", html, 'w');
       // page.render('AfterTimeout.jpeg', {format: 'jpeg', quality: '100'});
        phantom.exit();
    }, 100); // 1
};
