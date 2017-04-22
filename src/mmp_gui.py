from tkinter import *
from PIL import Image, ImageTk
import io
import mmp_main

class Gui():

    def __init__(self,main):

        self.main = main
        self.window = Tk()

        self.images = []

        self.HEIGHT = self.window.winfo_screenheight()
        self.WIDTH = self.window.winfo_screenwidth()
        self.COLOR = "#EEFFAA"
        self.COVER_SIZE = 220
        self.PADDING_PERCENT = 0.1


        self.window.geometry("%dx%d+0+0" % (self.WIDTH, self.HEIGHT))
        self.window.wm_title("MMP")
        self.window["bg"] = "white"

        self.menubar = Menu(self.window)
        self.menubar.add_command(label="Add Music", command=self.add_music)
        self.menubar.add_command(label="Options", command=self.options)
        self.menubar["bg"] = "white"
        self.menubar["fg"] = "black"

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.main_canvas = Canvas(self.window,height = self.HEIGHT,width = self.WIDTH,bg=self.COLOR,yscrollcommand=self.scrollbar.set)
        self.main_canvas.pack()


        self.scrollbar.config(command=self.main_canvas.yview)
        
        #self.main_frame = Frame(self.main_canvas,height= self.HEIGHT, width= self.WIDTH,bg=self.COLOR,relief=SUNKEN)
        #self.main_frame.pack()


        self.window.config(menu=self.menubar)


    def display(self,artists):
        pad = self.get_padding()
        x_ = y_ = pad
        for artist in artists:
            for album in artist.albums:
                cover = Canvas(self.main_canvas,width = self.COVER_SIZE, height = self.COVER_SIZE)
                output = io.BytesIO(self.main.get_image(album))
                output.seek(0)
                img = Image.open(output)
                img.thumbnail((self.COVER_SIZE,self.COVER_SIZE),Image.ANTIALIAS)
                pimg = ImageTk.PhotoImage(img)
                self.images.append(pimg)
                cover.create_image(0,0,image=pimg,anchor="nw")
                cover.pack()
                cover.place(x = x_, y = y_)
            
                if x_ + self.COVER_SIZE + pad  < self.WIDTH - self.COVER_SIZE:
                    x_ += self.COVER_SIZE + pad
                else:
                    x_ = pad
                    y_ += self.COVER_SIZE + pad
        self.window.mainloop()

    def add_music(self):
        pass

    def options(self):
        pass

    def get_padding(self):
        return self.COVER_SIZE * self.PADDING_PERCENT
