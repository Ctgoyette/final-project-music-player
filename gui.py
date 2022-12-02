from PyQt5 import QtCore, QtGui, QtWidgets 
from base_gui import Ui_MainWindow
from music_library import MusicLibrary
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.library_dropdown_artist_index = self.library_view_dropdown.findText('Artists')
        self.library_dropdown_album_index = self.library_view_dropdown.findText('Albums')
        self.library_dropdown_song_index = self.library_view_dropdown.findText('Tracks')
        self.library_view_dropdown.currentIndexChanged.connect(self.switch_library_view)
        self.song_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.artist_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.album_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.switch_library_view()
        self.button_library_view.clicked.connect(lambda: self.switch_content_view('Library'))
        self.button_playlist_view.clicked.connect(lambda: self.switch_content_view('Playlists'))
        self.playlist_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.switch_content_view('Library')

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
        else:
            pass





my_library = MusicLibrary()

#########################################################
#Actually display stuff
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
ui.add_table_items(my_library.songs, ui.song_list, ['Title', 'Artist', 'Album', 'Duration'], ['title', 'artist', 'album', 'duration_formatted'])
ui.add_table_items(my_library.albums, ui.album_list, ['Album', 'Artist', 'Year'], ['name', 'artist', 'year'])
ui.add_table_items(my_library.artists, ui.artist_list, ['Artist'], ['name'])
ui.MainWindow.show()
sys.exit(app.exec_())

