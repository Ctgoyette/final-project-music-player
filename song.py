class Song:
    def __init__(self, song_title = '', song_artist = '', song_duration = '', song_album = '', song_genre = ''):
        '''
        Initializes all attributes
        '''
        self.song_title = song_title
        self.song_duration = song_duration
        self.song_album = song_album
        self.song_artist = song_artist
        self.song_genre = song_genre

    def play(self):
        '''
        Plays the specified song
        '''
    def pause(self):
        '''
        Pauses the specified song
        '''
    def get_title():
        '''
        Gets the name of the specified song 
        '''
    def set_title():
        '''
        Gets the name of the specified song 
        '''
    def get_duration():
        '''
        Gets the name of the specified song 
        '''
    def set_duration():
        '''
        Gets the name of the specified song 
        '''
    def get_album():
        '''
        Gets the name of the specified song 
        '''
    def set_album():
        '''
        Gets the name of the specified song 
        '''
    def get_artist():
        '''
        Gets the name of the specified song 
        '''
    def set_artist():
        '''
        Gets the name of the specified song 
        '''
    def get_genre():
        '''
        Gets the name of the specified song 
        '''
    def set_genre():
        '''
        Gets the name of the specified song 
        '''
    
    title = property(fget = get_title, fset = set_title, doc='Title of song')
    duration = property(fget = get_duration, fset = set_duration, doc='Duration of song')
    album = property(fget = get_album, fset = set_album, doc='Album the song is on')
    artist = property(fget = get_artist, fset = set_artist, doc='Song artist')
    genre = property(fget = get_genre, fset = set_genre, doc='Genre of artist')