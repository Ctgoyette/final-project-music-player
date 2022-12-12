from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from base_gui import Ui_MainWindow
from music_library import MusicLibrary
import sys
import os
import qdarktheme

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        '''
        Initializes all required attributes and runs all function needed to properly setup the GUI
        '''
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setPalette(qdarktheme.load_palette())
        self.main_window_setup()
        self.music_library = MusicLibrary()
        self.player = QMediaPlayer()
        self.current_playing_list = QMediaPlaylist()
        self.library_page_setup()
        self.artist_and_album_pages_setup()
        self.settings_setup()
        self.playing_media_frame_setup()
        self.playlist_setup()
        self.button_styling()
        self.last_content_page_index_album = 0
        self.last_content_page_index_artist = 0
        self.selected_artist = None
        self.selected_album = None
        self.selected_playlist = None

    def library_page_setup(self):
        '''
        Connects all buttons on the library page to the functions they should execute when clicked. Also switches GUI to the 'Library' page
        and sets the proper content list to be shown based on the currently selected option of the Artist/Album/Tracks dropdown menu. Only runs 
        during the initialization of a PlayerWindow object
        '''
        self.library_dropdown_artist_index = self.library_view_dropdown.findText('Artists')
        self.library_dropdown_album_index = self.library_view_dropdown.findText('Albums')
        self.library_dropdown_song_index = self.library_view_dropdown.findText('Tracks')
        self.library_view_dropdown.currentIndexChanged.connect(self.switch_library_view)
        self.album_list.itemDoubleClicked.connect(partial(self.album_double_clicked, self.album_list, self.music_library.albums))
        self.artist_list.itemDoubleClicked.connect(self.artist_double_clicked)
        self.song_list.itemDoubleClicked.connect(partial(self.song_double_clicked, self.song_list, self.music_library.songs))
        self.button_library_view.clicked.connect(partial(self.switch_content_view, 'Library'))
        self.button_playlist_view.clicked.connect(partial(self.switch_content_view, 'Playlists'))
        self.switch_library_view()
        self.switch_content_view('Library')
    
    def artist_and_album_pages_setup(self):
        '''
        Connects all buttons on the album and artist to the functions they should execute when clicked. Also connects the tables on each page to
        the functions they should execute when an item in the table is double clicked and sets the default album cover placeholder image. Only runs 
        during the initialization of a PlayerWindow object
        '''
        self.album_page_back_button.clicked.connect(partial(self.switch_content_view, 'Album_Previous'))
        self.artist_page_back_button.clicked.connect(partial(self.switch_content_view, 'Artist_Previous'))
        self.artist_page_album_list.itemDoubleClicked.connect(lambda: self.album_double_clicked(self.artist_page_album_list, self.selected_artist.albums))
        self.album_page_song_list.itemDoubleClicked.connect(lambda: self.song_double_clicked(self.album_page_song_list, self.selected_album.songs))
        self.album_cover_display.setPixmap(QtGui.QPixmap(r'images\album-cover-placeholder.jpg').scaled(300, 300, QtCore.Qt.KeepAspectRatioByExpanding))

    def button_styling(self):
        '''
        Styles all buttons in the GUI to match the GUI theme. Also styles applicable buttons to indicate when the mouse hovers over them. Only runs 
        during the initialization of a PlayerWindow object
        '''
        button_styling = "QPushButton {color : rgb(230, 230, 230); border-style : solid; border-color : white; border-width : 1px;} QPushButton:hover {color: white; font-weight : bold;}"
        self.library_view_dropdown.setStyleSheet("QComboBox {background-color : rgb(32, 33, 36); color: rgb(230, 230, 230);} QComboBox:hover {color: white; font-weight : bold;}")
        self.button_library_view.setStyleSheet(button_styling)
        self.button_playlist_view.setStyleSheet(button_styling)
        self.album_page_back_button.setStyleSheet(button_styling)
        self.artist_page_back_button.setStyleSheet(button_styling)
        self.button_add_location.setStyleSheet(button_styling)
        self.button_create_playlist.setStyleSheet(button_styling)

    def initial_table_setup(self):
        '''
        Runs the functions required to load automatically load and display music and playlists from the user's library
        '''
        self.initial_file_location()
        self.display_tables_setup()

    def main_window_setup(self):
        '''
        Creates the main window and removes all margins around the main window. Only runs during the initialization of a PlayerWindow object
        '''
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.verticalLayout_6.setContentsMargins(0,11,0,0)
        self.MainWindow.setWindowTitle('Music Player')

    def settings_setup(self):
        '''
        Sets up the settings button with the requried icon and sizing. Also connects the settings button to the function it should execute when clicked. Connects
        the 'Add Location' button on the settings page the function it should execute when pressed. Only runs during the initialization of a PlayerWindow object
        '''
        settings_icon = QtGui.QIcon(r'images\settings_icon.png')
        self.settings_button.setIcon(settings_icon)
        self.settings_button.setIconSize(QtCore.QSize(35, 35))
        self.settings_button.clicked.connect(partial(self.switch_content_view, 'Settings'))
        self.button_add_location.clicked.connect(self.add_library_location)
    
    def display_tables_setup(self):
        '''
        Sets up, populates, and runs the function to automatically resize all tables used to display information in the GUI. Also sets up the right click menus allowing 
        the user to add a song to be played next or add a song to a playlist. Only runs during the initialization of a PlayerWindow object
        '''
        self.add_table_items(self.music_library.songs.values(), self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
        self.add_table_items(self.music_library.albums.values(), self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
        self.add_table_items(self.music_library.artists.values(), self.artist_list, ['Artist'], ['name'])
        self.tables = {
            'song_list': self.song_list,
            'artist_list': self.artist_list,
            'album_list': self.album_list,
            'playlist_list': self.playlist_list,
            'album_page_song_list': self.album_page_song_list,
            'artist_page_album_list': self.artist_page_album_list,
            'playlist_page_song_list': self.playlist_page_song_list
        }
        self.setup_table_resizing()
        self.song_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.song_list.customContextMenuRequested.connect(partial(self.song_library_context_menu, self.song_list, self.music_library.songs))
        self.album_page_song_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.album_page_song_list.customContextMenuRequested.connect(lambda: self.song_library_context_menu(self.album_page_song_list, self.selected_album.songs))

    def playing_media_frame_setup(self):
        '''
        Sets up the styles and connect functions of the media buttons and media slider that are shown in the player at the bottom of the GUI when media is playing. Also hides the player. 
        Only runs during the initialization of a PlayerWindow object
        '''
        media_button_style = "QToolButton {color : rgb(225, 225, 225); background-color : rgb(40, 40, 40); border-style : solid; border-color: white;} QToolButton:hover {color : white;}"
        play_icon = QtGui.QIcon(r'images\play_button.png')
        self.play_button.setIcon(play_icon)
        self.play_button.setIconSize(QtCore.QSize(50, 50))
        self.play_button.setStyleSheet(media_button_style)
        self.play_button.clicked.connect(self.play_pause)
        self.button_next_song.clicked.connect(self.play_next)
        self.button_next_song.setStyleSheet(media_button_style)
        self.button_previous_song.clicked.connect(self.play_previous)
        self.button_previous_song.setStyleSheet(media_button_style)
        self.player.positionChanged.connect(self.update_seekbar)
        self.player.durationChanged.connect(self.update_seekbar_range)
        self.seek_bar.sliderMoved.connect(self.seek_through_song)
        self.player.metaDataChanged.connect(self.meta_data_changed)
        self.frame_playing_media.setStyleSheet('background-color : rgb(40, 40, 40);')
        self.frame_playing_media.hide()
    
    def playlist_setup(self):
        '''
        Connects 'Create Playlist' button on the playlist page to the function it should execute when clicked and connects the playlist list to the function
        it should execute when a playlist is double clicked. Also sets up the right click menu alloing the user to delete a playlist. Only runs 
        during the initialization of a PlayerWindow object
        '''
        self.button_create_playlist.clicked.connect(self.create_playlist)
        self.input_playlist_name.returnPressed.connect(self.create_playlist)
        self.playlist_list.itemDoubleClicked.connect(self.playlist_double_clicked)
        self.playlist_page_song_list.itemDoubleClicked.connect(lambda: self.song_double_clicked(self.playlist_page_song_list, self.selected_playlist.songs))
        self.playlist_page_song_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.playlist_page_song_list.customContextMenuRequested.connect(self.song_playlist_context_menu)
        self.playlist_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.playlist_list.customContextMenuRequested.connect(self.playlist_list_context_menu)

    def initial_file_location(self):
        '''
        Determines the default library file location depending on the user's operating system and runs the function to add all applicable files in the default library location.
        Also adds the file location to the list of file locations displayed in the GUI and updates the list of playlists. Only runs during the initialization of a PlayerWindow object
        '''
        if sys.platform == "linux" or sys.platform == "linux2":
            pass
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            music_folder = os.path.expanduser("~\Music")
        else:
            pass
        self.music_library.add_library_file_location(music_folder)
        self.file_locations_list.addItem(music_folder)
        self.add_table_items(self.music_library.playlists.values(), self.playlist_list, ['Playlist'], ['name'])
            
    def setup_table_resizing(self):
        '''
        Automatically resizes all display tables in the GUI
        '''
        for table_name, table in self.tables.items():
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def add_table_row(self, table):
        '''
        Adds a row to the specific table in the GUI

        Inputs:
            - table (QTableWidget): The table to add the row to
        '''
        row_count = table.rowCount()
        table.insertRow(row_count)

    def add_table_items(self, items_to_add, table, table_headings, attributes_to_add):
        '''
        Adds the specified attributes of the specified items to the given table with the given table headings

        Inputs:
            - items_to_add (list): The list of items to add to the table
            - table (QTableWidget): The table to add the items to
            - table_headings (list): The list of column headings for the table
            - attributes_to_add (list): The list of attributes of the items to add as table cells
        '''
        while table.rowCount() > 1:
                    table.removeRow(1)
        column_count = table.columnCount()
        for column in range(0, column_count):
            header = QtWidgets.QTableWidgetItem(table_headings[column])
            font = header.font()
            font.setBold(True)
            header.setFont(font)
            table.setItem(0, column, header)
        row = 1
        for item in items_to_add:
            self.add_table_row(table)
            for column in range(0, column_count):
                table.setItem(row, column, QtWidgets.QTableWidgetItem(getattr(item, attributes_to_add[column])))
            row += 1
        table.resizeColumnsToContents()

    def switch_library_view(self):
        '''
        Switches the table on the library page to the correct table depending on the selected option of the Artists/Albums/Tracks dropdown
        menu
        '''
        index = self.library_view_dropdown.currentIndex()
        if index == self.library_dropdown_artist_index:
            self.library_view_stack.setCurrentIndex(0)
        elif index == self.library_dropdown_album_index:
            self.library_view_stack.setCurrentIndex(1)
        elif index == self.library_dropdown_song_index:
            self.library_view_stack.setCurrentIndex(2)
        else:
            pass
    
    def switch_content_view(self, selected_content_page):
        '''
        Switches the GUI page to the desired page

        Inputs:
            - selected_content_page (string): The string containing the name of the page to switch to
        '''
        if selected_content_page == 'Library':
            self.content_type_view_stack.setCurrentIndex(0)
        elif selected_content_page == 'Playlists':
            self.content_type_view_stack.setCurrentIndex(1)
        elif selected_content_page == 'Album':
            self.last_content_page_index_album = self.content_type_view_stack.currentIndex()
            self.content_type_view_stack.setCurrentIndex(2)
        elif selected_content_page == 'Artist':
            self.last_content_page_index_artist = self.content_type_view_stack.currentIndex()
            self.content_type_view_stack.setCurrentIndex(3)
        elif selected_content_page == 'Settings':
            self.content_type_view_stack.setCurrentIndex(4)
        elif selected_content_page == 'Playlist':
            self.content_type_view_stack.setCurrentIndex(5)
        elif selected_content_page == 'Album_Previous':
            self.content_type_view_stack.setCurrentIndex(self.last_content_page_index_album)
        elif selected_content_page == 'Artist_Previous':
            self.content_type_view_stack.setCurrentIndex(self.last_content_page_index_artist)
        else:
            pass
    
    def album_double_clicked(self, current_display_table, associated_library_list):
        '''
        Displays the album page for the selected album when an album is double clicked. The album page contains a list of all songs in the album and some basic information
        about the album

        Inputs:
            - current_display_table (QTableWidget): The table currently being displayed from which the album was selected
            - associated_library_list (dict): The dictionary of albums in the music library associated with the current display table
        '''
        row_index = current_display_table.currentRow()
        column_index = current_display_table.currentColumn()
        if row_index != 0:
            selected_album = current_display_table.item(row_index, column_index).text()
            self.selected_album = associated_library_list[selected_album]
            if column_index == 0:
                self.album_page_album.setText(self.selected_album.name)
                self.album_page_artist.setText(self.selected_album.artist)
                self.album_page_year.setText(self.selected_album.year)
                self.add_table_items(self.selected_album.songs.values(), self.album_page_song_list, ['Title', 'Duration'], ['title', 'duration_formatted'])
                self.switch_content_view('Album')
            elif column_index == 1:
                pass
            else:
                pass
    
    def artist_double_clicked(self):
        '''
        Displays the artist page for the selected artist when an artist is double clicked. The artist page contains a list of all albums by the artist
        '''
        row_index = self.artist_list.currentRow()
        column_index = self.artist_list.currentColumn()
        if row_index != 0:
            selected_artist = self.artist_list.item(row_index, column_index).text()
            self.selected_artist = self.music_library.artists[selected_artist]
            if column_index == 0:
                self.artist_page_artist.setText(self.selected_artist.name)
                self.add_table_items(self.selected_artist.albums.values(), self.artist_page_album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
                self.switch_content_view('Artist')
            elif column_index == 1:
                pass
            else:
                pass
    
    def song_double_clicked(self, current_display_table, associated_library_list):
        '''
        Plays the selected song when a song is double clicked
        
        Inputs:
            - current_display_table (QTableWidget): The table currently being displayed from which the song was selected
            - associated_library_list (dict): The dictionary of songs in the music library associated with the current display table
        '''
        row_index = current_display_table.currentRow()
        column_index = current_display_table.currentColumn()
        if row_index != 0:
            if column_index == 0:
                self.current_playing_list.clear()
                for song in associated_library_list.values():
                    self.current_playing_list.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile(song.song_file)))
                self.player.setPlaylist(self.current_playing_list)
                self.frame_playing_media.show()
                self.current_playing_list.setCurrentIndex(row_index - 1)
                self.play_pause()
            else:
                pass
        else:
            pass
    
    def add_library_location(self):
        '''
        Opens the user's file manager allowing the user to select a folder to add to their music library. Once selected, adds the songs and playlists from specified file location
        to the display tables in the GUI
        '''
        selected_folder = QtWidgets.QFileDialog.getExistingDirectory()
        if selected_folder:
            self.music_library.add_library_file_location(selected_folder)
            self.file_locations_list.addItem(selected_folder)
            self.add_table_items(self.music_library.songs.values(), self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
            self.add_table_items(self.music_library.albums.values(), self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
            self.add_table_items(self.music_library.artists.values(), self.artist_list, ['Artist'], ['name'])
        else:
            pass

    def play_pause(self):
        '''
        Plays the currently loaded song if it is paused and pauses the currently loaded song if it is playing. Also switches the icon of the play/pause button depending
        on the playing state
        '''
        play_icon = QtGui.QIcon(r'images\play_button.png')
        pause_icon = QtGui.QIcon(r'images\pause_button.png')
        if self.player.state() != QMediaPlayer.PlayingState:
            self.player.play()
            self.play_button.setIcon(pause_icon)
        else:
            self.player.pause()
            self.play_button.setIcon(play_icon)
    
    def play_next(self):
        '''
        Plays the next song in the loaded sequence of songs
        '''
        self.current_playing_list.next()
    
    def play_previous(self):
        '''
        Plays the previous song in the loaded sequence of songs
        '''
        self.current_playing_list.previous()

    def update_seekbar(self, position, senderType = False):
        '''
        Updates the seekbar with the current position in the currently playing song
        
        Inputs:
            - position (int): The current position of the song in milliseconds
            - senderType (bool): Whether the update is being triggered by a change in the seekbar's value or not. Defaults to False
        '''
        if senderType == False:
            self.seek_bar.setValue(position)
            self.seek_bar_position.setText(f'{int(position/60000):02}:{int(position/1000%60):02}')
        
    def update_seekbar_range(self, duration):
        '''
        Updates the seekbar's range when the duration of the currently loaded song changes (this happens when the current song changes)

        Inputs:
            - duration (int): The duration of the song in milliseconds
        '''
        self.seek_bar.setMaximum(duration)
        self.seek_bar_duration.setText(f'{int(duration/60000):02}:{int(duration/1000%60):02}')

    def seek_through_song(self, position):
        '''
        Seeks through the currently playing song to the specified positon

        Inputs:
            - position (int): The position in the song to seek to, in milliseconds
        '''
        sender = self.seek_bar.sender()
        if isinstance(sender, QtWidgets.QSlider):
            self.player.setPosition(position)
    
    def meta_data_changed(self):
        '''
        Updates the currently playing song and artist information in the player when the metadata changes
        '''
        song_title = self.player.metaData(QMediaMetaData.Title)
        if self.player.metaData(QMediaMetaData.ContributingArtist):
            album_artist = self.player.metaData(QMediaMetaData.ContributingArtist)[0]
        else:
            album_artist = self.player.metaData(QMediaMetaData.AlbumArtist)
        self.playing_song.setText(song_title)
        self.playing_song.adjustSize()
        self.playing_artist.setText(album_artist)
    
    def create_playlist(self):
        '''
        Creates a playlist in the application's music library with the name specified by the user in the text input box on the playlist page
        Also adds the playlist to the necessary GUI tables
        '''
        playlist_name = self.input_playlist_name.text()
        if playlist_name.replace(' ', '') != '':
            self.music_library.create_playlist(playlist_name)
            self.add_table_items(self.music_library.playlists.values(), self.playlist_list, ['Playlist'], ['name'])
        self.input_playlist_name.clear()

    def song_library_context_menu(self, selected_table, associated_library_list):
        '''
        Displays a right click menu when a song is right-clicked in the library section of the GUI, allowing the user to add the song to a playlist or play the song next

        Inputs:
            - selected_table (QTableWidget): The currently displaying table from which the song was right clicked
            - associated_library_list (dict): The list of songs associated with the selected table
        '''
        row_index = selected_table.currentRow()
        column_index = selected_table.currentColumn()
        if row_index != 0:
            if column_index == 0:
                song_context_menu = QtWidgets.QMenu(selected_table)
                sub_menu = QtWidgets.QMenu('Add to Playlist', song_context_menu)
                for key in self.music_library.playlists.keys():
                    sub_menu.addAction(key)
                song_context_menu.addMenu(sub_menu)
                song_context_menu.addAction('Add to Queue')
                song_context_menu.exec
                try:
                    option_pressed = song_context_menu.exec_(QtGui.QCursor.pos()).text()
                    selected_song = selected_table.item(row_index, column_index).text()
                    if option_pressed == 'Add to Queue':
                        self.queue_song(associated_library_list[selected_song])
                    elif self.music_library.get_playlist(option_pressed):
                        self.add_to_playlist(option_pressed, associated_library_list[selected_song])
                    else:
                        pass
                except:
                    pass
            else:
                pass
        else:
            pass
    
    def add_to_playlist(self, playlist_clicked, selected_song):
        '''
        Calls the function necessary to add the specified song to the specified playlist in the application's music library

        Inputs:
            - playlist_clicked (string): The name of the playlist the song should be added to
            - selected_song (Song): The song to be added to the playlist
        '''
        self.music_library.add_playlist_song(playlist_clicked, selected_song)

    def remove_from_playlist(self, playlist_clicked, selected_song):
        '''
        Calls the function necessary to remove the specified song from the the specified playlist in the application's music library. Also removes the song from the
        playlsit in the GUI.

        Inputs:
            - playlist_clicked (string): The name of the playlist the song should removed from
            - selected_song (Song): The song to be removed from the playlist
        '''
        self.music_library.remove_playlist_song(playlist_clicked, selected_song)
        self.add_table_items(self.selected_playlist.songs.values(), self.playlist_page_song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])

    def delete_playlist(self, playlist_clicked):
        '''
        Deletes the specified playlist from the application's music library and the GUI

        Inputs:
            - playlist_clicked(Playlist): The playlist to be deleted
        '''
        self.music_library.delete_playlist(playlist_clicked)
        self.add_table_items(self.music_library.playlists.values(), self.playlist_list, ['Playlist'], ['name'])

    def playlist_double_clicked(self):
        '''
        Displays the playlist page for the selected playlist when a playlist is double clicked
        '''
        row_index = self.playlist_list.currentRow()
        column_index = self.playlist_list.currentColumn()
        if row_index != 0:
            selected_playlist = self.playlist_list.item(row_index, column_index).text()
            self.selected_playlist = self.music_library.playlists[selected_playlist]
            if column_index == 0:
                self.playlist_page_playlist.setText(self.selected_playlist.name)
                self.add_table_items(self.selected_playlist.songs.values(), self.playlist_page_song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
                self.switch_content_view('Playlist')
            elif column_index == 1:
                pass
            else:
                pass

    def song_playlist_context_menu(self):
        '''
        Displays a right click menu when a song is right-clicked in the playlist section of the GUI, allowing the user to remove the song from the playlist
        '''
        row_index = self.playlist_page_song_list.currentRow()
        column_index = self.playlist_page_song_list.currentColumn()
        if row_index != 0:
            if column_index == 0:
                song_context_menu = QtWidgets.QMenu(self.playlist_page_song_list)
                song_context_menu.addAction('Remove From Playlist')
                song_context_menu.addAction('Add to Queue')
                song_context_menu.exec
                try:
                    option_pressed = song_context_menu.exec_(QtGui.QCursor.pos()).text()
                    selected_song = self.playlist_page_song_list.item(row_index, column_index).text()
                    if option_pressed == 'Remove From Playlist':
                        self.remove_from_playlist(self.selected_playlist, self.selected_playlist.songs[selected_song])
                    elif option_pressed == 'Add to Queue':
                        self.queue_song(self.selected_playlist.songs[selected_song])
                    else:
                        pass
                except:
                    pass
            else:
                pass
        else:
            pass
    
    def playlist_list_context_menu(self):
        '''
        Displays a right click menu when a playlist is right-clicked in the playlist section of the GUI, allowing the user to remove delete the playlist
        '''
        row_index = self.playlist_list.currentRow()
        column_index = self.playlist_list.currentColumn()
        if row_index != 0:
            if column_index == 0:
                song_context_menu = QtWidgets.QMenu(self.playlist_list)
                song_context_menu.addAction('Delete Playlist')
                song_context_menu.exec
                try:
                    option_pressed = song_context_menu.exec_(QtGui.QCursor.pos()).text()
                    selected_playlist = self.playlist_list.item(row_index, column_index).text()
                    if option_pressed == 'Delete Playlist':
                        self.delete_playlist(self.music_library.playlists[selected_playlist])
                except:
                    pass
            else:
                pass
        else:
            pass

    def queue_song(self, song):
        '''
        Adds the selected song to be played immediately after the currently playing song
        '''
        index_to_insert = self.current_playing_list.currentIndex() + 1
        self.current_playing_list.insertMedia(index_to_insert, QMediaContent(QtCore.QUrl.fromLocalFile(song.song_file)))

        


#########################################################
#Actually display stuff
#########################################################

ui = PlayerWindow()
# Shows the application window and automatically maximizes it
ui.MainWindow.showMaximized()

# Allows window to open before automatcally loading all songs and playlists in library (Windows) in case the library is very large
ui.initial_table_setup()
sys.exit(ui.app.exec_())