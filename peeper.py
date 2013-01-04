#!/usr/bin/python
import sys
import os
import re
import subprocess
import xml.etree.ElementTree as ET

def guess_proto(output):
  """This attempts to guess the HTTP prefix output based on the 
  message that the service detection plugin returns. It's very simple,
  but works for the time being.
  """

  regex = re.compile("TLS|OpenSSL")
  secure = regex.search(output)
  if secure:
    return "https"
  else:
    return "http"

file = sys.argv[1]
urls = []

tree = ET.parse(file)
root = tree.getroot()

for host in root.getiterator("ReportHost"):
  name = host.get("name")

  for item in host.getiterator("ReportItem"):
    svc = item.attrib['svc_name']
    detect = item.attrib['pluginName']

    if (svc == "www") and (detect == "Service Detection"):
      port = item.attrib['port']
      output = item.find("plugin_output")
      proto = guess_proto(output.text)
      url = proto + "://" +  name + ":" + port
      match = False

      #Check for duplicate entries
      for existing in urls:
        if (url == existing):
          match = True

      #Add proto://host:port if it doesn't exist
      if not (match):
        urls.append(url)


# make a directory and stash the results there
dir = re.sub(".nessus", "", file)
if os.path.exists(dir):
  print "The directory exists, aborting"
  exit
else:
  os.makedirs(dir)

# call phantom js here. should do somehting fun with the output...
num_in_row = 0

index = open(dir + "/index.html", "w")
index.write("<html><table><tr>\n")

urls.sort()
for url in urls:
  name = re.sub("http(s)?://", "", url)
  name = re.sub(":", "-", name)
  capture = "./phantomjs --ignore-ssl-errors=yes ./capture.js %s %s/%s.png" % (url, dir, name)
  process = subprocess.Popen([capture], shell=True)
  index.write("\t<td><a href=\"%s.png\"><img width=328 height=246 src=\"%s.png\"><br>%s</a></td>\n" % (name, name, url))
  num_in_row += 1
  if (num_in_row % 3 == 0 ):
    index.write("</tr><tr>\n")

index.write("</tr></table></html>")
index.close()
