class Artist:
    def __init__(self, artist_name = '', artist_albums = []):
        '''
        Initializes all attributes
        '''
        self.artist_name = artist_name
        self.artist_albums = artist_albums
        self.artist_album_count = len(artist_albums)