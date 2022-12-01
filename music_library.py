from artist import *
from playlist import *
from queue import *
from song import *
import os
import eyed3

class MusicLibrary:
    def __init__(self):
        self.hidden_artists = []
        self.hidden_names = []
        self.hidden_queue = Queue()
        self.list_of_songs = []
        self.find_songs()

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
        new_song = Song(file_location, song_title = '', song_artist = '', song_duration = '', song_album = '', song_year = '', song_genre = '')
        self.list_of_songs.append(new_song)

    def return_songs(self):
        return self.list_of_songs

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
    songs = property(fget = return_songs, doc = 'Songs in the libaray')
