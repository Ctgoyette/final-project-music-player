from artist import *
from playlist import *
from song import *
from album import *
import os
import eyed3
import operator

class MusicLibrary:
    def __init__(self):
        self.list_of_songs = dict()
        self.list_of_albums = dict()
        self.list_of_artists = dict()
        self.dict_of_playlists = dict()
        self.num_songs = len(self.list_of_songs)
        self.num_albums = len(self.list_of_albums)
        self.num_artists = len(self.list_of_artists)
        self.library_file_locations = []

    def find_songs(self, location):
        '''
        Searches the specified directory and all its subdirectories for MP3 and M3U files.
        Adds the MP3 files to the list of songs in the library and creates playlists from the M3U files.
        '''
        for root, dirs, files in os.walk(location):
            # select file name
            for file in files:
                # check the extension of files
                if file.endswith('.mp3'):
                    # print whole path of files
                    file_path = (os.path.join(root, file))
                    self.add_song(file_path)

                elif file.endswith('.m3u'):
                    file_path = (os.path.join(root, file))
                    file_name = os.path.basename(file_path)
                    file_name_raw = os.path.splitext(file_name)
                    self.create_playlist(file_name_raw[0], file_path)

                else:
                    pass

    def add_song(self, file_location):
        '''
        Adds the song at the specified file location to the list of songs in the library. Also adds the album and
        artist of the song if they do not yet exist in the library
        '''
        new_song = Song(file_location)
        is_add_album = True
        for album in self.list_of_albums.values():
            if new_song.album == album.name:
                is_add_album = False
                album.add_song(new_song)
                break
            else:
                pass
        if is_add_album:
            self.add_album(new_song)
        self.list_of_songs[new_song.title] = new_song
        self.num_songs = len(self.list_of_songs.keys())
    
    def add_album(self, song_with_album_info):
        '''
        Adds the album of the specified song to the list of albums in the library, and adds the album's artist if the artist does not yet 
        exist in the library. Also adds the specified song to the album's song list
        '''
        new_album = Album(song_with_album_info.album, song_with_album_info.artist, song_with_album_info.year, song_with_album_info.genre)
        is_add_artist = True
        for artist in self.list_of_artists.values():
            if new_album.artist == artist.name:
                is_add_artist = False
                artist.add_album(new_album)
                break
            else:
                pass
        if is_add_artist:
            self.add_artist(new_album)
        self.list_of_albums[new_album.name] = new_album
        self.num_albums = len(self.list_of_albums)
        new_album.add_song(song_with_album_info)

    def add_artist(self, album_with_artist_info):
        '''
        Adds the specified artist to the list of artists in the library, and adds the specified album to the artist's album list
        '''
        new_artist = Artist(album_with_artist_info.artist)
        self.list_of_artists[new_artist.name] = new_artist
        self.num_artists = len(self.list_of_artists)
        new_artist.add_album(album_with_artist_info)

    def get_songs(self):
        return self.list_of_songs
    
    def get_albums(self):
        return self.list_of_albums
    
    def get_artists(self):
        return self.list_of_artists

    def sort_object_list(self, list_to_sort, sort_attribute):
        '''
        Sorts the specifed list of objects by the specified object attribute using insertion sort

        Inputs:
            - (list) list of objects to sort => list_to_sort
            - (string) name of the attribute to sort by => sort_attribute
        '''
        if type(list_to_sort) is not dict:
            for current_index in range(1, len(list_to_sort)):
                    sort_key = getattr(list_to_sort[current_index], sort_attribute)
                    object_key = list_to_sort[current_index]

                    last_index = current_index - 1
                    while last_index >= 0 and sort_key < getattr(list_to_sort[last_index], sort_attribute):
                        list_to_sort[last_index + 1] = list_to_sort[last_index]
                        last_index -= 1
                    list_to_sort[last_index + 1] = object_key
        else:
            # temp_dict = dict()
            # for key in (sorted(list_to_sort.values(), key=operator.attrgetter(sort_attribute))):
            #     try:
            #         temp_dict[key.title] = key
            #     except:
            #         temp_dict[key.name] = key
            # list_to_sort = temp_dict
            temp_list = list(list_to_sort.values())
            for current_index in range(1, len(temp_list)):
                    sort_key = getattr(temp_list[current_index], sort_attribute)
                    object_key = temp_list[current_index]

                    last_index = current_index - 1
                    while last_index >= 0 and sort_key < getattr(temp_list[last_index], sort_attribute):
                        temp_list[last_index + 1] = temp_list[last_index]
                        last_index -= 1
                    temp_list[last_index + 1] = object_key
            list_to_sort.clear()
            for item in temp_list:
                try:
                    list_to_sort[item.title] = item
                except:
                    list_to_sort[item.name] = item
    
    def sort_all_album_tracks(self):
        for album in self.list_of_albums.values():
            self.sort_object_list(album.songs, 'track_num')

    def sort_all_albums(self):
        self.sort_object_list(self.list_of_albums, 'artist')

    def sort_all_artists(self):
        self.sort_object_list(self.list_of_artists, 'name')
    
    def sort_all_songs(self):
        self.sort_all_album_tracks()
        self.list_of_songs.clear()
        for album in self.list_of_albums.values():
            for song in album.songs.values():
                self.list_of_songs[song.title] = song
    
    def add_library_file_location(self, location = None):
        self.library_file_locations.append(location)
        self.find_songs(location)
        self.sort_all_albums()
        self.sort_all_artists()
        self.sort_all_songs()

    def create_playlist(self, playlist_name, file_location = None):
        '''
        Creates a new playlist with the specified name
        '''
        if file_location is None:
            new_playlist = Playlist(playlist_name)
        else:
            playlist_songs = dict()
            playlist_file= open(file_location, 'r')
            for line in playlist_file.readlines():
                if line == '\n' or line[0] == '#':
                    pass
                else:
                    raw_file_location = line.strip('\n')
                    self.add_song(raw_file_location)
                    song_file = eyed3.load(raw_file_location)
                    song_title = song_file.tag.title
                    playlist_songs[song_title] = self.list_of_songs[song_title]
            new_playlist = Playlist(playlist_name, file_location, playlist_songs)
        self.dict_of_playlists[playlist_name] = new_playlist
        
    def delete_playlist(self, playlist_to_remove):
        '''
        Deletes the specified playlist
        '''
        if os.path.exists(playlist_to_remove.playlist_file_location):
            os.remove(playlist_to_remove.playlist_file_location)
        self.playlists.pop(playlist_to_remove.name)

    def get_playlist(self, playlist):
        '''
        Returns the specified playlist
        '''
        return self.dict_of_playlists[playlist]
    
    def get_playlists(self):
        '''
        Gets all of the playlists in the library
        '''
        return self.dict_of_playlists

    def add_playlist_song(self, playlist, song):
        self.dict_of_playlists[playlist].add_song(song)

    def remove_playlist_song(self, playlist, song):
        playlist.remove_song(song)
    
    artists = property(fget = get_artists, doc = 'Artists in the libryar')
    albums = property(fget = get_albums, doc = 'Albums in the library')
    playlists = property(fget = get_playlists, doc = 'Playlists in the library')
    songs = property(fget = get_songs, doc = 'Songs in the library')