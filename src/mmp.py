#!/usr/bin/env python2

import mmp_main
import mmp_artist

import os
import fnmatch
import eyed3

class MMP():

    def __init__(self):

        self.artists = []
        self.albums = []

        self.read_paths()
        self.load_music()

    def read_paths(self):
        f = open(mmp_main.PATH_FILE,"a+")
        for line in f:
            self.paths.append(line.strip())
        f.close()

        #test
        self.paths = ['/run/media/renat/My Passport/MUSIK/3LT/']

    def write_path(self):
        pass

    def delete_path(self):
        pass

    def load_music(self):
        #reading all music file in.
        self.music_files = []
        for line in self.paths:
            for root, dirs, files in os.walk(line):
                for files in fnmatch.filter(files, '*.mp3'):
                    self.music_files.append(os.path.join(root,files))
        #creating artists
        for file_p in self.music_files:
            mfile = eyed3.load(file_p)
            str_artist = mfile.tag.artist
            if not artist_already_there(str_artist):
                artist = mmp_artist.Artist(str_artist)
                self.artists.append(artist)

        #creating albums
        for file_p in self.music_files:
            mfile = eyed3.load(file_p)
            str_album = mfile.tag.album
            if not album_already_there(str_album):
                album = mmp_album.Album(str_album)
                #add to artist
            album.add_song(file_p)


    def artist_already_there(str_artist):
        for artist in self.artists:
            if artist.name == str_artist:
                return True
        return False

    def album_already_there(str_album):
        for album in self.albums:
            if album.name == str_album:
                return True
        return False
