#!/usr/bin/env python

import mmp_gui
import mmp

PATH_FILE = "./mymusic"

def main():
    gui  = mmp_gui.Gui()
    mmp_o =  mmp.MMP()
    gui.display(mmp_o.artists)


def get_image(artist,album):
    mmp_o.get_image(artist,album)

if __name__ == "__main__":
    main()


