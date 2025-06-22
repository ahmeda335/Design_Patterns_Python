class PlayListIterator:
    def __init__(self, songs):
        self._songs = songs
        self._position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._position >= len(self._songs):
            raise StopIteration
        song = self._songs[self._position]
        self._position += 1
        return song
