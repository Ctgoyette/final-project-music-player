SUMMARY:

   This program is a music player application that allows the user to browse, play, and manage MP3 files on their computer using a graphical user interface (GUI). The program uses the cross-platform “PyQt5” library to create the GUI for the application. The code also makes use of the “qdarktheme” library to apply a dark color scheme to the GUI, giving the application an aesthetically pleasing look.
   The application has a number of features for browsing and playing music from a music library within the GUI. In the GUI, the user can view their music library by artist, album, or track, and can switch between these views using a dropdown menu. Double-clicking on an artist or album in the artist or album view will open a page with more detailed information about the artist or album, and allow the user to play all of the tracks from that artist or album by double clicking on the desired song. When viewing their library by track, the user can also double click on a specific track to play it. The code uses the tools built into the PyQt5 library to handle playback of audio files. All songs, artists, and albums are stored as an object of either “Song”, “Album”, and “Artist”. To determine the information stored in each object, such as the artist and album information, the “eyed3” library is used to read metadata from each MP3 file in the library.
   In addition to browsing and playing music from the library, the application also allows the user to create and manage playlists. The user can create a new playlists, delete playlists, add tracks to playlsits from their music library, remove tracks, and can play the tracks in a playlist in the order they were added to the playlist. Each playlist is an object of its own class, “Playlist”, and each playlist created is stored in an M3U file, one of the most common playlist file formats. The application also includes a settings page where the user can see the currently added library file locations, and add other file locations to search for music. If the user is on a Windows operating system, when the application is started, the program will automatically search for and load all playlists of filetype M3U and songs of filetype MP3 in “C:\Users\<user>\Music”.


CLASS OVERVIEW:

   For the most part, each of the classes below contain objects of other classes in their attributes. The only class that inherits from another class is PlayerWindow() which inherits from Ui_MainWindow(). Ui_MainWindow() is the class that contains the code generated by the GUI designer which helped visualize the layout the GUI before functionality was added. Becuase of the complexity of many of the classes, each class was separated into its own file. An overview of all classes and their attributes can be seen below. Not that Ui_MainWindow() is not included in the following explanations as it was proceduraly generated with hundreds of attributes:

