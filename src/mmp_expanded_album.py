from tkinter import Canvas

import mmp_gui
import mmp_main


class Expanded_Album():


    def __init__(self,gui,album_canvas):

        self.gui = gui
        self.COVER_PADDING = 20        
        self.COVER_SIZE = self.gui.COVER_SIZE_X + 70
        self.COLOR = "#33AABB" #test  
        self.ac = album_canvas       

        self.img = self.gui.get_cover(self.ac.album,self.COVER_SIZE,self.COVER_SIZE) 


    def draw(self):
        me = Canvas(self.gui.main_frame,width=self.gui.WIDTH,height = self.gui.EXPANDED_COVER_SIZE, bg = self.COLOR, highlightthickness = 0)
        me.create_image(self.COVER_PADDING,self.COVER_PADDING,image=self.img,anchor = "nw")
        me.pack()
	
        pad = self.gui.get_padding()
        x_pos = self.gui.WIDTH / 2 - 10
        y_pos = self.ac.y + self.gui.COVER_SIZE_Y + pad + 30
        self.me_id = self.gui.main_canvas.create_window((x_pos,y_pos),width=self.gui.WIDTH-20,height = self.gui.EXPANDED_COVER_SIZE,window = me)


    def remove(self):
        self.gui.main_canvas.delete(self.me_id)
