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
        self.song_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.artist_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.album_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.album_list.itemDoubleClicked.connect(self.album_double_clicked)
        self.switch_library_view()
        self.button_library_view.clicked.connect(lambda: self.switch_content_view('Library'))
        self.button_playlist_view.clicked.connect(lambda: self.switch_content_view('Playlists'))
        self.playlist_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.album_page_song_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.last_content_view_index = 0
        self.back_button.clicked.connect(lambda: self.switch_content_view('Previous'))
        self.switch_content_view('Library')
        self.album_cover_display.setPixmap(QtGui.QPixmap(r'images\album-cover-placeholder.jpg').scaled(300, 300, QtCore.Qt.KeepAspectRatio))
        self.add_table_items(self.music_library.songs, self.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
        self.add_table_items(self.music_library.albums, self.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
        self.add_table_items(self.music_library.artists, self.artist_list, ['Artist'], ['name'])

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
        last_view = self.last_content_view_index
        self.last_content_view_index = self.content_type_view_stack.currentIndex()
        if selected_content_page == 'Library':
            self.content_type_view_stack.setCurrentIndex(0)
        elif selected_content_page == 'Playlists':
            self.content_type_view_stack.setCurrentIndex(1)
        elif selected_content_page == 'Album':
            self.content_type_view_stack.setCurrentIndex(2)
        elif selected_content_page == 'Previous':
            self.content_type_view_stack.setCurrentIndex(last_view)
        else:
            pass
    
    def album_double_clicked(self):
        row_index = self.album_list.currentRow()
        column_index = self.album_list.currentColumn()
        if row_index != 0:
            selected_album = self.music_library.albums[row_index - 1]
            if column_index == 0:
                while self.album_page_song_list.rowCount() > 1:
                    self.album_page_song_list.removeRow(1)
                self.album_page_album.setText(selected_album.name)
                self.album_page_artist.setText(selected_album.artist)
                self.album_page_year.setText(selected_album.year)
                self.add_table_items(selected_album.songs, self.album_page_song_list, ['Title', 'Duration'], ['title', 'duration_formatted'])
                self.switch_content_view('Album')
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

