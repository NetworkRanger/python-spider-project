var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0';
page.open('http://movie.mtime.com/108737/', function(status){
    if (status !== 'success'){
        console.log('Unable to acces network');
    }else {
        var ua = page.evaluate(function(){
            return document.getElementById('ratingRegion').textContent;
        });
        console.log('ua');
    }
    phantom.exit();
});
