class Artist:
    def __init__(self, artist_name):
        '''
        Initializes all necessary attributes
        '''
        self.artist_name = artist_name
        self.artist_albums = dict()
        self.artist_album_count = len(self.artist_albums)

    def get_name(self):
        '''
        Returns the name of the artist
        '''
        return self.artist_name

    def set_name(self, name_to_set):
        '''
        Sets the name of the artist to the specified name

        Inputs:
            - name_to_set (string): Name to set for the album
        '''
        self.name = name_to_set

    def get_albums(self):
        '''
        Returns the name of the albums belonging to the artist
        '''
        return self.artist_albums

    def add_album(self, album_to_add):
        '''
        Adds the specifed album to the artist's catalogue

        Inputs:
            - album_to_add (Album): Album to add to the artist's collection
        '''
        self.artist_albums[album_to_add.name] = album_to_add
        self.artist_album_count = len(self.artist_albums)

    name = property(fget = get_name, fset = set_name, doc = 'Artist name')
    albums = property(fget = get_albums, doc = 'Artist\'s albums')
    