#!/usr/bin/python
# -*- coding: utf-8 -*- 

import gi
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk,Gdk,Gio
from gi.repository import WebKit

class Main():
    def __init__(self)
        self.WALLPAPER_KEY = "org.gnome.desktop.background"
        self.IMAGE_PATH = Gio.Settings.new(self.WALLPAPER_KEY).get_string("picture-uri")

        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.window.add(self.webview)

        stylesheet = open("dash.css",mode="w")
        stylesheet.write("body { background: url('%s')}" % self.IMAGE_PATH);
        stylesheet.close();

        self.webview.load_uri('file:///home/bigbn/dash.html')

        self.show()
        self.main()

    def show():
        self.win.set_type_hint(Gdk.WindowTypeHint.DESKTOP)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.fullscreen()
        self.win.show_all()

    def main():
        Gtk.main()


if __name__=='__main__':
    instance = Main()
