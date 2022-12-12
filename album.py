import song

class Album:
    def __init__(self, album_name = '', album_artist = '', album_year = '', album_genre = ''):
        '''
        Initializes all necessary attributes
        '''
        self.album_songs = dict()
        self.album_name = album_name
        self.album_artist = album_artist
        self.album_year = album_year
        self.album_genre = album_genre
        self.album_song_count = len(self.album_songs)

    def get_name(self):
        '''
        Returns the name of the album 
        '''
        return self.album_name

    def set_name(self, name_to_set):
        '''
        Sets the name of the album to the specified name

        Inputs:
            - name_to_set (string): Name to set for the album
        '''
        self.name = name_to_set

    def get_artist(self):
        '''
        Returns the name of the album artist
        '''
        return self.album_artist

    def set_artist(self, artist_to_set):
        '''
        Sets the name of the album artist to the specfied artist name

        Inputs:
            - artist_to_set (string): Artist to set for the album
        '''
        self.album_artist = artist_to_set

    def get_year(self):
        '''
        Returns the release year of the album 
        '''
        return self.album_year

    def set_year(self, year_to_set):
        '''
        Sets the release year of the album to the specified year

        Inputs:
            - year_to_set (string): Year to set for the album
        '''
        self.album_year = year_to_set 

    def get_genre(self):
        '''
        Returns the genre of the album 
        '''
        return self.album_genre

    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the album to the specified genre

        Inputs:
            - genre_to_set (string): Genre to set for the album
        '''
        self.album_genre = genre_to_set
    
    def get_song_count(self):
        '''
        Returns the number of songs in an album
        '''
        return self.album_song_count

    def add_song(self, song_to_add):
        '''
        Adds the specified song to the album

        Inputs:
            - song_to_add (Song): Song to add to the album
        '''
        self.album_songs[song_to_add.title] = song_to_add
        self.album_song_count = len(self.album_songs)

    def get_songs(self):
        '''
        Returns the songs in an album
        '''
        return self.album_songs
    
    name = property(fget = get_name, fset = set_name, doc = 'Name of album')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Album artist')
    year = property(fget = get_year, fset = set_year, doc = 'Year album was released')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of album')
    song_count = property(fget = get_song_count, doc = 'Number of songs in album')
    songs = property(fget = get_songs, doc = 'Songs in album')

