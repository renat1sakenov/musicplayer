#! /usr/bin/env python2

class Album():

    def __init__(self,name="default"):
        self.name = name
        self.songs = []


    ''' return the track following 'song'. if 'song' is the last None is returned '''
    def get_next(self,song):
        for i in range(len(self.songs)):
            if self.songs[i][0]== song and i < len(self.songs)-1:
                return self.songs[i+1]
        return None
            
