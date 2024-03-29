
# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.0
# Copyright: (c) 2007-2009 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...

from distutils.core import setup
from py2exe.build_exe import py2exe

import glob
import os
import zlib
import shutil

# Remove the build folder
shutil.rmtree("build", ignore_errors=True)

# Version
version = int(open("files/setup/setup-version.txt").readline()) + 1
open("files/setup/setup-version.txt", "w").write(str(version))



class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)


# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = [('files', ['files/settings.yaml.example']),
              ('files/cache', ['files/cache/counter.txt']),
              ('files/icons', ['files/icons/AddedIcon.ico',
                               'files/icons/sdbe.ico',
                               'files/icons/NormalIcon.ico',
                               'files/icons/ModifiedIcon.ico']),
              ('files/icons/milky', ['files/icons/milky/31.png',
                                    'files/icons/milky/14.png',
                                    'files/icons/milky/12.png',
                                    'files/icons/milky/30.png',
                                    'files/icons/milky/44.png',
                                    'files/icons/milky/21.png',
                                    'files/icons/milky/38.png',
                                    'files/icons/milky/13.png',
                                    'files/icons/milky/40.png',
                                    'files/icons/milky/27.png',
                                    'files/icons/milky/29.png',
                                    'files/icons/milky/16.png',
                                    'files/icons/milky/6.png',
                                    'files/icons/milky/42.png',
                                    'files/icons/milky/32.png',
                                    'files/icons/milky/10.png',
                                    'files/icons/milky/35.png',
                                    'files/icons/milky/41.png',
                                    'files/icons/milky/45.png',
                                    'files/icons/milky/26.png',
                                    'files/icons/milky/18.png',
                                    'files/icons/milky/5.png',
                                    'files/icons/milky/36.png',
                                    'files/icons/milky/2.png',
                                    'files/icons/milky/43.png',
                                    'files/icons/milky/37.png',
                                    'files/icons/milky/39.png',
                                    'files/icons/milky/20.png',
                                    'files/icons/milky/25.png',
                                    'files/icons/milky/15.png',
                                    'files/icons/milky/4.png',
                                    'files/icons/milky/11.png',
                                    'files/icons/milky/7.png',
                                    'files/icons/milky/33.png',
                                    'files/icons/milky/odbcmanager.PNG',
                                    'files/icons/milky/19.png',
                                    'files/icons/milky/9.png',
                                    'files/icons/milky/17.png',
                                    'files/icons/milky/23.png',
                                    'files/icons/milky/28.png',
                                    'files/icons/milky/8.png',
                                    'files/icons/milky/22.png',
                                    'files/icons/milky/24.png',
                                    'files/icons/milky/34.png',
                                    'files/icons/milky/3.png',
                                    'files/icons/milky/1.png',
                                    'files/icons/milky/62.png',
                                    'files/icons/milky/61.png',
                                    'files/icons/milky/113.png',
                                    'files/icons/milky/46.png',
                                    'files/icons/milky/108.png',
                                    'files/icons/milky/110.png',
                                    'files/icons/milky/109.png',
                                    'files/icons/milky/90.png',
                                    'files/icons/milky/79.png',
                                    'files/icons/milky/100.png',
                                    'files/icons/milky/97.png',
                                    'files/icons/milky/85.png',
                                    'files/icons/milky/94.png',
                                    'files/icons/milky/92.png',
                                    'files/icons/milky/65.png',
                                    'files/icons/milky/96.png',
                                    'files/icons/milky/98.png',
                                    'files/icons/milky/60.png',
                                    'files/icons/milky/99.png',
                                    'files/icons/milky/54.png',
                                    'files/icons/milky/103.png',
                                    'files/icons/milky/129.png',
                                    'files/icons/milky/104.png',
                                    'files/icons/milky/102.png',
                                    'files/icons/milky/93.png',
                                    'files/icons/milky/125.png',
                                    'files/icons/milky/116.png',
                                    'files/icons/milky/53.png',
                                    'files/icons/milky/55.png',
                                    'files/icons/milky/56.png',
                                    'files/icons/milky/106.png',
                                    'files/icons/milky/114.png',
                                    'files/icons/milky/80.png',
                                    'files/icons/milky/105.png',
                                    'files/icons/milky/95.png',
                                    'files/icons/milky/107.png',
                                    'files/icons/milky/91.png',
                                    'files/icons/milky/101.png',
                                    'files/icons/milky/126.png',
                                    'files/icons/milky/76.png',
                                    'files/icons/milky/49.png',
                                    'files/icons/milky/77.png',
                                    'files/icons/milky/122.png',
                                    'files/icons/milky/57.png',
                                    'files/icons/milky/123.png',
                                    'files/icons/milky/115.png',
                                    'files/icons/milky/48.png',
                                    'files/icons/milky/131.png',
                                    'files/icons/milky/121.png',
                                    'files/icons/milky/63.png',
                                    'files/icons/milky/89.png',
                                    'files/icons/milky/81.png',
                                    'files/icons/milky/86.png',
                                    'files/icons/milky/130.png',
                                    'files/icons/milky/120.png',
                                    'files/icons/milky/127.png',
                                    'files/icons/milky/84.png',
                                    'files/icons/milky/78.png',
                                    'files/icons/milky/71.png',
                                    'files/icons/milky/128.png',
                                    'files/icons/milky/52.png',
                                    'files/icons/milky/72.png',
                                    'files/icons/milky/68.png',
                                    'files/icons/milky/87.png',
                                    'files/icons/milky/82.png',
                                    'files/icons/milky/83.png',
                                    'files/icons/milky/51.png',
                                    'files/icons/milky/64.png',
                                    'files/icons/milky/67.png',
                                    'files/icons/milky/47.png',
                                    'files/icons/milky/50.png',
                                    'files/icons/milky/118.png',
                                    'files/icons/milky/111.png',
                                    'files/icons/milky/59.png',
                                    'files/icons/milky/88.png',
                                    'files/icons/milky/69.png',
                                    'files/icons/milky/66.png',
                                    'files/icons/milky/58.png',
                                    'files/icons/milky/124.png',
                                    'files/icons/milky/119.png',
                                    'files/icons/milky/73.png',
                                    'files/icons/milky/74.png',
                                    'files/icons/milky/70.png',
                                    'files/icons/milky/112.png',
                                    'files/icons/milky/75.png',
                                    'files/icons/milky/117.png',
                                    'files/icons/milky/db.png',
                                    'files/icons/milky/folder.png']),
              ('files/sql', ['files/sql/counter.txt']),
              ('files/templates', ['files/templates/default.yaml',
                                    'files/templates/user.yaml']),
              ('files/workspace', ['files/workspace/counter.txt']),
              ('files/testDB', ['files/testDB/db_news.sqlite']),
              ('files/recent', ['files/recent/counter.txt']),
              ('files/search', ['files/search/counter.txt']),
              ('files/setup', ['files/setup/setup-version.txt',
                                'files/setup/changelog.txt']),
              ('imageformats', ['files/dll/imageformats/qico4.dll']),
			  ('.', ['files/dll/qscintilla2.dll'])]



includes = ['sip', 'decimal', 'datetime', 'yaml']
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
icon_resources = [(1, 'files/icons/sdbe.ico')]
bitmap_resources = []
other_resources = []


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added


# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D

GUI2Exe_Target_1 = Target(
    # what to build
    script = "sdbe.pyw",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "sdbe",
    version = "0.%s" % version,
    company_name = "No Company",
    copyright = "No Copyrights",
    name = "Py2Exe Sample File",

    )

# No custom class for UPX compression or Inno Setup script

# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(

    # No UPX or Inno Setup

    data_files = data_files,

    options = {"py2exe": {"compressed": 0,
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "files/exe/sdbe-build-%s" % version,
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',

                         }
              },

    zipfile = None,
    console = [],
    windows = [GUI2Exe_Target_1],
    service = [],
    com_server = [],
    ctypes_com_server = []
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added

os.popen('"c:/Program Files/WinRAR/Rar.exe" a files/exe/sdbe-build-%s.rar files/exe/sdbe-build-%s' % (version, version))

# And we are done. That's a setup script :-D