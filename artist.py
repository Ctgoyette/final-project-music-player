class Artist:
    def __init__(self, artist_name):
        '''
        Initializes all attributes
        '''
        self.artist_name = artist_name
        self.artist_albums = []
        self.artist_album_count = len(self.artist_albums)

    def get_name(self):
        '''
        Gets the name of the artist
        '''
        return self.artist_name

    def set_name(self, name_to_set):
        '''
        Sets the name of the artist to the specified name
        '''
    def get_albums(self):
        '''
        Gets the name of the albums belonging to the artist
        '''
        return self.artist_albums

    def add_album(self, album_to_add):
        '''
        Adds the specifed album to the artist's catalogue
        '''
        self.artist_albums.append(album_to_add)
        self.artist_album_count = len(self.artist_albums)

    def remove_album(self, album_to_remove):
        '''
        Removes the specified album from the artist's catalogue
        '''

    name = property(fget = get_name, fset = set_name, doc = 'Artist name')
    albums = property(fget = get_albums, doc = 'Artist\'s albums')
    