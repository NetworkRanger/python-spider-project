var webPage = require('webpage');
var page = webPage.create();

page.onLoadFinished = function (status) {
    console.log('Status: ' + status);
    // Do other things here...
};