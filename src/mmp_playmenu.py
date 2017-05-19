from tkinter import *

import mmp_gui

class Playmenu():

    def __init__(self,gui):
        self.gui = gui
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height=self.gui.PLAYMENU_HEIGHT,bg = "red",highlightthickness=0)

        pause_can = Canvas(me,width = 100 ,height = 50,bg = "green", highlightthickness=0)
        pause_can.bind("<Button-1>",self.pause)
        pause_can.pack()
        me.create_window((0,0),width = 100, height = 50, anchor ="nw",window=pause_can)

        me.pack()
        self.me_id = self.gui.main_canvas.create_window((0,0),width=self.gui.WIDTH,height=self.gui.PLAYMENU_HEIGHT,anchor="nw",window=me)

    def pause(self,event):
        self.gui.pause()
