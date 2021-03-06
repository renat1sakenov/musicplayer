from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import io

import mmp_playmenu
import mmp_album_canvas
import mmp_main
import mmp_expanded_album

class Gui():

    def __init__(self,main):

        self.main = main
        self.window = Tk()

        self.album_list = []

        self.COVER_CLICKED_ID  = -1 
        self.HEIGHT = self.window.winfo_screenheight()
        self.WIDTH = self.window.winfo_screenwidth()
        self.COLOR = "#EEFFAA"
        self.COVER_SIZE_X = 220
        self.COVER_SIZE_Y = 250
        self.PADDING_PERCENT = 0.1
        self.ABSOLUTE_PADDING_X = 100
        self.ABSOLUTE_PADDING_Y = 125 

        self.ec = None
        self.last_row_clicked = False
 
        self.PLAYMENU_HEIGHT = 75


        #the minimal height of an expanded albun view
        self.EXPANDED_COVER_SIZE = self.COVER_SIZE_Y * 1.5

        self.window.geometry("%dx%d+0+0" % (self.WIDTH, self.HEIGHT))
        self.window.wm_title("MMP")
        self.window["bg"] = "white"

        self.menubar = Menu(self.window)
        self.menubar.add_command(label="Add Music", command=self.add_music)
        self.menubar.add_command(label="Options", command=self.options)
        self.menubar.add_command(label="Reload", command=self.reload)
        self.menubar["bg"] = "white"
        self.menubar["fg"] = "black"

        self.main_frame = Frame(self.window,height= self.HEIGHT, width= self.WIDTH,relief=SUNKEN)
        self.main_frame.pack()

        self.playmenu = mmp_playmenu.Playmenu(self)

        self.main_canvas = Canvas(self.main_frame,height = self.HEIGHT-self.PLAYMENU_HEIGHT,width = self.WIDTH,bg=self.COLOR) 

        self.scrollbar = Scrollbar(self.main_frame,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.main_canvas.yview)

        self.main_canvas.pack()
        self.main_canvas.config(yscrollcommand=self.scrollbar.set) 
        self.window.config(menu=self.menubar)

    def display(self,artists):
        self.ac_counter = 0
        self.album_list = [] 
        pad = self.get_padding()
        y_  = pad + self.ABSOLUTE_PADDING_Y
        x_  = pad + self.ABSOLUTE_PADDING_X
        for artist in artists.keys():
            for album in artists[artist]:
                pimg = self.get_cover(album,self.COVER_SIZE_X,self.COVER_SIZE_X)
                ac = mmp_album_canvas.Album_Canvas(self.ac_counter,self,x_,y_,pimg,artist,album)
                ac.draw()
                self.album_list.append(ac)
                self.ac_counter +=1
                if x_ + self.COVER_SIZE_X + pad  < self.WIDTH - self.COVER_SIZE_X:
                    x_ += self.COVER_SIZE_X + pad
                else:
                    x_ = pad + self.ABSOLUTE_PADDING_X
                    y_ += self.COVER_SIZE_Y + pad
        self.main_canvas.config(scrollregion=(0,0,0,y_ + self.COVER_SIZE_Y))
        self.adjust_scrolling()
        self.window.mainloop()

    def add_music(self):
        dirname = filedialog.askdirectory(parent=self.window,initialdir="/home/",title="Select your music")
        self.main.add_music(dirname)

    def options(self):
        pass

    def reload(self):
        self.main.reload()

    def get_padding(self):
        return self.COVER_SIZE_X * self.PADDING_PERCENT


    def get_cover(self,album,x,y):
        output = io.BytesIO(self.main.get_image(album))
        output.seek(0)
        img = Image.open(output)
        img.thumbnail((x,y),Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def adjust_scrolling(self):
        if self.ec != None and self.last_row_clicked: 
            self.main_canvas.config(scrollregion=(0,0,0,self.album_list[len(self.album_list)-1].y + self.COVER_SIZE_Y + self.ec.TOTAL_SIZE))
        else:
            self.main_canvas.config(scrollregion=(0,0,0,self.album_list[len(self.album_list)-1].y + self.COVER_SIZE_Y))
    
    ''' moves the cover objects that are below y_ in move_size. i should have the value -1 or 1 (for up and down) '''
    def move_covers(self,y_,i,move_size):
        for cover in self.album_list:
            if cover.y > y_:
                cover.move(i,move_size)

    def ac_clicked(self,id_):
        self.last_row_clicked = False
        if self.COVER_CLICKED_ID == -1:
            self.ec = mmp_expanded_album.Expanded_Album(self,self.album_list[id_])
            self.ec.draw()
            self.move_size = self.ec.TOTAL_SIZE 
            self.move_covers(self.album_list[id_].y,1,self.move_size)
            if self.album_list[id_].y == self.album_list[len(self.album_list)-1].y:
                self.last_row_clicked = True
            self.adjust_scrolling()
            self.COVER_CLICKED_ID = id_
        else:
            self.ec.remove()
            self.move_covers(self.album_list[self.COVER_CLICKED_ID].y,-1,self.move_size)
            self.adjust_scrolling()
            if self.COVER_CLICKED_ID != id_:
                self.COVER_CLICKED_ID = -1 
                self.ac_clicked(id_)
            else:
                self.COVER_CLICKED_ID = -1

    def play(self,track,album,artist):
        self.main.play(track,album,artist)
    
    def pause(self):
        self.main.pause()

    def next(self):
        self.main.next()

    def loop(self):
        self.main.loop()

    def slider(self,change):
        self.main.slider(change)

    def update_slider(self,change):
        self.playmenu.update_slider(change)

    def adjust_volume(self,change):
        self.main.adjust_volume(change)

    def shuffle(self):
        self.main.shuffle()
