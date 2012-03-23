# -*- coding: utf-8 -*-
import os
import simplejson as json
import base64
path="/home/bigbn/"  # insert the path to the directory of interest
dirList=os.listdir(path)

files = []

for fname in dirList:
    if not fname.startswith("."):
        files.append([fname,base64.b64encode(path+fname)])

response=json.dumps(files)

resources = open("res/filemanager.json","w")
resources.write(response)
resources.close()

js_plugin = """$(document).ready(function() {
                 $.getJSON('filemanager.json', function(json) {
                  var items = []
                  $.each(json, function(key, val) {
                   items.push('<a href="xdg:' + val[1] + '">'+ val[0]+'</a>');
                  });
                  $('<div>', {'class': 'filemanager',
                   html: items.join('')
                  }).appendTo('body');
                 });
                }); """

resources = open("res/filemanager.js","w")
resources.write(js_plugin)
resources.close()

plugin_style = """.filemanager {width: 300px;}
                  .filemanager a {padding: 5px; background: rgba(255,255,255, 0.2); color: black; display: block; margin: 1px;}"""

resources = open("res/filemanager.css","w")
resources.write(plugin_style)
resources.close()


