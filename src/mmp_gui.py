#!/usr/bin/env python2

#import tkinter
from tkinter import * 
import mmp_main

class Gui():

    def __init__(self):
        self.window = Tk() 
        self.window.geometry("%dx%d+0+0" % (self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.wm_title("MMP")
        self.window["bg"] = "white"

        self.menubar = Menu(self.window)
        self.menubar.add_command(label="Add Music", command=self.add_music)
        self.menubar.add_command(label="Options", command=self.options)
        self.menubar["bg"] = "white"
        self.menubar["fg"] = "black"

        self.window.config(menu=self.menubar)
        self.window.mainloop()



    def display(self,artists):
        print("displaying music")



    def add_music(self):
        pass

    def options(self):
        pass