class PlayerWindow(base_gui.Ui_MainWindow)
 |  Attributes defined here:
 |
 |  self.last_content_page_index_album = 0 # Index of last content page when switching to album page
 |  self.last_content_page_index_artist = 0 # Index of last content page when switching to artist page
 |  self.selected_artist = None # The currently selected artist
 |  self.selected_album = None # The currently selected album
 |  self.selected_playlist = None # The currently selected playlist
 |
 |  Method resolution order:
 |      PlayerWindow
 |      base_gui.Ui_MainWindow
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initializes all required attributes and runs all function needed to properly setup the GUI
 |
 |  add_library_location(self)
 |      Opens the user's file manager allowing the user to select a folder to add to their music library. Once selected, adds the songs and playlists from specified file location
 |      to the display tables in the GUI
 |
 |  add_table_items(self, items_to_add, table, table_headings, attributes_to_add)
 |      Adds the specified attributes of the specified items to the given table with the given table headings
 |
 |      Inputs:
 |          - items_to_add (list): The list of items to add to the table
 |          - table (QTableWidget): The table to add the items to
 |          - table_headings (list): The list of column headings for the table
 |          - attributes_to_add (list): The list of attributes of the items to add as table cells
 |
 |  add_table_row(self, table)
 |      Adds a row to the specific table in the GUI
 |
 |      Inputs:
 |          - table (QTableWidget): The table to add the row to
 |
 |  add_to_playlist(self, playlist_clicked, selected_song)
 |      Calls the function necessary to add the specified song to the specified playlist in the application's music library
 |
 |      Inputs:
 |          - playlist_clicked (string): The name of the playlist the song should be added to
 |          - selected_song (Song): The song to be added to the playlist
 |
 |  album_double_clicked(self, current_display_table, associated_library_list)
 |      Displays the album page for the selected album when an album is double clicked. The album page contains a list of all songs in the album and some basic information
 |      about the album
 |
 |      Inputs:
 |          - current_display_table (QTableWidget): The table currently being displayed from which the album was selected
 |          - associated_library_list (dict): The dictionary of albums in the music library associated with the current display table
 |
 |  artist_and_album_pages_setup(self)
 |      Connects all buttons on the album and artist to the functions they should execute when clicked. Also connects the tables on each page to
 |      the functions they should execute when an item in the table is double clicked and sets the default album cover placeholder image. Only runs
 |      during the initialization of a PlayerWindow object
 |
 |  artist_double_clicked(self)
 |      Displays the artist page for the selected artist when an artist is double clicked. The artist page contains a list of all albums by the artist
 |
 |  button_styling(self)
 |      Styles all buttons in the GUI to match the GUI theme. Also styles applicable buttons to indicate when the mouse hovers over them. Only runs
 |      during the initialization of a PlayerWindow object
 |
 |  create_playlist(self)
 |      Creates a playlist in the application's music library with the name specified by the user in the text input box on the playlist page
 |      Also adds the playlist to the necessary GUI tables
 |
 |  delete_playlist(self, playlist_clicked)
 |      Deletes the specified playlist from the application's music library and the GUI
 |
 |      Inputs:
 |          - playlist_clicked(Playlist): The playlist to be deleted
 |
 |  display_tables_setup(self)
 |      Sets up, populates, and runs the function to automatically resize all tables used to display information in the GUI. Also sets up the right click menus allowing
 |      the user to add a song to be played next or add a song to a playlist. Only runs during the initialization of a PlayerWindow object
 |
 |  initial_file_location(self)
 |      Determines the default library file location depending on the user's operating system and runs the function to add all applicable files in the default library location.
 |      Also adds the file location to the list of file locations displayed in the GUI and updates the list of playlists. Only runs during the initialization of a PlayerWindow object
 |
 |  initial_table_setup(self)
 |      Runs the functions required to load automatically load and display music and playlists from the user's library
 |
 |  library_page_setup(self)
 |      Connects all buttons on the library page to the functions they should execute when clicked. Also switches GUI to the 'Library' page
 |      and sets the proper content list to be shown based on the currently selected option of the Artist/Album/Tracks dropdown menu. Only runs
 |      during the initialization of a PlayerWindow object
 |
 |  main_window_setup(self)
 |      Creates the main window and removes all margins around the main window. Only runs during the initialization of a PlayerWindow object
 |
 |  meta_data_changed(self)
 |      Updates the currently playing song and artist information in the player when the metadata changes
 |
 |  play_next(self)
 |      Plays the next song in the loaded sequence of songs
 |
 |  play_pause(self)
 |      Plays the currently loaded song if it is paused and pauses the currently loaded song if it is playing. Also switches the icon of the play/pause button depending
 |      on the playing state
 |
 |  play_previous(self)
 |      Plays the previous song in the loaded sequence of songs
 |
 |  playing_media_frame_setup(self)
 |      Sets up the styles and connect functions of the media buttons and media slider that are shown in the player at the bottom of the GUI when media is playing. Also hides the player.
 |      Only runs during the initialization of a PlayerWindow object
 |
 |  playlist_double_clicked(self)
 |      Displays the playlist page for the selected playlist when a playlist is double clicked
 |
 |  playlist_list_context_menu(self)
 |      Displays a right click menu when a playlist is right-clicked in the playlist section of the GUI, allowing the user to remove delete the playlist
 |
 |  playlist_setup(self)
 |      Connects 'Create Playlist' button on the playlist page to the function it should execute when clicked and connects the playlist list to the function
 |      it should execute when a playlist is double clicked. Also sets up the right click menu alloing the user to delete a playlist. Only runs
 |      during the initialization of a PlayerWindow object
 |
 |  queue_song(self, song)
 |      Adds the selected song to be played immediately after the currently playing song
 |
 |  remove_from_playlist(self, playlist_clicked, selected_song)
 |      Calls the function necessary to remove the specified song from the the specified playlist in the application's music library. Also removes the song from the
 |      playlsit in the GUI.
 |
 |      Inputs:
 |          - playlist_clicked (string): The name of the playlist the song should removed from
 |          - selected_song (Song): The song to be removed from the playlist
 |
 |  seek_through_song(self, position)
 |      Seeks through the currently playing song to the specified positon
 |
 |      Inputs:
 |          - position (int): The position in the song to seek to, in milliseconds
 |
 |  settings_setup(self)
 |      Sets up the settings button with the requried icon and sizing. Also connects the settings button to the function it should execute when clicked. Connects
 |      the 'Add Location' button on the settings page the function it should execute when pressed. Only runs during the initialization of a PlayerWindow object
 |
 |  setup_table_resizing(self)
 |      Automatically resizes all display tables in the GUI
 |
 |  song_double_clicked(self, current_display_table, associated_library_list)
 |      Plays the selected song when a song is double clicked
 |
 |      Inputs:
 |          - current_display_table (QTableWidget): The table currently being displayed from which the song was selected
 |          - associated_library_list (dict): The dictionary of songs in the music library associated with the current display table
 |
 |  song_library_context_menu(self, selected_table, associated_library_list)
 |      Displays a right click menu when a song is right-clicked in the library section of the GUI, allowing the user to add the song to a playlist or play the song next
 |
 |      Inputs:
 |          - selected_table (QTableWidget): The currently displaying table from which the song was right clicked
 |          - associated_library_list (dict): The list of songs associated with the selected table
 |
 |  song_playlist_context_menu(self)
 |      Displays a right click menu when a song is right-clicked in the playlist section of the GUI, allowing the user to remove the song from the playlist
 |
 |  switch_content_view(self, selected_content_page)
 |      Switches the GUI page to the desired page
 |
 |      Inputs:
 |          - selected_content_page (string): The string containing the name of the page to switch to
 |
 |  switch_library_view(self)
 |      Switches the table on the library page to the correct table depending on the selected option of the Artists/Albums/Tracks dropdown
 |      menu
 |
 |  update_seekbar(self, position, senderType=False)
 |      Updates the seekbar with the current position in the currently playing song
 |
 |      Inputs:
 |          - position (int): The current position of the song in milliseconds
 |          - senderType (bool): Whether the update is being triggered by a change in the seekbar's value or not. Defaults to False
 |
 |  update_seekbar_range(self, duration)
 |      Updates the seekbar's range when the duration of the currently loaded song changes (this happens when the current song changes)
 |
 |      Inputs:
 |          - duration (int): The duration of the song in milliseconds

 #####################################################################################################################################################

