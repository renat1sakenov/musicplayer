import subprocess
import os
import time
from threading import Thread


import mmp


class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.PLAYING_NOW = False

    def play(self,track):
        if not self.PLAYING_NOW:
            print("MMP: New track " + str(track))
            self.PLAYING_NOW = True
            self.playing = subprocess.Popen("mpg123 '" + track+"'\n",shell=True,stdin=subprocess.PIPE)
            #some kind of polling / interrupt when the track ends, :
            '''
            if self.PLAYING_NOW:
                self.control.next_track()
            '''
        else: 
            print("MMP: Interrupting current track")
            self.PLAYING_NOW = False
            os.system("killall mpg123") #todo..
            time.sleep(0.1)		#change so that current process really died
            self.play(track)

    def pause(self):
        print("trying now!")
        #self.playing.communicate(b's')[0]
        self.playing.stdin.write(b's')[0]
