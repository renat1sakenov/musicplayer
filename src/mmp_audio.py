import subprocess
from threading import Thread

import mmp


class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.thread_check = None

    def play(self,track):
        self.TRACK_FINISHED = True
        if self.playing == None:
            self.playing = subprocess.Popen(['mpg123','-q',track])
            self.thread_check = Thread(target=self.run)
            self.thread_check.start()
        else: 
            self.TRACK_FINISHED = False
            self.playing.terminate()
            self.playing = None
            self.play(track)


    def run(self):
        while self.playing.poll() == None:
            pass
        if self.TRACK_FINISHED:
            print("track finished")
            self.next_track()

    def next_track(self):
        self.playing = None
        self.control.next_track()