class MusicLibrary()
 |  Attributes defined here:
 |
 |  self.list_of_songs = dict() # Dictionary of songs in the music library
 |  self.list_of_albums = dict() # Dictionary of albums in the music library
 |  self.list_of_artists = dict() # Dictionary of artists in the music library
 |  self.dict_of_playlists = dict() # Dictionary of playlists in the music library
 |  self.num_songs = len(self.list_of_songs) # Number of songs in the music library
 |  self.num_albums = len(self.list_of_albums) # Number of albums in the music library
 |  self.num_artists = len(self.list_of_artists) # Number of artists in the music library
 |  self.library_file_locations = [] # List of music library file location
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initializes all necessary attributes
 |
 |  add_album(self, song_with_album_info)
 |      Adds the album of the specified song to the list of albums in the library and adds the album's artist if the artist does not yet
 |      exist in the library. Also adds the specified song to the album's song list
 |
 |      Inputs:
 |          - song_with_album_info (Song): Song with the album info needed to add the new album
 |
 |  add_artist(self, album_with_artist_info)
 |      Adds the specified artist to the list of artists in the library and adds the specified album to the artist's album list
 |
 |      Inputs:
 |          - album_with_album_info (Album): Album with the artist info needed to add the new artist
 |
 |  add_library_file_location(self, location=None)
 |      Add the songs and playlists in the specified file location to the library
 |
 |      Inputs:
 |          - location (string): The file location to add to the music library. If no location is specified, defaults to None
 |
 |  add_playlist_song(self, playlist, song)
 |      Adds the specified song to the specified playlist
 |
 |      Inputs:
 |          - playlist (string): The name of the playlist the song should be added to
 |          - song (Song): The song to be added to the playlist
 |
 |  add_song(self, file_location)
 |      Adds the song at the specified file location to the list of songs in the library. Also adds the album and
 |      artist of the song if they do not yet exist in the library
 |
 |      Inputs:
 |          - fil_location (string): File location of the song being added
 |
 |  create_playlist(self, playlist_name, file_location=None)
 |      Creates a new playlist with the specified name from the playlist file located at the specified file location
 |
 |      Inputs:
 |          - playlist_name (string): The name of the new playlist
 |          - file_location (string): The location of the playlist file. If no file location is specified, defaults to None
 |
 |  delete_playlist(self, playlist_to_remove)
 |      Deletes the specified playlist
 |
 |      Inputs:
 |          - playlist_to_remove (Playlist): The playlist to remove
 |
 |  find_songs(self, location)
 |      Searches the specified directory and all its subdirectories for MP3 and M3U files.
 |      Adds the MP3 files to the list of songs in the library and creates playlists from the M3U files.
 |
 |      Inputs:
 |          - location (string): File path to search for songs and playlists
 |
 |  get_albums(self)
 |      Returns the list of albums in the library
 |
 |  get_artists(self)
 |      Returns the list of artists in the library
 |
 |  get_playlist(self, playlist)
 |      Returns the specified playlist object
 |
 |      Inputs:
 |          - playlist (string): Name of the playlist to be returned
 |
 |  get_playlists(self)
 |      Returns the dictionary of all the playlists in the music library
 |
 |  get_songs(self)
 |      Returns the list of songs in the library
 |
 |  remove_playlist_song(self, playlist, song)
 |      Removes the specified song from the specified playlist
 |
 |      Inputs:
 |          - playlist (Playlist): Playlist to remove song from
 |          - song (Song): Song to remove from playlist
 |
 |  sort_all_album_tracks(self)
 |      Sorts all tracks in all albums in the music library by track number
 |
 |  sort_all_albums(self)
 |      Sorts all albums in the music library by artist in alphabetical order
 |
 |  sort_all_artists(self)
 |      Sorts all artist in the music library by name in alphabetical order
 |
 |  sort_all_songs(self)
 |      Sorts all songs in the music library by title in alphabetical order
 |
 |  sort_object_list(self, list_to_sort, sort_attribute)
 |      Sorts the specifed list of objects by the specified object attribute using insertion sort
 |
 |      Inputs:
 |          - list_to_sort (list) or (dict): List of objects to sort
 |          - sort_attribute (string): Name of the object attribute to sort by

 #####################################################################################################################################################

 class Song(builtins.object)
 |  Attributes defined here:
 |
 |  self.audio_file = eyed3.load(file) # Song file loaded with eyed3
 |  self.song_title = self.audio_file.tag.title # Title of song
 |  self.song_artist = self.audio_file.tag.artist # Artist of song
 |  self.song_duration = self.audio_file.info.time_secs # Length of song in milliseconds
 |  self.song_duration_formatted = self.convert_duration_to_display_format() # Length of song formatted for display
 |  self.song_album = self.audio_file.tag.album # Song album appears on
 |  self.song_year = str(self.audio_file.tag.getBestDate()) # Year song was released
 |  self.song_genre = self.audio_file.tag.genre # Genre of song
 |  self.track_num = self.audio_file.tag.track_num[0] # Track number of song on the album it belongs to
 |  self.song_file = file # File location of the song
 |
 |  Methods defined here:
 |
 |  __init__(self, file)
 |      Initializes all necessary attributes. If the necessary metadata does not exist in the file, sets all attributes to 'Unknown'
 |
 |  convert_duration_to_display_format(self)
 |      Converts the song_duration attribute of the object to a string in the format `MM:SS` and returns the result
 |
 |  get_album(self)
 |      Returns the name of the album that the song belongs to
 |
 |  get_artist(self)
 |      Returns the name of the artist of the song
 |
 |  get_duration(self)
 |      Returns the duration of the song
 |
 |  get_duration_formatted(self)
 |      Returns the duration of the song
 |
 |  get_genre(self)
 |      Returns the genre of the song
 |
 |  get_title(self)
 |      Returns the title of the song
 |
 |  get_year(self)
 |      Returns the release year of the song
 |
 |  set_album(self, album_to_set)
 |      Sets the name of the album that the song belongs to the specifed album
 |
 |      Inputs:
 |          - album_to_set (string): Album to set for the song
 |
 |  set_artist(self, artist_to_set)
 |      Sets the name of the artist of the song to the specified artist name
 |
 |      Inputs:
 |          - artist_to_set (string): Artist to set for the song
 |
 |  set_duration(self, duration_to_set)
 |      Sets the duration of the song to the specified duration
 |
 |      Inputs:
 |          - duration_to_set (float): Duration to set for the song
 |
 |  set_genre(self, genre_to_set)
 |      Sets the genre of the song to the specifed genre
 |
 |      Inputs:
 |          - genre_to_set (string): Genre to set for the song
 |
 |  set_title(self, title_to_set)
 |      Sets the title of the song to the specified title
 |
 |      Inputs:
 |          - title_to_set (string): Title to set for the song
 |
 |  set_year(self, year_to_set)
 |      Sets the release year of the song to the specified year
 |
 |      Inputs:
 |          - year_to_set (string): Year to set for the song

