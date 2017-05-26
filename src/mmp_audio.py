import mmp

from vlc import MediaPlayer as player

class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.PLAYING_NOW = False

    def play(self,track):
        if not self.PLAYING_NOW:
            self.PLAYING_NOW = True
            self.playing = player(track)
            self.playing.play()
        else:
            self.playing.stop()
            self.PLAYING_NOW = False
            self.play(track)

    def pause(self):
        self.playing.pause()
       
