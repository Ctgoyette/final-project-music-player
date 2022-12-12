import sys
import os

class Playlist:
    def __init__(self, playlist_name, playlist_file_location = None, playlist_songs = dict()):
        '''
        Initializes all necessary attributes
        '''
        self.playlist_name = playlist_name
        self.playlist_songs = playlist_songs
        self.playlist_file_location = playlist_file_location
        self.num_songs = len(self.playlist_songs)
        if playlist_file_location is None:
            self.create_new_playlist_file()
    
    def get_default_folder(self):
        '''
        Returns the default folder for the music library depending on the operating system
        '''
        if sys.platform == "linux" or sys.platform == "linux2":
            default_folder = os.getcwd()
        elif sys.platform == "darwin":
            default_folder = os.getcwd()
        elif sys.platform == "win32":
            default_folder = os.path.expanduser("~\Music")
        else:
            pass
        return default_folder

    def create_new_playlist_file(self):
        '''
        Creates a new empty playlist file with the specified name in the default music library folder
        '''
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

    def add_song(self, song_to_add):
        '''
        Adds the specified song to the playlist and to the playlist file

        Inputs:
            - song_to_add (Song): Song to remove from the playlist
        '''
        self.playlist_songs[song_to_add.title] = song_to_add
        playlist_file = open(self.playlist_file_location, 'a')
        playlist_file.write(song_to_add.song_file + '\n\n')
        playlist_file.close()

    def remove_song(self, song_to_remove):
        '''
        Removes the specified song from the playlist and the playlist file
        
        Inputs:
            - song_to_remove (Song): Song to remove from the playlist
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
        Returns the name of the playlist
        '''
        return self.playlist_name

    def get_songs(self):
        '''
        Returns all the songs in the playlist
        '''
        return self.playlist_songs
    
    name = property(fget = get_name, doc = 'Name of playlist')
    songs = property(fget = get_songs, doc = 'Songs in the playlist')