#####################################################################################################################################################

class Album(builtins.object)
 |  Attributes defined here:
 |
 |  self.album_songs = dict() # Songs in the album
 |  self.album_name = album_name # Name of the album
 |  self.album_artist = album_artist # Artist of the album
 |  self.album_year = album_year # Year the album was made
 |  self.album_genre = album_genre # Genre of the album
 |  self.album_song_count = len(self.album_songs) # Number of songs in the album
 |
 |  Methods defined here:
 |
 |  __init__(self, album_name='', album_artist='', album_year='', album_genre='')
 |      Initializes all necessary attributes
 |
 |  add_song(self, song_to_add)
 |      Adds the specified song to the album
 |
 |      Inputs:
 |          - song_to_add (Song): Song to add to the album
 |
 |  get_artist(self)
 |      Returns the name of the album artist
 |
 |  get_genre(self)
 |      Returns the genre of the album
 |
 |  get_name(self)
 |      Returns the name of the album
 |
 |  get_song_count(self)
 |      Returns the number of songs in an album
 |
 |  get_songs(self)
 |      Returns the songs in an album
 |
 |  get_year(self)
 |      Returns the release year of the album
 |
 |  set_artist(self, artist_to_set)
 |      Sets the name of the album artist to the specfied artist name
 |
 |      Inputs:
 |          - artist_to_set (string): Artist to set for the album
 |
 |  set_genre(self, genre_to_set)
 |      Sets the genre of the album to the specified genre
 |
 |      Inputs:
 |          - genre_to_set (string): Genre to set for the album
 |
 |  set_name(self, name_to_set)
 |      Sets the name of the album to the specified name
 |
 |      Inputs:
 |          - name_to_set (string): Name to set for the album
 |
 |  set_year(self, year_to_set)
 |      Sets the release year of the album to the specified year
 |
 |      Inputs:
 |          - year_to_set (string): Year to set for the album

 #####################################################################################################################################################

 class Artist(builtins.object)
 |  Attributes defined here:
 |
 |  self.artist_name = artist_name # Name of artist
 |  self.artist_albums = dict() # Albums by the artist
 |  self.artist_album_count = len(self.artist_albums) # Numbers of albums in artist's collection
 |
 |  Methods defined here:
 |
 |  __init__(self, artist_name)
 |      Initializes all necessary attributes
 |
 |  add_album(self, album_to_add)
 |      Adds the specifed album to the artist's catalogue
 |
 |      Inputs:
 |          - album_to_add (Album): Album to add to the artist's collection
 |
 |  get_albums(self)
 |      Returns the name of the albums belonging to the artist
 |
 |  get_name(self)
 |      Returns the name of the artist
 |
 |  set_name(self, name_to_set)
 |      Sets the name of the artist to the specified name
 |
 |      Inputs:
 |          - name_to_set (string): Name to set for the artist

 #####################################################################################################################################################

 class Playlist()
 |  Attributes defined here:
 |
 |  self.playlist_name = playlist_name # Name of the playlist
 |  self.playlist_songs = playlist_songs # Songs in the playlist  
 |  self.playlist_file_location = playlist_file_location # File location of the playlist file associated with the playlist 
 |  self.num_songs = len(self.playlist_songs)
 |
 |  Methods defined here:
 |
 |  __init__(self, playlist_name, playlist_file_location=None, playlist_songs={})
 |      Initializes all necessary attributes
 |
 |  add_song(self, song_to_add)
 |      Adds the specified song to the playlist and to the playlist file
 |
 |      Inputs:
 |          - song_to_add (Song): Song to remove from the playlist
 |
 |  create_new_playlist_file(self)
 |      Creates a new empty playlist file with the specified name in the default music library folder
 |
 |  get_default_folder(self)
 |      Returns the default folder for the music library depending on the operating system
 |
 |  get_name(self)
 |      Returns the name of the playlist
 |
 |  get_songs(self)
 |      Returns all the songs in the playlist
 |
 |  remove_song(self, song_to_remove)
 |      Removes the specified song from the playlist and the playlist file
 |
 |      Inputs:
 |          - song_to_remove (Song): Song to remove from the playlist


