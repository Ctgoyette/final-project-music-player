from PyQt5 import QtCore, QtGui, QtWidgets 
from base_gui import Ui_MainWindow
from music_library import MusicLibrary
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.artist_dropdown_index = self.library_list_view_dropdown.findText('Artists')
        self.album_dropdown_index = self.library_list_view_dropdown.findText('Albums')
        self.song_dropdown_index = self.library_list_view_dropdown.findText('Tracks')
        self.library_list_view_dropdown.currentIndexChanged.connect(self.switch_list_view)
        self.artist_list_index = 0
        self.album_list_index = 1
        self.song_list_index = 1
        self.switch_list_view()
        self.song_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.artist_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.album_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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

    def switch_list_view(self):
        index = self.library_list_view_dropdown.currentIndex()
        if  index == self.artist_dropdown_index:
            self.library_view_stack.setCurrentIndex(0)
        elif index == self.album_dropdown_index:
            self.library_view_stack.setCurrentIndex(1)
        elif index == self.song_dropdown_index:
            self.library_view_stack.setCurrentIndex(2)
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

