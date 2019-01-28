var webPage = require('webpage');
var page = webPage.create();
page.onInitialized = function(){
    page.evaluate(function(){
        document.addEventListener('DOMContentLoaded', function(){
            console.log('DOM content has loaded.');
        }, false);
    });
};

