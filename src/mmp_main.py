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

    def add_music(self,dirname):
        try:
            f = open(PATH_FILE,"a")
            f.write(dirname+"\n")
            f.close()
        except:
            print("Error writing to ./mymusic ")

    def display(self):
        self.gui.display(self.mmp_o.artists)
    
    def reload(self):
        self.mmp_o.reload()
        self.gui.display(self.mmp_o.artists)

    def play(self,track,album,artist):
        self.mmp_o.play(track,album,artist)

    def pause(self):
        self.mmp_o.pause()

    def next(self):
        self.mmp_o.next()

    def loop(self):
        self.mmp_o.loop()

    def slider(self,change):
        self.mmp_o.slider(change)
   
    def update_slider(self,change):
        self.gui.update_slider(change) 

    def adjust_volume(self,change):
        self.mmp_o.adjust_volume(change)

if __name__ == "__main__":
    Main()


