var webPage = require('webpage');
var page = webPage.create();
var postBody = 'user=username&password=password';

page.open('http://www.google.com/', 'POST', postBody, function(status) {
    console.log('Status: ' + status);
    // Do other things here...
});

var webPage = require('webpage');
var page = webPage.create();
var settings = {
    operation: 'POST',
    encoding: 'utf8',
    headers: {
        'Content-Type': 'application/json',
    },
    data: JSON.stringify({
        some: 'data',
        another: ['custom', 'data']
    })
};

page.open('http://your.custom.api', settings, function(status){
    console.log('Status: ' + status);
    // Do other things here...
});
