class MusicLibrary:
    def __init__(self, artists, playlists, queue):
        self.artists = artists
        self.playlists = playlists
        self.queue = queue

    def create_playlist(self, playlist_name):
        '''
        Creates a new playlist with the specified name
        '''
    def delete_playlist(self, playlist_to_remove):
        '''
        Deletes the specified playlist
        '''
    def get_artists(self):
        '''
        Gets all of the artists in the library
        '''
    def get_playlists(self):
        '''
        Gets all of the playlists in the library
        '''
    def add_artist(self, artist_to_add):
        '''
        Adds the specified artist
        '''
    
    artists = property(fget = get_artists, doc = 'Artists in the library')
    playlists = property(fget = get_playlists, doc = 'Playlists in the library')
