from artist import *
from playlist import *
from song import *
from album import *
import os
import eyed3

class MusicLibrary:
    def __init__(self):
        self.list_of_songs = []
        self.list_of_albums = []
        self.list_of_artists = []
        self.num_songs = len(self.list_of_songs)
        self.num_albums = len(self.list_of_albums)
        self.num_artists = len(self.list_of_artists)
        self.find_songs()
        self.sort_object_list(self.list_of_artists, 'name')
        self.sort_object_list(self.list_of_albums, 'name')

    def find_songs(self, location = None):
        if location is None:
            for root, dirs, files in os.walk(r'C:\Users\Casey\Music'):
                # select file name
                for file in files:
                    # check the extension of files
                    if file.endswith('.mp3'):
                        # print whole path of files
                        file_path = (os.path.join(root, file))
                        self.add_song(file_path)
                        
        else:
            pass

    def add_song(self, file_location):
        '''
        Adds the song at the specified file location to the list of songs in the library. Also adds the album and
        artist of the song if they do not yet exist in the library
        '''
        new_song = Song(file_location)
        is_add_album = True
        is_add_artist = True
        for album in self.list_of_albums:
            if new_song.album == album.name:
                is_add_album = False
                break
            else:
                pass
        for artist in self.list_of_artists:
            if new_song.artist == artist.name:
                is_add_artist = False
                break
            else:
                pass
        if is_add_album:
            self.add_album(new_song)
        if is_add_artist:
            self.add_artist(new_song)
        self.list_of_songs.append(new_song)
        self.num_songs = len(self.list_of_songs)
    
    def add_album(self, song_with_album_info):
        '''
        Adds the album of the specified song to the list of albums in the library
        '''
        new_album = Album(song_with_album_info.album, song_with_album_info.artist, song_with_album_info.year, song_with_album_info.genre)
        self.list_of_albums.append(new_album)
        self.num_albums = len(self.list_of_albums)

    def add_artist(self, song_with_artist_info):
        '''
        Adds the specified artist
        '''
        new_artist = Artist(song_with_artist_info.artist)
        self.list_of_artists.append(new_artist)
        self.num_artists = len(self.list_of_artists)

    def get_songs(self):
        return self.list_of_songs
    
    def get_albums(self):
        return self.list_of_albums
    
    def get_artists(self):
        return self.list_of_artists

    def sort_object_list(self, list_to_sort, sort_attribute):
        '''
        Sorts the specifed list of objects by the specified object attribute

        Inputs:
            - (list) list of objects to sort => list_to_sort
            - (string) name of the attribute to sort by => sort_attribute
        '''
        for current_index in range(1, len(list_to_sort)):
                sort_key = getattr(list_to_sort[current_index], sort_attribute)
                object_key = list_to_sort[current_index]

                last_index = current_index - 1
                while last_index >= 0 and sort_key < getattr(list_to_sort[last_index], sort_attribute):
                    list_to_sort[last_index + 1] = list_to_sort[last_index]
                    last_index -= 1
                list_to_sort[last_index + 1] = object_key

    def create_playlist(self, playlist_name):
        '''
        Creates a new playlist with the specified name
        '''
    def delete_playlist(self, playlist_to_remove):
        '''
        Deletes the specified playlist
        '''
    def get_playlists(self):
        '''
        Gets all of the playlists in the library
        '''
    
    artists = property(fget = get_artists, doc = 'Artists in the libryar')
    albums = property(fget = get_albums, doc = 'Albums in the library')
    playlists = property(fget = get_playlists, doc = 'Playlists in the library')
    songs = property(fget = get_songs, doc = 'Songs in the libaray')