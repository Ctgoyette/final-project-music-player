import sys
import os
import eyed3

class Playlist:
    def __init__(self, playlist_name, playlist_file_location = None, playlist_songs = dict()):
        self.playlist_name = playlist_name
        self.playlist_songs = playlist_songs
        self.playlist_duration = 0
        self.playlist_file_location = playlist_file_location
        self.num_songs = len(self.playlist_songs)
        if playlist_file_location is None:
            self.create_new_playlist()
    
    def get_default_folder(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            default_folder = os.getcwd()
        elif sys.platform == "darwin":
            default_folder = os.getcwd()
        elif sys.platform == "win32":
            default_folder = os.path.expanduser("~\Music")
        else:
            pass
        return default_folder

    def create_new_playlist(self):
        default_folder = self.get_default_folder()
        path_to_playlist = os.path.join(default_folder, 'Playlists')
        if not os.path.exists(path_to_playlist):
            os.makedirs(path_to_playlist)
        playlist_file_name = self.playlist_name + '.m3u'
        playlist_file_location = os.path.join(path_to_playlist, playlist_file_name)
        playlist_file = open(playlist_file_location, 'w')
        playlist_file.write('#EXTM3U\n\n')
        playlist_file.close()
        self.playlist_file_location = playlist_file_location

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
        self.playlist_songs[song_to_add.title] = song_to_add
        playlist_file = open(self.playlist_file_location, 'a')
        playlist_file.write(song_to_add.song_file + '\n\n')
        playlist_file.close()

    def remove_song(self, song_to_remove):
        '''
        Removes the specified song from the playlist
        '''
        self.playlist_songs.pop(song_to_remove.title)
        with open(self.playlist_file_location, 'r') as playlist_file:
            data = playlist_file.readlines()

        search_string = song_to_remove.song_file + '\n'
        index_list = [i for i, song_file in enumerate(data) if song_file == search_string]

        index_to_remove = index_list[0]
        del data[index_to_remove + 1]
        del data[index_to_remove]

        with open(self.playlist_file_location, 'w') as playlist_file:
            playlist_file.writelines(data)

    def get_name(self):
        '''
        Gets the name of the playlist
        '''
        return self.playlist_name

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
        return self.playlist_songs

    def get_song_count(self):
        '''
        Gets the number of songs in the playlist
        '''
    
    name = property(fget = get_name, fset = set_name, doc = 'Name of playlist')
    duration = property(fget = get_duration, fset = set_duration, doc = 'Duration of playlist')
    songs = property(fget = get_songs, doc = 'Songs in the playlist')
    song_count = property(fget = get_song_count, doc = 'Number of songs in playlist')
