import mmp_main
import mmp_artist
import mmp_album

import os
import fnmatch
import eyed3

class MMP():

    def __init__(self,main):

        self.paths = []
        self.main = main
        self.artists = []
        eyed3.log.setLevel("ERROR")

        self.read_paths()
        self.load_music()

        ''' 
        TEST
        for a in self.artists:
            print(a.name)
            for b in a.albums:
                print(b.name)
                for s in b.songs:
                    print(s)
        '''
        self.music_files = [] #no need for them

    def read_paths(self):
        f = open(mmp_main.PATH_FILE,"r")
        for line in f:
            self.paths.append(line.strip())
        f.close()

        '''test
        self.paths = ['/run/media/renat/My Passport/MUSIK/Animal Collective/','/run/media/renat/My Passport/MUSIK/The Beatles/','/run/media/renat/My Passport/MUSIK/John Frusciante','/run/media/renat/My Passport/MUSIK/Linkin Park','/run/media/renat/My Passport/MUSIK/Red Hot Chili Peppers','/run/media/renat/My Passport/MUSIK/The Beach Boys']
        '''
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
            if self.get_artist(str_artist) == None:
                artist = mmp_artist.Artist(str_artist)
                self.artists.append(artist)

        #creating albums
        for file_p in self.music_files:
            mfile = eyed3.load(file_p)
            str_artist = mfile.tag.artist
            str_album = mfile.tag.album
            if self.get_album(str_artist,str_album) == None:
                album = mmp_album.Album(str_album)
                self.get_artist(mfile.tag.artist).albums.append(album)
            else:
                album = self.get_album(str_artist,str_album)
            album.songs.append(file_p)

    def get_artist(self,str_artist):
        for artist in self.artists:
            if artist.name == str_artist:
                return artist
        return None

    def get_album(self,str_artist,str_album):
        for album in self.get_artist(str_artist).albums:
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
