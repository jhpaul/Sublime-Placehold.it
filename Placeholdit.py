import sublime, sublime_plugin, urllib2, json, os, re

SETTINGS = sublime.load_settings("Placeholdit.sublime-settings")
BGCOLOR = SETTINGS.get('ph_bgcolor')
if BGCOLOR == None:
    BGCOLOR = "0eafff"
TEXTCOLOR = SETTINGS.get('ph_textcolor')
if TEXTCOLOR == None:
    TEXTCOLOR = "ffffff"
SIZE = SETTINGS.get('ph_size')
if SIZE == None:
    SIZE = "600x400"
FORMAT = SETTINGS.get('ph_format')
if FORMAT == None:
    FORMAT = ".png"
TEXT = SETTINGS.get('ph_text')
if TEXT == None:
    TEXT = "600x400"

def insert_image(size):
    global BGCOLOR, TEXTCOLOR, FORMAT, TEXT
    if TEXT == "":
        imageurl = 'http://placehold.it/{0}/{1}/{2}{3}'.format(size, BGCOLOR, TEXTCOLOR, FORMAT)
    else:
        imageurl = 'http://placehold.it/{0}/{1}/{2}{3}&text={4}'.format(size, BGCOLOR, TEXTCOLOR, FORMAT, TEXT)
    imagetag = '<img alt="{0}" src="{1}" />'.format(TEXT, imageurl)
    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    for region in view.sel():
        view.replace(edit, region, imagetag)
    view.end_edit(edit) 

class InsertImageCommand(sublime_plugin.TextCommand):
    global SIZE
    def run(self, edit):
        insert_image(SIZE)

class InsertCustomImageCommand(sublime_plugin.TextCommand):
    global BGCOLOR, TEXTCOLOR, SIZE, FORMAT, TEXT
    def run(self, edit):
        sublime.active_window().show_input_panel("Set Size:", "600x400", self.on_done, None, None)
        pass

    def on_done(self, text):
        insert_image(text)
