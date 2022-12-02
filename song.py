import eyed3
eyed3.log.setLevel("ERROR")
class Song:
    def __init__(self, file):
        '''
        Initializes all attributes
        '''
        self.audio_file = eyed3.load(file)
        self.song_title = self.audio_file.tag.title
        self.song_artist = self.audio_file.tag.artist
        self.song_duration = self.audio_file.info.time_secs
        self.song_duration_formatted = self.convert_duration_to_display_format()
        self.song_album = self.audio_file.tag.album
        self.song_year = self.audio_file.tag.getBestDate()
        self.song_genre = self.audio_file.tag.genre
        # self.song_track_number = self.audio_file.tag.track

    def convert_duration_to_display_format(self):
        minutes = int(self.song_duration) // 60
        seconds = int(self.song_duration) % 60
        formatted_duration = '{0}:{0:0>2}'.format(minutes, seconds)
        return formatted_duration

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
        return self.song_title

    def set_title(self, title_to_set):
        '''
        Sets the title of the song to the specified title
        '''
    def get_artist(self):
        '''
        Gets the name of the artist of the song 
        '''
        return self.song_artist

    def set_artist(self, artist_to_set):
        '''
        Sets the name of the artist of the song to the specified artist name
        '''
    def get_duration(self):
        '''
        Gets the duration of the song 
        '''
        return self.song_duration

    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the song to the specified duration
        '''
    
    def get_duration_formatted(self):
        '''
        Gets the duration of the song 
        '''
        return self.song_duration_formatted

    def get_album(self):
        '''
        Gets the name of the album that the song belongs to
        '''
        return self.song_album

    def set_album(self, album_to_set):
        '''
        Sets the name of the album that the song belongs to the specifed album
        '''
    def get_year(self):
        '''
        Gets the release year of the song 
        '''
        return self.song_year

    def set_year(self, year_to_set):
        '''
        Sets the release year of the song to the specified year
        '''
    def get_genre(self):
        '''
        Gets the genre of the song 
        '''
        return self.song_genre

    def set_genre(self, genre_to_set):
        '''
        Sets the genre of the song to the specifed genre
        '''
    
    title = property(fget = get_title, fset = set_title, doc = 'Title of song')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of song')
    duration_formatted = property(fget = get_duration_formatted, doc = 'Duration of song in displayable format')
    album = property(fget = get_album, fset = set_album, doc = 'Album the song is on')
    artist = property(fget = get_artist, fset = set_artist, doc = 'Song artist')
    year = property(fget = get_year, fset = set_year, doc = 'Song release year')
    genre = property(fget = get_genre, fset = set_genre, doc = 'Genre of song')