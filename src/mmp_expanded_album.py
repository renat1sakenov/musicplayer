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

        self.TRACK_HEIGHT = 30    
        self.TRACK_WIDTH = .5 
        
        self.TRACK_LIST_MAX_LEN = 10
        self.DUAL_LIST = False

        self.img = self.gui.get_cover(self.ac.album,self.COVER_SIZE,self.COVER_SIZE) 


    def draw(self):
        
        self.TOTAL_SIZE = self.gui.EXPANDED_COVER_SIZE 
        #there will be two columns for the tracks 
        if len(self.ac.album.songs) > self.TRACK_LIST_MAX_LEN:
            self.DUAL_LIST = True

        #if the album contains more than "10" tracks, the expanded view must be drawn larger than the minimal expanded view.
        if len(self.ac.album.songs) > 2*self.TRACK_LIST_MAX_LEN: 
            self.TOTAL_SIZE += ((len(self.ac.album.songs)- 2*self.TRACK_LIST_MAX_LEN)/2) *self.TRACK_HEIGHT 
                
        #the main canvas for the expande view 
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height = self.TOTAL_SIZE, bg = self.COLOR, highlightthickness = 0)
        me.create_image(self.COVER_PADDING,self.COVER_PADDING,image=self.img,anchor = "nw")
        me.create_text(self.TEXT_PADDING_X,self.COVER_PADDING,font=("Purisa",20),anchor="nw",text = self.ac.artist + " - " + self.ac.album.name)
	
        pad = self.gui.get_padding()
        y_pos = self.ac.y + self.gui.EXPANDED_COVER_SIZE / 2 - pad*2 - 10
        
        
        #the canvas in which the tracks are shown.
        inner_can = Canvas(me,width=self.gui.WIDTH * 0.7 ,height = self.TOTAL_SIZE - 70 , bg = self.INNER_COLOR, highlightthickness=0)
        
        xt=yt = 0
        for track in self.ac.album.songs:
            track_can = Canvas(inner_can,width = self.TRACK_WIDTH*self.gui.WIDTH*0.7, height = self.TRACK_HEIGHT,bg = self.INNER_COLOR,highlightthickness=0)
            track_can.create_text(0,0,font=("Purisa",15),anchor="nw",text=track[1])
            track_can.pack()
            track_can.bind("<Button-1>",lambda event, arg=track[0]: self.play(event,arg))
            inner_can.create_window((xt,yt),width=self.TRACK_WIDTH*self.gui.WIDTH*0.7,height=self.TRACK_HEIGHT,anchor="nw",window=track_can)        
            if self.DUAL_LIST:
                if xt == 0:
                    xt = self.TRACK_WIDTH*self.gui.WIDTH*0.7
                else: 
                   xt = 0
                   yt += self.TRACK_HEIGHT
            else:
                yt += self.TRACK_HEIGHT
        inner_can.pack()
        me.create_window((self.TEXT_PADDING_X, self.INNER_CANVAS_OFFSET_Y),width=self.gui.WIDTH * 0.7,height=self.TOTAL_SIZE - 70,anchor ="nw",window=inner_can)	
        me.pack()

        self.me_id = self.gui.main_canvas.create_window((0,y_pos),width=self.gui.WIDTH-20,height = self.TOTAL_SIZE,anchor = "nw",window = me)
    
    def play(self,event,track):
        self.gui.play(track,self.ac.album,self.ac.artist)

    def remove(self):
        self.gui.main_canvas.delete(self.me_id)
