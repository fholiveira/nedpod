from filesystem import FileSystem
from shutil import copy


class Jukebox:
    def __init__(self, speaker, path):
        self.speaker = speaker
        self.file_system = FileSystem(path)

    def write_playlist(self, playlist):
        _, speach = self.file_system.create_playlist(playlist) 

        lang = self.speaker.discover_language(playlist.name)
        self.speaker.record(playlist.name, language=lang).save(speach)

        for song in playlist:
            song_file, speach = self.file_system.create_song(playlist, song) 

            copy(song.filename, song_file)

            lang = self.speaker.discover_language(song.title, song.album)
            self.speaker.record(song.title, language=lang).save(speach)
