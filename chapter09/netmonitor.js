var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();

page.onResourceRequested = function (requests) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};

page.onResourceRequested = function (response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);