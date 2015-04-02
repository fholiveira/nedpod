from os.path import join, abspath
from song import Mp3Music
from os import makedirs
from shutil import copy
from re import sub


class FileSystem:
    def __init__(self, path):
        self.songs_path = join(abspath(path), 'songs')
        self.speakables_path = join(abspath(path), 'speakables')

        makedirs(self.songs_path)
        makedirs(self.speakables_path)

    def create_playlist(self, playlist):
        foldername = self.build_filename(playlist.name)

        folder = join(self.songs_path,  foldername)
        speach = join(self.speakables_path, foldername)

        makedirs(folder)
        makedirs(speach)

        return (folder, speach + '.mp3')

    def create_song(self, playlist, song):
        extension = '.mp3' if isinstance(song, Mp3Music) else '.m4a' 
        filename = self.build_filename(song.title)

        foldername = self.build_filename(playlist.name)

        song_file = join(self.songs_path, foldername, filename) + extension
        speach_file = join(self.speakables_path, foldername, filename) + '.mp3'

        return (song_file, speach_file)
        
    def build_filename(self, name):
        return sub('[^\w ]', '', name.replace(' ', '_').lower())

