import mmp_main
import mmp_album
import mmp_audio

import os
import fnmatch
import eyed3
from collections import defaultdict

class MMP():

    def __init__(self,main):

        self.paths = []
        self.main = main
        self.artists = defaultdict(list)
        self.audio = mmp_audio.Audio(self)
        eyed3.log.setLevel("ERROR")

        self.current_album = None
        self.current_song = None
        self.current_artist = None

        self.LOOP = False

        self.read_paths()
        self.load_music()


    def read_paths(self):
        f = open(mmp_main.PATH_FILE,"r")
        for line in f:
            self.paths.append(line.strip())
        f.close()

    def write_path(self):
        pass

    def delete_path(self):
        pass

    def reload(self):
        self.read_paths()
        self.load_music()

    '''
    reading music files from directories into artists -> albums -> songs
    '''
    def load_music(self):
        self.music_files = []
        for line in self.paths:
            for root, dirs, files in os.walk(line):
                for files in fnmatch.filter(files, '*.mp3'):
                    self.music_files.append(os.path.join(root,files))
        for file_p in self.music_files:
            mfile = eyed3.load(file_p)
            str_artist = mfile.tag.artist
            str_album = mfile.tag.album 
            str_track = file_p.split("/")[-1] if (mfile.tag.title == None) else  mfile.tag.title
            if self.get_album(self.artists[str_artist],str_album) == None:
                album = mmp_album.Album(str_album)
                self.artists[str_artist].append(album)
            self.get_album(self.artists[str_artist],str_album).songs.append((file_p,str_track))
        self.music_files = []   


    def get_album(self,album_list,str_album):
        for album in album_list:
            if album.name == str_album:
                return album
        return None

    def get_image(self,album):
        if len(album.songs) <=  0:
            print("Error: No songs")
            return
        mfile = eyed3.load(album.songs[0][0])
        if len(mfile.tag.images) > 0:
            return mfile.tag.images[0].image_data
        else: 
            return open("../cover/std.png","rb").read()

    def next_track(self):
        self.current_song = self.current_album.get_next(self.current_song)[0]
        if self.current_song != None:
            self.audio.play(self.current_song)
        else:
            if self.LOOP:
                self.current_song = self.current_album.songs[0][0]

    def play(self,track,album,artist):
        self.current_album = album
        self.current_song = track
        self.current_artist = artist
        self.audio.play(track)
