class Queue:
    def __init__(self, songs = []):
        self.hidden_songs = songs
        self.hidden_song_count = len(songs)

    def add_song(self, song_to_add):
        '''
        Adds the specfied song to the queue
        '''
    def remove_song(self, song_to_remove):
        '''
        Removes the specified song from the queue
        '''
    def get_songs(self):
        '''
        Gets all the songs in the queue
        '''
    def get_song_count(self):
        '''
        Gets all the songs in the queue
        '''
    
    songs = property(fget = get_songs, doc = 'Songs in the queue')
    song_count = property(fget = get_song_count, doc = 'Number of songs in queue')

