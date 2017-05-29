import mmp

from vlc import MediaPlayer as player
from vlc import MediaListPlayer as mlistplayer
from vlc import MediaList as mlist
from threading import Thread

import time

class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.LOOP = False 
        self.PLAYING_NOW = False
        self.ALBUM_SELECTED = False
        self.SLIDER_UPDATE = True

    def play(self,track,album):
        self.ALBUM_SELECTED = True
        if not self.PLAYING_NOW:
            self.SLIDER_UPDATE = True
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

            Thread(target=self.start_slider_updater).start()

        else:
            self.playing.stop()
            self.SLIDER_UPDATE = False
            self.PLAYING_NOW = False
            self.play(track,album)


    def next(self):
        if self.ALBUM_SELECTED:
            self.PLAYING_NOW = False
            self.SLIDER_UPDATE = False
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

    def slider(self,change):
        self.playing.set_position(float(change/100))


    def start_slider_updater(self):
        while self.SLIDER_UPDATE:
            time.sleep(1)
            self.control.update_slider(self.playing.get_position())

    def adjust_volume(self,change):
        if self.playing != None:
            self.playing.audio_set_volume(change)
       
