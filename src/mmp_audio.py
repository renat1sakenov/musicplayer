import mmp

from vlc import MediaPlayer as player
from vlc import MediaListPlayer as mlistplayer
from vlc import MediaList as mlist

#
from vlc import Media as media
#
from threading import Thread
from random import randint

import time

class Audio():


    def __init__(self,control):
        self.control = control
        self.playing = None
        self.calbum = None
        self.track = None
        self.LOOP = False 
        self.PLAYING_NOW = False
        self.ALBUM_SELECTED = False
        self.SLIDER_UPDATE = True
        self.SHUFFLE = False

    def play(self,track,album):
        self.ALBUM_SELECTED = True
        if not self.PLAYING_NOW:
            self.SLIDER_UPDATE = True
            self.PLAYING_NOW = True
            self.calbum = album
            self.track = track            

            #set up new playlist, the album
            self.playlist = mlistplayer()
            self.playing = player()
            self.playlist.set_media_player(self.playing)
            
            if self.SHUFFLE:
                self.shuffle() 
            else:
                self.set_playlist()

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


    def shuffle(self):
       self.SHUFFLE = not self.SHUFFLE
       if self.ALBUM_SELECTED:
           if self.SHUFFLE:
           
               shuffle_album = mlist()
               shuffle_album.add_media(self.track)
               l = len(self.calbum.songs)
               ilist = [self.calbum.get_index(self.track)]
 
               while shuffle_album.count() != l:
                   i = randint(0,l-1)    
                   if i not in ilist:
                       ilist.append(i) 
                       shuffle_album.add_media(self.calbum.songs[i][0])
               self.playlist.set_media_list(shuffle_album)
           else:
               self.set_playlist()

    def set_playlist(self):
       b = False
       current_album = mlist()
       for song in self.calbum.songs:
           if  song[0] == self.track:
              b = True
           if b: 
               current_album.add_media(song[0])
       self.playlist.set_media_list(current_album)
       self.playlist.play()

       
