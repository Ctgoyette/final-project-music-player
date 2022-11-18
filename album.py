import song

class Album:
    def __init__(self, album_songs = [], album_name = '', album_duration = '', album_year = '', album_genre = ''):
        self.album_songs = album_songs
        self.album_name = album_name
        self.album_duration = album_duration
        self.album_year = album_year
        self.album_genre = album_genre
        self.album_song_count = len(album_songs)

    def play_album(self):
        '''
        Plays the songs in an album beginning with the first song
        '''
