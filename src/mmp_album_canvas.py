from tkinter import Canvas

import mmp_main
import mmp_gui

class Album_Canvas():
    
    def __init__(self,id_,gui,x,y,cover,artist,album):
       self.id = id_
       self.cover = cover
       self.gui = gui
       self.x = x
       self.y = y
       self.artist = artist
       self.album = album
       


    def draw(self):
       me = Canvas(self.gui.main_frame,width=self.gui.COVER_SIZE_X, height = self.gui.COVER_SIZE_Y,bg = self.gui.COLOR,highlightthickness = 0)
       me.create_image(0,0,image=self.cover,anchor="nw")
       me.create_text(0,self.gui.COVER_SIZE_X,font=("Purisa",10),anchor="nw",text=self.artist + " - " + self.album.name)

       me.bind("<Button-1>",lambda event, arg=self.id: self.click(event,arg))

       me.pack()
       self.me_id = self.gui.main_canvas.create_window((self.x,self.y),width = self.gui.COVER_SIZE_X, height = self.gui.COVER_SIZE_Y,window = me)

    def remove(self):
        self.gui.main_canvas.delete(self.me_id)

    def click(self,event,arg):
        self.gui.ac_clicked(arg)

    def move(self,i):
        self.gui.main_canvas.move(self.me_id,0,i * self.gui.EXPANDED_COVER_SIZE)
        self.y += i*self.gui.EXPANDED_COVER_SIZE
