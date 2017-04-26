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
        self.ac = album_canvas       

        self.img = self.gui.get_cover(self.ac.album,self.COVER_SIZE,self.COVER_SIZE) 


    def draw(self):
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height = self.gui.EXPANDED_COVER_SIZE, bg = self.COLOR, highlightthickness = 0)
        me.create_image(self.COVER_PADDING,self.COVER_PADDING,image=self.img,anchor = "nw")
        me.create_text(self.TEXT_PADDING_X,self.COVER_PADDING,font=("Purisa",20),anchor="nw",text = self.ac.artist + " - " + self.ac.album.name)
	
        pad = self.gui.get_padding()
        x_pos = self.gui.WIDTH / 2 - 10
        y_pos = self.ac.y + self.gui.COVER_SIZE_Y + pad + 30
        
        inner_can = Canvas(me,width=self.gui.WIDTH * 0.7 ,height = self.gui.EXPANDED_COVER_SIZE * 0.6 , bg = self.INNER_COLOR, highlightthickness=0)
        
        #button = Button(inner_can,width = 100, height = 100, bg = "#FFFFFF")
        #inner_can.create_window((50,50),width = 100, height = 100,window=button)

 
        inner_can.pack()
        me.create_window(( x_pos + 140, 200),width=self.gui.WIDTH * 0.75,height=self.gui.EXPANDED_COVER_SIZE * 0.7,window=inner_can)	
        me.pack()

        
	
        self.me_id = self.gui.main_canvas.create_window((x_pos,y_pos),width=self.gui.WIDTH-20,height = self.gui.EXPANDED_COVER_SIZE,window = me)


    def remove(self):
        self.gui.main_canvas.delete(self.me_id)
