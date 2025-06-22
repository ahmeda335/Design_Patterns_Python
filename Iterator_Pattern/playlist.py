from iterator import PlayListIterator

class PlayList:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def __iter__(self):
        return PlayListIterator(self._songs)
        