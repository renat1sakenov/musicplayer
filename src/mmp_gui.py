from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import io

import mmp_album_canvas
import mmp_main

class Gui():

    def __init__(self,main):

        self.main = main
        self.window = Tk()

        self.album_list = []

        self.HEIGHT = self.window.winfo_screenheight()
        self.WIDTH = self.window.winfo_screenwidth()
        self.COLOR = "#EEFFAA"
        self.COVER_SIZE_X = 220
        self.COVER_SIZE_Y = 250
        self.PADDING_PERCENT = 0.1
        self.ABSOLUTE_PADDING_X = 100
        self.ABSOLUTE_PADDING_Y = 125


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

        self.main_canvas = Canvas(self.main_frame,height = self.HEIGHT,width = self.WIDTH,bg=self.COLOR) 

        self.scrollbar = Scrollbar(self.main_frame,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.main_canvas.yview)

        self.main_canvas.pack()

        self.main_canvas.config(yscrollcommand=self.scrollbar.set)
        
        self.window.config(menu=self.menubar)


    def display(self,artists):
        pad = self.get_padding()
        y_  = pad + self.ABSOLUTE_PADDING_Y
        x_  = pad + self.ABSOLUTE_PADDING_X
        for artist in artists:
            for album in artist.albums:
                output = io.BytesIO(self.main.get_image(album))
                output.seek(0)
                img = Image.open(output)
                img.thumbnail((self.COVER_SIZE_X,self.COVER_SIZE_X),Image.ANTIALIAS)
                pimg = ImageTk.PhotoImage(img)

                ac = mmp_album_canvas.Album_Canvas(self,x_,y_,pimg,artist,album)
                ac.draw()
                self.album_list.append(ac)

                if x_ + self.COVER_SIZE_X + pad  < self.WIDTH - self.COVER_SIZE_X:
                    x_ += self.COVER_SIZE_X + pad
                else:
                    x_ = pad + self.ABSOLUTE_PADDING_X
                    y_ += self.COVER_SIZE_Y + pad
        self.main_canvas.config(scrollregion=(0,0,0,y_ + self.COVER_SIZE_Y))

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
