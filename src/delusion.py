#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import gi
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk,Gdk,Gio,GObject
#from gi.repository import WebKit
from browser import Browser
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import threading

class Main():
    def __init__(self):
        self.WALLPAPER_KEY = "org.gnome.desktop.background"
        self.IMAGE_PATH = Gio.Settings.new(self.WALLPAPER_KEY).get_string("picture-uri")
        self.SERVER_PORT = 8112

        DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SessionBus()
        self.bus.add_signal_receiver(self.dbus_listener,None,None,None,None,)

        self.window = Gtk.Window()
        self.webview = Browser()
        
        self.window.add(self.webview)
        self.refresh()
        self.webview.load_uri('file://%s/res/desktop.html' % os.getcwd())

        self.load_plugins()
        
        self.show()
        self.main()

    def dbus_listener(self,section=None,arg2=None,arg3=None,arg4=None,arg5=None,arg6=None):
        if "/org/gnome/desktop/background/" in str(section):        
            self.refresh()

    def refresh(self):
        import SocketServer
        self.IMAGE_PATH = Gio.Settings.new(self.WALLPAPER_KEY).get_string("picture-uri")
        stylesheet = open("%s/res/background.css" % os.getcwd() ,mode="w")
        stylesheet.write("body { background: url('%s') no-repeat; background-size: 100%%;}" % self.IMAGE_PATH);
        stylesheet.close();
        self.webview.reload()

    def load_plugins(self):
        for filename in os.listdir("%s/plugins" % os.getcwd()):
            if filename == "__init__.py" or filename == "":
                break
            try:
                plugin = __import__("plugins."+filename[:-3])
            except:
                pass 
      
        pass

    def show(self):
        self.window.set_type_hint(Gdk.WindowTypeHint.DESKTOP)
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.fullscreen()
        self.window.show_all()

    def main(self):
        Gtk.main()


if __name__=='__main__':
    instance = Main()
