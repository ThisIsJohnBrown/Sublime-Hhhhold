#   ------------------------------------------------------------
#   Sublime Hhhhold.com Placeholder Image Plugin
#   Version 1.0
#   by John Brown (@thisisjohnbrown)
#
#   https://github.com/ThisIsJohnBrown/Sublime-hhhhold
#
#   ------------------------------------------------------------
import sublime, sublime_plugin, urllib2, json, os, random, re

SETTINGS = sublime.load_settings("Hhhhold.sublime-settings")
DEFAULT_SIZES = SETTINGS.get('hh_default_sizes')
if DEFAULT_SIZES == None:
    DEFAULT_SIZES = "400x300, 800x600, 220x100, 70x70"
SET_RANGES = "Small, Medium, Large, Extra Large, Random, Random range"
IMAGEPATH = SETTINGS.get('hh_imagepath')
if IMAGEPATH == None:
    IMAGEPATH = "images/"
SAVELOCAL = SETTINGS.get('hh_localimages')
if SAVELOCAL == None:
    SAVELOCAL = False
SIZE = SETTINGS.get('hh_size')
if SIZE == None:
    SIZE = "400x300"
FORMAT = SETTINGS.get('hh_format')
if FORMAT == None:
    FORMAT = "png"

def load_default_sizes():
    global DEFAULT_SIZES
    all_sizes = [sizes.strip() for sizes in DEFAULT_SIZES.split(',')]

    return all_sizes

def load_set_sizes():
    global SET_RANGES
    set_sizes = [sizes.strip() for sizes in SET_RANGES.split(',')]

    return set_sizes

def get_current_path():
    view = sublime.Window.active_view(sublime.active_window())
    current_file = view.file_name()
    index = current_file.rfind('/')
    current_dir = current_file[:index]
    return current_dir

def insert_image(imageinfo):
    global FORMAT, IMAGEPATH, SAVELOCAL
    rand = random.randrange(0, 100000)

    imageurl = 'http://hhhhold.com/{0}{1}{2}?{3}'.format(imageinfo['size'], imageinfo['layout'], FORMAT, rand)
    
    if SAVELOCAL:
        file_name = "hhhhold-{0}-{1}.{2}".format(imageinfo['size'][:-1], rand, FORMAT)
        path = get_current_path()
        imagefile = urllib2.urlopen(imageurl)
        localFile = open(path+"/"+IMAGEPATH+file_name, 'w+')
        localFile.write(imagefile.read())
        localFile.close()
        insert_image_tag(IMAGEPATH+file_name)
    else:
        insert_image_tag(imageurl)

def set_dimension_mode(imageinfo):
    all_modes = ['any', 'portait', 'landscape']

    def on_enter(num):
        if num == 1:
            imageinfo['layout'] = 't/'
        elif num == 2:
            imageinfo['layout'] = 'w/'
        insert_image(imageinfo)

    sublime.active_window().show_quick_panel(all_modes, on_enter)

def insert_random_size(imageinfo):
    global RANGE
    set_sizes = load_set_sizes()
    def on_enter(num):
        #insert_image(all_sizes[num])
        if num == 0:
            imageinfo['size'] = 's/'
        elif num == 1:
            imageinfo['size'] = 'm/'
        elif num == 2:
            imageinfo['size'] = 'l/'
        elif num == 3:
            imageinfo['size'] = 'xl/'
        elif num == 4:
            imageinfo['size'] = 'r/'
        set_dimension_mode(imageinfo)

    sublime.active_window().show_quick_panel(set_sizes, on_enter)

def insert_image_tag(selected_image):
    imagetag = '<img alt="" src="{0}" />'.format(selected_image)
    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    for region in view.sel():
        view.replace(edit, region, imagetag)
    view.end_edit(edit) 

def insert_cached_images():
    global IMAGEPATH, FORMAT
    current_dir = get_current_path()

    imagefiles = [os.path.join(root, name)
        for root, dirs, files in os.walk(current_dir+"/"+IMAGEPATH)
            for name in files
                if name.startswith("hhhhold") and name.endswith(FORMAT)]

    imagefiles = [w.replace(current_dir+"/", '') for w in imagefiles]

    def on_enter(selected_image):
        if selected_image != -1:
            insert_image_tag(imagefiles[selected_image])
    sublime.active_window().show_quick_panel(imagefiles, on_enter)

class InsertImageCommand(sublime_plugin.TextCommand):
    global SAVELOCAL, SIZE, FORMAT
    def run(self, edit):
        seloptions = []
        seloptions.append("Hhhhold insert default size ({0})".format(SIZE))
        seloptions.append("Hhhhold insert random size")
        seloptions.append("Hhhhold insert cached images")

        def on_enter(num):
            imageinfo = {
                'size': '',
                'layout': ''
            }

            if num == 0:
                imageinfo['size'] = '{0}/'.format(SIZE)
                insert_image(imageinfo)
            elif num == 1:
                insert_random_size(imageinfo)
            elif num == 2:
                insert_cached_images()

        sublime.active_window().show_quick_panel(seloptions, on_enter)
