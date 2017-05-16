import subprocess
from threading import Thread

import mmp


class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.thread_play = None
        self.PLAYING_B = False

    def play(self,track):
        if not self.PLAYING_B:
            self.PLAYING_B = True
            self.thread_play = Thread(target=self.run,args = (track,))
            self.thread_play.start()
        else: 
            self.PLAYING_B = False
            self.playing.terminate()
            self.play(track)

    def run(self,track):
        print("playing " + str(self.playing))
        self.playing = subprocess.Popen(['mpg123','-q',track]).wait()
        print("2 " + str(self.playing))
        if self.PLAYING_B:
            self.control.next_track()
