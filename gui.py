from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from base_gui import Ui_MainWindow
from music_library import MusicLibrary
import eyed3
import sys
import os
import qdarktheme

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setPalette(qdarktheme.load_palette())
        self.main_window_setup()
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
        self.selected_playlist = None
        self.current_playing_list = QMediaPlaylist()
        self.artist_page_album_list.itemDoubleClicked.connect(lambda: self.album_double_clicked(self.artist_page_album_list, self.selected_artist.albums))
        self.album_page_song_list.itemDoubleClicked.connect(lambda: self.song_double_clicked(self.album_page_song_list, self.selected_album.songs))
        self.switch_content_view('Library')
        self.album_cover_display.setPixmap(QtGui.QPixmap(r'images\album-cover-placeholder.jpg').scaled(300, 300, QtCore.Qt.KeepAspectRatioByExpanding))
        self.settings_button_setup()
        self.add_location_button_setup()
        self.player = QMediaPlayer()
        self.playing_media_frame_setup()
        self.playlist_setup()
        self.button_styling()

    def button_styling(self):
        button_styling = "QPushButton {color : rgb(230, 230, 230); border-style : solid; border-color : white; border-width : 1px;} QPushButton:hover {color: white; font-weight : bold;}"
        self.library_view_dropdown.setStyleSheet("QComboBox {background-color : rgb(32, 33, 36); color: rgb(230, 230, 230);} QComboBox:hover {color: white; font-weight : bold;}")
        self.button_library_view.setStyleSheet(button_styling)
        self.button_playlist_view.setStyleSheet(button_styling)
        self.album_page_back_button.setStyleSheet(button_styling)
        self.artist_page_back_button.setStyleSheet(button_styling)
        self.button_add_location.setStyleSheet(button_styling)

    def initial_table_setup(self):
        self.initial_file_location()
        self.display_tables_setup()

    def main_window_setup(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.verticalLayout_6.setContentsMargins(0,11,0,0)

    def settings_button_setup(self):
        settings_icon = QtGui.QIcon(r'images\settings_icon.png')
        self.settings_button.setIcon(settings_icon)
        self.settings_button.setIconSize(QtCore.QSize(35, 35))
        self.settings_button.clicked.connect(partial(self.switch_content_view, 'Settings'))
    
    def display_tables_setup(self):
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

    def add_location_button_setup(self):
        self.button_add_location.clicked.connect(self.add_library_location)

    def playing_media_frame_setup(self):
        media_button_style = "QToolButton {color : rgb(225, 225, 225); background-color : rgb(40, 40, 40); border-style : solid; border-color: white;} QToolButton:hover {color : white;}"
        play_icon = QtGui.QIcon(r'images\play_button.png')
        self.play_button.setIcon(play_icon)
        self.play_button.setIconSize(QtCore.QSize(50, 50))
        self.play_button.setStyleSheet(media_button_style)
        self.play_button.clicked.connect(self.play_pause)
        self.button_next_song.clicked.connect(self.play_next)
        self.button_next_song.setStyleSheet(media_button_style)
        self.button_previous_song.clicked.connect(self.play_last)
        self.button_previous_song.setStyleSheet(media_button_style)
        self.player.positionChanged.connect(self.update_seekbar)
        self.player.durationChanged.connect(self.update_seekbar_range)
        self.seek_bar.sliderMoved.connect(self.seek_through_song)
        self.frame_playing_media.hide()
        self.player.metaDataChanged.connect(self.meta_data_changed)
        self.frame_playing_media.setStyleSheet('background-color : rgb(40, 40, 40);')
    
    def playlist_setup(self):
        self.button_create_playlist.clicked.connect(self.create_playlist)
        self.input_playlist_name.returnPressed.connect(self.create_playlist)
        self.playlist_list.itemDoubleClicked.connect(self.playlist_double_clicked)
        self.playlist_page_song_list.itemDoubleClicked.connect(lambda: self.song_double_clicked(self.playlist_page_song_list, self.selected_playlist.songs))
        self.playlist_page_song_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.playlist_page_song_list.customContextMenuRequested.connect(self.song_playlist_context_menu)
        self.playlist_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.playlist_list.customContextMenuRequested.connect(self.playlist_list_context_menu)

    def initial_file_location(self):
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
        elif selected_content_page == 'Playlist':
            self.content_type_view_stack.setCurrentIndex(5)
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

    def update_seekbar(self, position, senderType = False):
        if senderType == False:
            self.seek_bar.setValue(position)
            self.seek_bar_position.setText(f'{int(position/60000):02}:{int(position/1000%60):02}')
        
    def update_seekbar_range(self, duration):
        self.seek_bar.setMaximum(duration)
        self.seek_bar_duration.setText(f'{int(duration/60000):02}:{int(duration/1000%60):02}')

    def seek_through_song(self, position):
        sender = self.seek_bar.sender()
        if isinstance(sender, QtWidgets.QSlider):
            self.player.setPosition(position)
    
    def meta_data_changed(self):
        song_title = self.player.metaData(QMediaMetaData.Title)
        if self.player.metaData(QMediaMetaData.ContributingArtist):
            album_artist = self.player.metaData(QMediaMetaData.ContributingArtist)[0]
        else:
            album_artist = self.player.metaData(QMediaMetaData.AlbumArtist)
        self.playing_song.setText(song_title)
        self.playing_song.adjustSize()
        self.playing_artist.setText(album_artist)
    
    def create_playlist(self):
        playlist_name = self.input_playlist_name.text()
        if playlist_name.replace(' ', '') != '':
            self.music_library.create_playlist(playlist_name)
            self.add_table_items(self.music_library.playlists.values(), self.playlist_list, ['Playlist'], ['name'])
        self.input_playlist_name.clear()

    def song_library_context_menu(self, selected_table, associated_library_list):
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
        self.music_library.add_playlist_song(playlist_clicked, selected_song)

    def remove_from_playlist(self, playlist_clicked, selected_song):
        self.music_library.remove_playlist_song(playlist_clicked, selected_song)
        self.add_table_items(self.selected_playlist.songs.values(), self.playlist_page_song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])

    def delete_playlist(self, playlist_clicked):
        self.music_library.delete_playlist(playlist_clicked)
        self.add_table_items(self.music_library.playlists.values(), self.playlist_list, ['Playlist'], ['name'])

    def playlist_double_clicked(self):
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
        index_to_insert = self.current_playing_list.currentIndex() + 1
        self.current_playing_list.insertMedia(index_to_insert, QMediaContent(QtCore.QUrl.fromLocalFile(song.song_file)))

        


#########################################################
#Actually display stuff
#########################################################

ui = PlayerWindow()
ui.MainWindow.showMaximized()
ui.initial_table_setup()
sys.exit(ui.app.exec_())