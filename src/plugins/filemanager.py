# -*- coding: utf-8 -*-
import os
path="/home/bigbn"  # insert the path to the directory of interest
dirList=os.listdir(path)
for fname in dirList:
    if not fname.startswith("."):
        print "<a href='xdg:/home/bigbn/%s'>%s</a>" % (fname,fname)

