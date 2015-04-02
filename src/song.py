from os.path import splitext
from mutagen.id3 import ID3
from mutagen.mp4 import MP4


class Mp3Song:
    def __init__(self, filename):
        self.filename = filename
        
        tag = ID3(filename)
        album = tag.get('TAL')

        self.title = ', '.join(tag['TIT2'].text)
        self.album = ', '.join(album.text if album else '')

class M4aSong:
    def __init__(self, filename):
        self.filename = filename

        tag = MP4(filename)
        self.title = ', '.join(tag['\xa9nam'])
        self.album = ', '.join(tag['\xa9alb'])


def load_song(filename):
    extension = splitext(filename)[1]

    if extension == '.mp3':
        return Mp3Song(filename)

    if extension == '.m4a':
        return M4aSong(filename)
