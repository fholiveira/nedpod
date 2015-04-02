from os.path import splitext, basename
from mutagen.id3 import ID3
from mutagen.mp4 import MP4
import logging


class Music:
    def __init__(self, filename):
        self.filename = filename
        self.title, self.album = self.load_audio_info()
        
    def load_audio_info(self):
        title, album = (splitext(basename(self.filename))[0] , '')

        try:
            tags = self._get_tags()

            title = self._get_title(tags)
            album = self._get_album(tags)
        except:
            logging.error("The music file {path} does not have audio tags.".format(path=self.filename))

        return (title, album)


class Mp3Music(Music):
    def _get_tags(self):
        return ID3(self.filename)

    def _get_title(self, tags):
        try:
            return ', '.join(tags['TIT2'].text)
        except:
            logging.error('Could not find the music title in the file "{path}".'.format(path=self.filename))

        return splitext(basename(self.filename))[0]
        
    def _get_album(self, tags):
        try:
            return ', '.join(tags['TAL'].text)
        except:
            logging.error('Could not find the music album title in the file "{path}".'.format(path=self.filename))

        return ''


class M4aMusic(Music):
    def _get_tags(self):
        return MP4(self.filename)

    def _get_title(self, tags):
        try:
            return ', '.join(tags['\xa9nam'])
        except:
            logging.error('Could not find the music title in the file "{path}".'.format(path=self.filename))

        return splitext(basename(self.filename))[0]
        
    def _get_album(self, tags):
        try:
            return ', '.join(tags['\xa9alb'])
        except:
            logging.error('Could not find the music album title in the file "{path}".'.format(path=self.filename))

        return ''


def load_song(filename):
    extension = splitext(filename)[1]

    if extension == '.mp3':
        return Mp3Music(filename)

    if extension == '.m4a':
        return M4aMusic(filename)