INSTRUCTIONS FOR USE:

   Before using this project, several libraries must be downloaded. On Windows, this requires downloading packages via pip. If you are unsure if you have pip installed or you do not have it installed, you can follow this link for instructions on how to install pip: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/. Once you have installed pip, you'll need to go into the command prompt. The command prompt can be found by typing 'cmd' into the Start Menu search bar. In the command prompt, we'll have to install the PyQt5 module using 'pip install PyQt5', the pyqtdarktheme module using 'pip install pyqtdarktheme', and the eyed3 modeul using 'pip install eyeD3' and 'pip install python-magic-bin'. If for some reason these installations do not work, check the version of Python you are using using the command prompt command 'python --version'. PyQt5 is known to have some issues with Python 3.10, so this program was developed and tested in 3.9.13, the final regular maintenance release of Python 3.9. If you are having trouble installing any of the above packages, try rolling back to Python 3.9.
   To run this program, only 'gui.py' has to be run. To do this, you can open your favorite editor or the command prompt. In the terminal, navigate to the folder where the project is stored and run the program with 'python gui.py'. This will run the program and open the application. You can use the dropdown menu in the upper left to navigate between tracks, artists, and albums. You can navigate between your music library and playlists by clicking on the Library and Playlist buttons at the top of the screen. To add a file location to your library, you can click the settings button in the upper right corner to access settings, then click on 'Add Location' and select a folder with mp3 files. A folder called "Example MP3 Files" is included in this project directory to test the functionality if you do not have any MP3 files. To play a song, you can double click it, and all the media buttons of a normal music player will appear at the bottom of the screen. When viewing all artists, double clicking on an artist will bring you to the artist page with a list of the albums by that artist. You can then double click on an album to select it and play songs with another double click. When viewing all albums, you can select an album by double clicking it and then doubling clicking the song to play. The next song in the sequence you have selected (album, playlist, etc.) will automatically play when the current song is finished.

SUGGESTED FUTURE DIRECTIONS:

   One of the next things I would suggest working on for those interested is the ability to shuffle-play playlists. This is a very common part of music players that was not implemented in this application. Allowing users to shuffle a playlist would bring more convenienve to users and elevate the functionality of the program to the next level. Another feature I would suggest working on is suggested playlists. Suggested playlists would be playlists automatically generated by the application based on the user's musical interests, mainly based around genre interests. The user would be able to select their interests in the settings menu, and the application would then automatically create playlists with the songs in the user's library that follow the user's musical interests. Unfortunately, this feature was planned, but was not able to be implemented due to time constraints and complexity of the feature.
