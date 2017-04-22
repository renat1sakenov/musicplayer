#!/usr/bin/env python

import mmp_gui
import mmp

PATH_FILE = "./mymusic"


class Main():

    def __init__(self):
        self.mmp_o =  mmp.MMP(self)
        self.gui  = mmp_gui.Gui(self)
        self.gui.display(self.mmp_o.artists)


    def get_image(self,album):
        return self.mmp_o.get_image(album)



if __name__ == "__main__":
    Main()


