#!/usr/bin/env python2

import main
import os
import fnmatch
import eyed3

class MMP():

    def __init__(self):
        self.read_paths()
        self.load_music()

    def read_paths(self):
        f = open(main.PATH_FILE,"a+")
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
        self.music_files = []
        for line in self.paths:
            for root, dirs, files in os.walk(line):
                for files in fnmatch.filter(files, '*.mp3'):
                    self.music_files.append(os.path.join(root,files))
