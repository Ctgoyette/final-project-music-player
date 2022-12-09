from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from base_gui import Ui_MainWindow
from music_library import MusicLibrary, Song
import sys
import os
import qdarktheme

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.music_library = MusicLibrary()
        self.library_dropdown_artist_index = self.library_view_dropdown.findText('Artists')
        self.library_dropdown_album_index = self.library_view_dropdown.findText('Albums')
        self.library_dropdown_song_index = self.library_view_dropdown.findText('Tracks')
        self.library_view_dropdown.currentIndexChanged.connect(self.switch_library_view)
        self.album_list.itemDoubleClicked.connect(partial(self.album_double_clicked, self.album_list, self.music_library.albums))
        self.artist_list.itemDoubleClicked.connect(self.artist_double_clicked)
        self.song_list.itemDoubleClicked.connect(partial(self.song_double_clicked, self.song_list, self.music_library.songs))
        self.switch_library_view()
        self.button_library_view.clicked.connect(partial(self.switch_content_view, 'Library'))
        self.button_playlist_view.clicked.connect(partial(self.switch_content_view, 'Playlists'))
        self.last_content_page_index_album = 0
        self.last_content_page_index_artist = 0
        self.album_page_back_button.clicked.connect(partial(self.switch_content_view, 'Album_Previous'))
        self.artist_page_back_button.clicked.connect(partial(self.switch_content_view, 'Artist_Previous'))
        self.selected_artist = None
        self.selected_album = None
        self.current_playing_list = QMediaPlaylist()
        self.artist_page_album_list.itemDoubleClicked.connect(lambda: self.album_double_clicked(self.artist_page_album_list, self.selected_artist.albums))
        self.album_page_song_list.itemDoubleClicked.connect(lambda: self.song_double_clicked(self.album_page_song_list, self.selected_album.songs))
        self.switch_content_view('Library')
        self.music_library.add_library_file_location()
        self.album_cover_display.setPixmap(QtGui.QPixmap(r'images\album-cover-placeholder.jpg').scaled(300, 300, QtCore.Qt.KeepAspectRatioByExpanding))
        self.display_tables_setup()
        self.settings_button_setup()
        self.add_location_button_setup()
        self.player = QMediaPlayer()
        self.media_buttons_setup()

    def settings_button_setup(self):
        settings_icon = QtGui.QIcon(r'images\settings_icon.png')
        self.settings_button.setIcon(settings_icon)
        self.settings_button.setIconSize(QtCore.QSize(35, 35))
        self.settings_button.setStyleSheet("QPushButton {background-color : rgb(240, 240, 240); border : none;} QPushButton:hover {background-color : rgb(250, 250, 250);}")
        self.settings_button.clicked.connect(partial(self.switch_content_view, 'Settings'))
    
    def display_tables_setup(self):
        self.add_table_items(self.music_library.songs, self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
        self.add_table_items(self.music_library.albums, self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
        self.add_table_items(self.music_library.artists, self.artist_list, ['Artist'], ['name'])
        self.tables = {
            'song_list': self.song_list,
            'artist_list': self.artist_list,
            'album_list': self.album_list,
            'playlist_list': self.playlist_list,
            'album_page_song_list': self.album_page_song_list,
            'artist_page_album_list': self.artist_page_album_list
        }
        self.setup_table_resizing()

    def add_location_button_setup(self):
        self.button_add_location.clicked.connect(self.add_library_location)

    def media_buttons_setup(self):
        play_icon = QtGui.QIcon(r'images\play_button.png')
        self.play_button.setIcon(play_icon)
        self.play_button.setIconSize(QtCore.QSize(50, 50))
        self.play_button.setStyleSheet("QPushButton {background-color : rgb(240, 240, 240); border : none;}")
        self.play_button.clicked.connect(self.play_pause)
        self.button_next_song.clicked.connect(self.play_next)
        self.button_next_song.setStyleSheet("QToolButton {background-color : rgb(240, 240, 240); border : none;} QToolButton:hover {color : white;}")
        self.button_previous_song.clicked.connect(self.play_last)
        self.button_previous_song.setStyleSheet("QToolButton {background-color : rgb(240, 240, 240); border : none;} QToolButton:hover {color : white;}")
        self.play_button.hide()
        self.button_next_song.hide()
        self.button_previous_song.hide()

    def setup_table_resizing(self):
        for table_name, table in self.tables.items():
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def add_table_row(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

    def add_table_items(self, items_to_add, table, table_headings, attributes_to_add):
        while table.rowCount() > 1:
                    table.removeRow(1)
        column_count = table.columnCount()
        for column in range(0, column_count):
            table.setItem(0, column, QtWidgets.QTableWidgetItem(table_headings[column]))
        row = 1
        for item in items_to_add:
            self.add_table_row(table)
            for column in range(0, column_count):
                table.setItem(row, column, QtWidgets.QTableWidgetItem(getattr(item, attributes_to_add[column])))
            row += 1
        table.resizeColumnsToContents()

    def switch_library_view(self):
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
        elif selected_content_page == 'Album_Previous':
            self.content_type_view_stack.setCurrentIndex(self.last_content_page_index_album)
        elif selected_content_page == 'Artist_Previous':
            self.content_type_view_stack.setCurrentIndex(self.last_content_page_index_artist)
        else:
            pass
    
    def album_double_clicked(self, current_display_table, associated_library_list):
        row_index = current_display_table.currentRow()
        column_index = current_display_table.currentColumn()
        if row_index != 0:
            self.selected_album = associated_library_list[row_index - 1]
            if column_index == 0:
                self.album_page_album.setText(self.selected_album.name)
                self.album_page_artist.setText(self.selected_album.artist)
                self.album_page_year.setText(self.selected_album.year)
                self.add_table_items(self.selected_album.songs, self.album_page_song_list, ['Title', 'Duration'], ['title', 'duration_formatted'])
                self.switch_content_view('Album')
            elif column_index == 1:
                pass
            else:
                pass
    
    def artist_double_clicked(self):
        row_index = self.artist_list.currentRow()
        column_index = self.artist_list.currentColumn()
        if row_index != 0:
            self.selected_artist = self.music_library.artists[row_index - 1]
            if column_index == 0:
                self.artist_page_artist.setText(self.selected_artist.name)
                self.add_table_items(self.selected_artist.albums, self.artist_page_album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
                self.switch_content_view('Artist')
            elif column_index == 1:
                pass
            else:
                pass
    
    def song_double_clicked(self, current_display_table, associated_library_list):
        row_index = current_display_table.currentRow()
        column_index = current_display_table.currentColumn()
        if column_index == 0:
            self.current_playing_list.clear()
            for song in associated_library_list:
                self.current_playing_list.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile(song.song_file)))
            self.player.setPlaylist(self.current_playing_list)
            if row_index != 0:
                self.play_button.show()
                self.button_next_song.show()
                self.button_previous_song.show()
                self.current_playing_list.setCurrentIndex(row_index - 1)
                self.play_pause()
            else:
                pass
        else:
            pass
    
    def add_library_location(self):
        selected_folder = QtWidgets.QFileDialog.getExistingDirectory()
        if selected_folder:     
            self.music_library.add_library_file_location(selected_folder)
            self.file_locations_list.addItem(selected_folder)
            self.add_table_items(self.music_library.songs, self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
            self.add_table_items(self.music_library.albums, self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
            self.add_table_items(self.music_library.artists, self.artist_list, ['Artist'], ['name'])
        else:
            pass

    def play_pause(self):
        play_icon = QtGui.QIcon(r'images\play_button.png')
        pause_icon = QtGui.QIcon(r'images\pause_button.png')
        if self.player.state() != QMediaPlayer.PlayingState:
            self.player.play()
            self.play_button.setIcon(pause_icon)
        else:
            self.player.pause()
            self.play_button.setIcon(play_icon)
    
    def play_next(self):
        self.current_playing_list.next()
    
    def play_last(self):
        self.current_playing_list.previous()
        


#########################################################
#Actually display stuff
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
# app.setStyleSheet(qdarktheme.load_stylesheet())
ui.MainWindow.show()
sys.exit(app.exec_())

