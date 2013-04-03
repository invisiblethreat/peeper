var page = require('webpage').create(),
  url, filename, size;

url = phantom.args[0];
filename = phantom.args[1];
page.viewportSize = { width: 1024, height: 768 };
page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };

page.open(url, function (status) {
  if ( status !== 'success')
  {
    console.log('FAILED to load the address ' + url );
    phantom.exit();
  }
  window.setTimeout(function ()
  {
    page.render(filename);
    phantom.exit();
  }, 2000);
});
