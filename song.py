import eyed3
eyed3.log.setLevel("ERROR")
class Song:
    def __init__(self, file):
        '''
        Initializes all necessary attributes. If the necessary metadata does not exist in the file, sets all attributes to 'Unknown'
        '''
        self.audio_file = eyed3.load(file)
        try:
            self.song_title = self.audio_file.tag.title
            self.song_artist = self.audio_file.tag.artist
            self.song_duration = self.audio_file.info.time_secs
            self.song_duration_formatted = self.convert_duration_to_display_format()
            self.song_album = self.audio_file.tag.album
            self.song_year = str(self.audio_file.tag.getBestDate())
            self.song_genre = self.audio_file.tag.genre
            self.track_num = self.audio_file.tag.track_num[0]
        except:
            self.song_title = 'Unknown'
            self.song_artist = 'Unknown'
            self.song_duration = 0
            self.song_duration_formatted = '00:00'
            self.song_album = 'Unknown'
            self.song_year = 'Unknown'
            self.song_genre = 'Unknown'
            self.track_num = 'Unknown'
        self.song_file = file

    def convert_duration_to_display_format(self):
        '''
        Converts the song_duration attribute of the object to a string in the format `MM:SS` and returns the result
        '''
        minutes = int(self.song_duration // 60)
        seconds = int(self.song_duration % 60)
        formatted_duration = f'{minutes:02}:{seconds:02}'
        return formatted_duration

    def get_title(self):
        '''
        Returns the title of the song 
        '''
        return self.song_title

    def set_title(self, title_to_set):
        '''
        Sets the title of the song to the specified title
        
        Inputs:
            - title_to_set (string): Title to set for the song
        '''
        self.song_title = title_to_set

    def get_artist(self):
        '''
        Returns the name of the artist of the song 
        '''
        return self.song_artist

    def set_artist(self, artist_to_set):
        '''
        Sets the name of the artist of the song to the specified artist name

        Inputs:
            - artist_to_set (string): Artist to set for the song
        '''
        self.song_artist = artist_to_set

    def get_duration(self):
        '''
        Returns the duration of the song 
        '''
        return self.song_duration

    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the song to the specified duration

        Inputs:
            - duration_to_set (float): Duration to set for the song
        '''
        self.song_duration = duration_to_set

    def get_duration_formatted(self):
        '''
        Returns the duration of the song 
        '''
        return self.song_duration_formatted

    def get_album(self):
        '''
        Returns the name of the album that the song belongs to
        '''
        return self.song_album

    def set_album(self, album_to_set):
        '''
        Sets the name of the album that the song belongs to the specifed album

        Inputs:
            - album_to_set (string): Album to set for the song
        '''
        self.song_album = album_to_set

    def get_year(self):
        '''
        Returns the release year of the song 
        '''
        return self.song_year

    def set_year(self, year_to_set):
        '''
        Sets the release year of the song to the specified year

        Inputs:
            - year_to_set (string): Year to set for the song
        '''
        self.song_year = year_to_set

    def get_genre(self):
        '''
        Returns the genre of the song 
        '''
        return self.song_genre

    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the song to the specifed genre

        Inputs:
            - genre_to_set (string): Genre to set for the song
        '''
        self.song_genre = genre_to_set
    
    title = property(fget = get_title, fset = set_title, doc = 'Title of song')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of song')
    duration_formatted = property(fget = get_duration_formatted, doc = 'Duration of song in displayable format')
    album = property(fget = get_album, fset = set_album, doc = 'Album the song is on')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Song artist')
    year = property(fget = get_year, fset = set_year, doc = 'Song release year')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of song')
