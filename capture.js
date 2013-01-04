//Original capture.js by Tim Tomes(@LaNMaSter53)
var page = require('webpage').create(),
    url, filename, size;

url = phantom.args[0];
filename = phantom.args[1];
page.viewportSize = { width: 1024, height: 768 };
page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
page.open(url, function (status) {
        window.setTimeout(function () {
            page.render(filename);
            phantom.exit();
        }, 200);
});
