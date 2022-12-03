from PyQt5 import QtCore, QtGui, QtWidgets 
from base_gui import Ui_MainWindow
from music_library import MusicLibrary, Song
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.music_library = MusicLibrary()
        self.library_dropdown_artist_index = self.library_view_dropdown.findText('Artists')
        self.library_dropdown_album_index = self.library_view_dropdown.findText('Albums')
        self.library_dropdown_song_index = self.library_view_dropdown.findText('Tracks')
        self.library_view_dropdown.currentIndexChanged.connect(self.switch_library_view)
        self.album_list.itemDoubleClicked.connect(lambda: self.album_double_clicked(self.album_list, self.music_library.albums))
        self.artist_list.itemDoubleClicked.connect(self.artist_double_clicked)
        self.switch_library_view()
        self.button_library_view.clicked.connect(lambda: self.switch_content_view('Library'))
        self.button_playlist_view.clicked.connect(lambda: self.switch_content_view('Playlists'))
        self.last_content_page_index_album = 0
        self.last_content_page_index_artist = 0
        self.album_page_back_button.clicked.connect(lambda: self.switch_content_view('Album_Previous'))
        self.artist_page_back_button.clicked.connect(lambda: self.switch_content_view('Artist_Previous'))
        self.selected_artist = self.music_library.artists[0]
        self.selected_album = self.music_library.albums[0]
        self.artist_page_album_list.itemDoubleClicked.connect(lambda: self.album_double_clicked(self.artist_page_album_list, self.selected_artist.albums))
        self.switch_content_view('Library')
        self.album_cover_display.setPixmap(QtGui.QPixmap(r'images\album-cover-placeholder.jpg').scaled(300, 300, QtCore.Qt.KeepAspectRatio))
        self.add_table_items(self.music_library.songs, self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
        self.add_table_items(self.music_library.albums, self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
        self.add_table_items(self.music_library.artists, self.artist_list, ['Artist'], ['name'])
        self.list_of_tables = [self.song_list, self.artist_list, self.album_list, self.playlist_list, self.album_page_song_list, self.artist_page_album_list]
        self.setup_table_resizing()

    def setup_table_resizing(self):
        for table in self.list_of_tables:
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def add_table_row(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

    def add_table_items(self, items_to_add, table, table_headings, attributes_to_add):
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
                while self.album_page_song_list.rowCount() > 1:
                    self.album_page_song_list.removeRow(1)
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
                while self.artist_page_album_list.rowCount() > 1:
                    self.artist_page_album_list.removeRow(1)
                self.artist_page_artist.setText(self.selected_artist.name)
                self.add_table_items(self.selected_artist.albums, self.artist_page_album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
                self.switch_content_view('Artist')
            elif column_index == 1:
                pass
            else:
                pass


#########################################################
#Actually display stuff
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
ui.MainWindow.show()
sys.exit(app.exec_())

