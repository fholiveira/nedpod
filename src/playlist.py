from os.path import abspath, join, dirname, splitext, basename
from song import load_song


class Playlist:
    def __init__(self, filename):
        self.name = splitext(basename(filename))[0]
        self.filename = dirname(abspath(filename))

        with open(filename) as playlist:
           self._songs = [line.strip() for line in playlist.readlines() 
                          if not line.startswith('#')]

    def __iter__(self):
        for song_path in self._songs:
            yield load_song(join(self.filename, song_path))
