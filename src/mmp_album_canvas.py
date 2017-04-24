from tkinter import Canvas

import mmp_main
import mmp_gui

class Album_Canvas():
    
    def __init__(self,gui,x,y,cover,artist,album):
       self.cover = cover
       self.gui = gui
       self.x = x
       self.y = y
       self.artist = artist.name
       self.album = album.name
       


    def draw(self):
       me = Canvas(self.gui.main_frame,width=self.gui.COVER_SIZE_X, height = self.gui.COVER_SIZE_Y,bg = self.gui.COLOR,highlightthickness = 0)
       me.create_image(0,0,image=self.cover,anchor="nw")
       me.create_text(0,self.gui.COVER_SIZE_X,font=("Purisa",10),anchor="nw",text=self.artist + " - " + self.album)
       me.pack()
       self.me_id = self.gui.main_canvas.create_window((self.x,self.y),width = self.gui.COVER_SIZE_X, height = self.gui.COVER_SIZE_Y,window = me)

    def remove(self):
        self.gui.main_canvas.delete(self.me_id)
