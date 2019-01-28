var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();

page.onConsoleMesage = function (msg) {
    console.log('Page title is ' + msg);
};
page.open(url, function (status) {
    page.evaluate(function () {
        console.log(document.title);
    });
    phantom.exit();
});