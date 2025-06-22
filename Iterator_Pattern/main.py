from song import Song
from playlist import PlayList

PLAYLIST = PlayList()
PLAYLIST.add_song(Song("Bohemian Rhapsody", "Queen"))
PLAYLIST.add_song(Song("Imagine", "John Lennon"))
PLAYLIST.add_song(Song("Hotel California", "Eagles"))
PLAYLIST.add_song(Song("Smells Like Teen Spirit", "Nirvana"))

print("Playlist:")
for song in PLAYLIST:
    print(song)
    