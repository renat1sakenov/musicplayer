from tkinter import * 
import mmp_main

class Gui():

    def __init__(self):

        self.window = Tk()

        self.HEIGHT = self.window.winfo_screenheight()
        self.WIDTH = self.window.winfo_screenwidth()
        self.COLOR = "#EEFFAA"
        self.COVER_SIZE = 40


        self.window.geometry("%dx%d+0+0" % (self.WIDTH, self.HEIGHT))
        self.window.wm_title("MMP")
        self.window["bg"] = "white"

        self.menubar = Menu(self.window)
        self.menubar.add_command(label="Add Music", command=self.add_music)
        self.menubar.add_command(label="Options", command=self.options)
        self.menubar["bg"] = "white"
        self.menubar["fg"] = "black"

        self.main_frame = Frame(self.window,height= self.HEIGHT, width= self.WIDTH,bg=self.COLOR,relief=SUNKEN)
        self.main_frame.pack()	

        self.window.config(menu=self.menubar)
        self.window.mainloop()



    def display(self,artists):	
        for artist in artists:
            for album in artist.albums:
                cover = Canvas(self.main_frame,width = self.COVER_SIZE, height = self.COVER_SIZE)
                cover.create_image(0,0,mmp_main.get_image(artist,album))
                cover.pack()
        print("displaying music")


    def add_music(self):
        pass

    def options(self):
        pass
