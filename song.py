class Song:
    def __init__(self, song_title = '', song_artist = '', song_duration = '', song_album = '', song_year = '', song_genre = ''):
        '''
        Initializes all attributes
        '''
        self.song_title = song_title
        self.song_artist = song_artist
        self.song_duration = song_duration
        self.song_album = song_album
        self.song_year = song_year
        self.song_genre = song_genre

    def play(self):
        '''
        Plays the song
        '''
    def pause(self):
        '''
        Pauses the song
        '''
    def get_title(self):
        '''
        Gets the title of the song 
        '''
    def set_title(self, title_to_set):
        '''
        Sets the title of the song to the specified title
        '''
    def get_artist(self):
        '''
        Gets the name of the artist of the song 
        '''
    def set_artist(self, artist_to_set):
        '''
        Sets the name of the artist of the song to the specified artist name
        '''
    def get_duration(self):
        '''
        Gets the duration of the song 
        '''
    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the song to the specified duration
        '''
    def get_album(self):
        '''
        Gets the name of the album that the song belongs to
        '''
    def set_album(self, album_to_set):
        '''
        Sets the name of the album that the song belongs to the specifed album
        '''
    def get_year(self):
        '''
        Gets the release year of the song 
        '''
    def set_year(self, year_to_set):
        '''
        Sets the release year of the song to the specified year
        '''
    def get_genre(self):
        '''
        Gets the genre of the song 
        '''
    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the song to the specifed genre
        '''
    
    title = property(fget = get_title, fset = set_title, doc = 'Title of song')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of song')
    album = property(fget = get_album, fset = set_album, doc = 'Album the song is on')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Song artist')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of song')