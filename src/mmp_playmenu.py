from tkinter import *

import mmp_gui

class Playmenu():

    def __init__(self,gui):
        self.gui = gui
        self.ENABLE_UPDATE = False
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height=self.gui.PLAYMENU_HEIGHT,bg = "red",highlightthickness=0)

        pause_can = Canvas(me,width = 100 ,height = 50,bg = "green", highlightthickness=0)
        pause_can.bind("<Button-1>",self.pause)
        pause_can.pack()
        pause_can.create_text(20,20,anchor="nw",text="PAUSE")	#for now
        me.create_window((0,0),width = 100, height = 50, anchor ="nw",window=pause_can)

        next_can = Canvas(me,width = 100, height = 50,bg = "yellow", highlightthickness=0)
        next_can.bind("<Button-1>",self.next)
        next_can.pack()
        next_can.create_text(20,20,anchor="nw",text="Next")  #for now
        me.create_window((110,0),width=100, height = 50, anchor="nw",window=next_can)

        
        loop_can = Canvas(me,width = 50, height = 25, bg = "blue", highlightthickness=0)
        loop_can.bind("<Button-1>",self.loop)
        loop_can.pack()
        loop_can.create_text(0,0,anchor="nw",text="loop") # for now
        me.create_window((220,0),width=50,height=25,anchor="nw",window=loop_can)

        self.slider = Scale(me,from_=0,to=100, orient=HORIZONTAL, command = self.slider_move,label="song")
        self.slider.bind("<Enter>", self.toggle_slider_update)
        self.slider.bind("<Leave>", self.toggle_slider_update)
        self.slider.pack()
        me.create_window((300,0),width=100,height = 70,anchor="nw",window=self.slider)

        self.volume = Scale(me,from_=0,to=100,orient=HORIZONTAL,command=self.adjust_volume,label="vol")
        self.volume.set(100)
        self.volume.pack()
        me.create_window((410,0),width=100,height=70,anchor="nw",window=self.volume)

        shuffle = Canvas(me,width=100,height = 50, bg = "magenta", highlightthickness=0)
        shuffle.bind("<Button-1>",self.shuffle)
        shuffle.pack()
        shuffle.create_text(20,20,anchor="nw",text="shuffle") #for now
        me.create_window((520,0),width=100,height=50,anchor="nw",window=shuffle)
 
        me.pack()
        #self.me_id = self.gui.main_canvas.create_window((0,0),width=self.gui.WIDTH,height=self.gui.PLAYMENU_HEIGHT,anchor="nw",window=me)

    def pause(self,event):
        self.gui.pause()

    def next(self,event):
        self.gui.next()

    def loop(self,event):
        self.gui.loop()

    def slider_move(self,event):
        if self.ENABLE_UPDATE: 
            self.gui.slider(self.slider.get())

    def update_slider(self,change):
        self.slider.set(change*100)

    def toggle_slider_update(self,event):
        self.ENABLE_UPDATE = not self.ENABLE_UPDATE

    def adjust_volume(self,event):
        self.gui.adjust_volume(self.volume.get())


    def shuffle(self,event):
        self.gui.shuffle()
