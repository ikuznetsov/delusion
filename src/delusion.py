#!/usr/bin/python
# -*- coding: utf-8 -*- 

import gi
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk,Gdk,Gio
from gi.repository import WebKit
import dbus
from dbus.mainloop.glib import DBusGMainLoop

class Main():
    def __init__(self):
        self.WALLPAPER_KEY = "org.gnome.desktop.background"
        self.IMAGE_PATH = Gio.Settings.new(self.WALLPAPER_KEY).get_string("picture-uri")

        DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SessionBus()
        self.bus.add_signal_receiver(self.dbus_listener,None,None,None,None,)

        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.window.add(self.webview)

        self.refresh()
        self.webview.load_uri('file:///home/bigbn/dash.html')
        
        self.show()
        self.main()

    def dbus_listener(self,section=None,arg2=None,arg3=None,arg4=None,arg5=None):
        if "/org/gnome/desktop/background/" in section:        
            self.refresh()

    def refresh(self):
        self.IMAGE_PATH = Gio.Settings.new(self.WALLPAPER_KEY).get_string("picture-uri")
        stylesheet = open("/home/bigbn/dash.css",mode="w")
        stylesheet.write("body { background: url('%s')}" % self.IMAGE_PATH);
        stylesheet.close();
        self.webview.reload()

    def show(self):
        self.window.set_type_hint(Gdk.WindowTypeHint.DESKTOP)
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.fullscreen()
        self.window.show_all()

    def main(self):
        Gtk.main()


if __name__=='__main__':
    instance = Main()