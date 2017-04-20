#!/usr/bin/env python

import mmp_gui
import mmp

PATH_FILE = "./mymusic"

def main():
    gui  = mmp_gui.Gui()
    mmp_o =  mmp.MMP()
    gui.display(mmp_o.artists)


if __name__ == "__main__":
    main()


