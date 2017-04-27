from tkinter import Canvas
from tkinter import Button

import mmp_gui
import mmp_main


class Expanded_Album():


    def __init__(self,gui,album_canvas):

        self.gui = gui
        self.COVER_PADDING = 20        
        self.COVER_SIZE = self.gui.COVER_SIZE_X + 70
        self.COLOR = "#DADF22"
        self.INNER_COLOR = "#FAFF33"
        self.TEXT_PADDING_X = self.COVER_PADDING + gui.EXPANDED_COVER_SIZE
        self.INNER_CANVAS_OFFSET_Y = 55 
        self.ac = album_canvas       

        self.img = self.gui.get_cover(self.ac.album,self.COVER_SIZE,self.COVER_SIZE) 


    def draw(self):
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height = self.gui.EXPANDED_COVER_SIZE, bg = self.COLOR, highlightthickness = 0)
        me.create_image(self.COVER_PADDING,self.COVER_PADDING,image=self.img,anchor = "nw")
        me.create_text(self.TEXT_PADDING_X,self.COVER_PADDING,font=("Purisa",20),anchor="nw",text = self.ac.artist + " - " + self.ac.album.name)
	
        pad = self.gui.get_padding()
        y_pos = self.ac.y + self.gui.EXPANDED_COVER_SIZE / 2 - pad*2 - 10
        
        inner_can = Canvas(me,width=self.gui.WIDTH * 0.7 ,height = self.gui.EXPANDED_COVER_SIZE * 0.6 , bg = self.INNER_COLOR, highlightthickness=0)
        
        #button = Button(inner_can,width = 100, height = 100, bg = "#FFFFFF")
        #inner_can.create_window((50,50),width = 100, height = 100,window=button)

 
        inner_can.pack()
        me.create_window((self.TEXT_PADDING_X, self.INNER_CANVAS_OFFSET_Y),width=self.gui.WIDTH * 0.7,height=self.gui.EXPANDED_COVER_SIZE * 0.7,anchor ="nw",window=inner_can)	
        me.pack()

        self.me_id = self.gui.main_canvas.create_window((0,y_pos),width=self.gui.WIDTH-20,height = self.gui.EXPANDED_COVER_SIZE,anchor = "nw",window = me)


    def remove(self):
        self.gui.main_canvas.delete(self.me_id)
