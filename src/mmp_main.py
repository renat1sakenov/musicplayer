#!/usr/bin/env python

import mmp_gui
import mmp
import mmp_audio


PATH_FILE = "./mymusic"


class Main():

    def __init__(self): 
        self.audio_thread = mmp_audio.Audio(self)
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
    

    def next_track(self):
        pass

    def play(self,track):
        self.audio_thread.play(track)


if __name__ == "__main__":
    Main()


