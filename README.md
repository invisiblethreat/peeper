peeper
======

peeper is designed to parse Nessus reports that detect webservers,
and take screen shots of the parsed report.

What you need
-------------

* [PhantomJS 1.9+][3]
* Fonts to render text with PhantomJS (an issue for servers/headless systems, not usually installed)
* Python

Who thought of this first?
--------------------------
That would be [Tim Tomes(@LaNMaSter53)][1]), I've just taken the idea
and made it very specific to Nessus reports. If you want to see his 
code, check it out [here][2].

  [1]: https://twitter.com/LaNMaSteR53       "Tim Tomes(@LaNMaSter53)"
  [2]: https://bitbucket.org/LaNMaSteR53/peepingtom "here" 
  [3]: http://phantomjs.org/ "PhantomJS"

How you use it
--------------
* Put peeper.py and capture.js in the bin/ directory in your PhantomJS
install, or make sure PhantomJS is in your path, your choice. (You'll
need to edit the subprocess command if you use the latter option.)
* Feed it a Nessus report file: ./peeper.py testing_report.nessus
* Visit the resulting directory 'testing_report', and look at the 
index.html for thumbnails, and click for full size images
