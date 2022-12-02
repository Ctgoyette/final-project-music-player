import song

class Album:
    def __init__(self, album_name = '', album_artist = '', album_year = '', album_genre = ''):
        self.album_songs = []
        self.album_name = album_name
        self.album_artist = album_artist
        # self.album_duration = album_duration
        self.album_year = album_year
        self.album_genre = album_genre
        self.album_song_count = len(self.album_songs)

    def play_album(self):
        '''
        Plays the songs in an album beginning with the first song
        '''
    def get_name(self):
        '''
        Gets the name of the album 
        '''
    def set_name(self, name_to_set):
        '''
        Sets the name of the album to the specified name
        '''
    def get_artist(self):
        '''
        Gets the name of the album artist
        '''
    def set_artist(self, artist_to_set):
        '''
        Sets the name of the album artist to the specfied artist name
        '''
    def get_duration(self):
        '''
        Gets the duration of the album 
        '''
    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the album to the specfied duration
        '''
    def get_year(self):
        '''
        Gets the release year of the album 
        '''
    def set_year(self, year_to_set):
        '''
        Sets the release year of the album to the specified year
        '''
    def get_genre(self):
        '''
        Gets the genre of the album 
        '''
    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the album to the specified genre
        '''
    def get_song_count(self):
        '''
        Gets the number of songs in an album
        '''
    def add_song(self, song_to_add):
        '''
        Adds a song to an album
        '''
    def remove_song(self, song_to_remove):
        '''
        Removes a song from an album
        '''
    def get_songs(self):
        '''
        Gets the songs in an album
        '''
    
    name = property(fget = get_name, fset = set_name, doc = 'Name of album')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Album artist')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of album')
    year = property(fget = get_year, fset = set_year, doc = 'Year album was released')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of album')
    song_count = property(fget = get_song_count, doc = 'Number of songs in album')
    songs = property(fget = get_songs, doc = 'Songs in album')

