class Playlist:
    def __init__(self, playlist_name, playlist_songs = [], playlist_duration = ''):
        self.playlist_name = playlist_name
        self.playlist_songs = playlist_songs
        self.playlist_duration = playlist_duration
        self.song_count = len(playlist_songs)
    
    def play(self):
        '''
        Plays all the songs in the playlist beginning with the first song
        '''
    def shuffle_play(self):
        '''
        Plays all the songs in the playlist in a randomly shuffled order
        '''
    def add_song(self, song_to_add):
        '''
        Adds the specified song to the playlist
        '''
    def remove_song(self, song_to_remove):
        '''
        Removes the specified song from the playlist
        '''
    def get_name(self):
        '''
        Gets the name of the playlist
        '''
    def set_name(self):
        '''
        Sets the name of the playlist
        '''
    def get_duration(self):
        '''
        Gets the duration of the playlist
        '''
    def set_duration(self, duration_to_set):
        '''
        Sets the duration of the playlist to the specified value
        '''
    def get_songs(self):
        '''
        Gets all the songs in the playlist
        '''
    def get_song_count(self):
        '''
        Gets the number of songs in the playlist
        '''
    
    name = property(fget = get_name, fset = set_name, doc = 'Name of playlist')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of playlist')
    songs = property(fget = get_songs, doc = 'Songs in the playlist')
    song_count = property(fget = get_song_count, doc = 'Number of songs in playlist')
