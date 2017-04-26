import mmp_main
import mmp_artist
import mmp_album

import os
import fnmatch
import eyed3
from collections import defaultdict

class MMP():

    def __init__(self,main):

        self.paths = []
        self.main = main
        self.artists = defaultdict(list)
        eyed3.log.setLevel("ERROR")

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
            if self.get_album(self.artists[str_artist],str_album) == None:
                album = mmp_album.Album(str_album)
                self.artists[str_artist].append(album)
            self.get_album(self.artists[str_artist],str_album).songs.append(file_p)
        self.music_files = []   


    def get_album(self,album_list,str_album):
        for album in album_list:
            if album.name == str_album:
                return album
        return None

    def get_image(self,album):
        #test: getting the image from first song:
        if len(album.songs) <=  0:
            print("Error: No songs")
            return
        mfile = eyed3.load(album.songs[0])
        return mfile.tag.images[0].image_data
