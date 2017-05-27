import mmp

from vlc import MediaPlayer as player
from vlc import MediaListPlayer as mlistplayer
from vlc import MediaList as mlist

class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.LOOP = False 
        self.PLAYING_NOW = False
        self.ALBUM_SELECTED = False

    def play(self,track,album):
        self.ALBUM_SELECTED = True
        if not self.PLAYING_NOW:
            self.PLAYING_NOW = True
            self.calbum = album
            
            #set up new playlist, the album
            self.playlist = mlistplayer()
            self.playing = player()
            self.playlist.set_media_player(self.playing)
            
            b = False
            current_album = mlist()
            for song in album.songs:
                if  song[0] == track:
                    b = True
                if b: 
                    current_album.add_media(song[0])
            self.playlist.set_media_list(current_album)
            self.playlist.play()
        else:
            self.playing.stop()
            self.PLAYING_NOW = False
            self.play(track,album)


    def next(self):
        if self.ALBUM_SELECTED:
            self.PLAYING_NOW = False
            self.playing.stop()
            if self.playlist.next() == -1:
                if self.LOOP:
                    self.play(self.calbum.songs[0][0],self.calbum)
                else: 
                    self.ALBUM_SELECTED = False      
 
    def pause(self):
        self.playing.pause()

    def loop(self):
        self.LOOP = not self.LOOP
       
