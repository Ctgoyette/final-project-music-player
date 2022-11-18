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
        Plays the specified song
        '''
    def pause(self):
        '''
        Pauses the specified song
        '''
    def get_title(self):
        '''
        Gets the name of the specified song 
        '''
    def set_title(self, title_to_set):
        '''
        Sets the name of the specified song 
        '''
    def get_artist(self):
        '''
        Gets the name of the artist of the specified song 
        '''
    def set_artist(self, artist_to_set):
        '''
        Sets the name of the artist of the specified song 
        '''
    def get_duration(self):
        '''
        Gets the duration of the specified song 
        '''
    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the specified song 
        '''
    def get_album(self):
        '''
        Gets the name of the album that the specified song belongs to
        '''
    def set_album(self, album_to_set):
        '''
        Sets the name of the album that the specified song belongs to
        '''
    def get_year(self):
        '''
        Gets the release year of the specified song 
        '''
    def set_year(self, year_to_set):
        '''
        Sets the release year of the specified song 
        '''
    def get_genre(self):
        '''
        Gets the genre of the specified song 
        '''
    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the specified song 
        '''
    
    title = property(fget = get_title, fset = set_title, doc = 'Title of song')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of song')
    album = property(fget = get_album, fset = set_album, doc = 'Album the song is on')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Song artist')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of song')