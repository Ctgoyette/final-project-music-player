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

    def add_table_row(self, table):
        rowCount = table.rowCount()
        table.insertRow(rowCount)

    def add_songs_to_display(self, songs_to_add):
        self.song_list.setItem(0, 0, QtWidgets.QTableWidgetItem('Title'))
        self.song_list.setItem(0, 1, QtWidgets.QTableWidgetItem('Artist'))
        self.song_list.setItem(0, 2, QtWidgets.QTableWidgetItem('Album'))
        self.song_list.setItem(0, 3, QtWidgets.QTableWidgetItem('Duration'))
        row = 1
        for song in songs_to_add:
            self.add_table_row(self.song_list)
            self.song_list.setItem(row, 0, QtWidgets.QTableWidgetItem(song.title))
            self.song_list.setItem(row, 1, QtWidgets.QTableWidgetItem(song.artist))
            self.song_list.setItem(row, 2, QtWidgets.QTableWidgetItem(song.album))
            self.song_list.setItem(row, 3, QtWidgets.QTableWidgetItem(str(song.duration_formatted)))
            row += 1
        self.song_list.resizeColumnsToContents()
    
    def add_albums_to_display(self, albums_to_add):
        self.album_list.setItem(0, 0, QtWidgets.QTableWidgetItem('Album'))
        self.album_list.setItem(0, 1, QtWidgets.QTableWidgetItem('Artist'))
        self.album_list.setItem(0, 2, QtWidgets.QTableWidgetItem('Year'))
        row = 1
        for album in albums_to_add:
            self.add_table_row(self.album_list)
            self.album_list.setItem(row, 0, QtWidgets.QTableWidgetItem(album.album_name))
            self.album_list.setItem(row, 1, QtWidgets.QTableWidgetItem(album.album_artist))
            self.album_list.setItem(row, 2, QtWidgets.QTableWidgetItem(str(album.album_year)))
            row += 1
        self.album_list.resizeColumnsToContents()

    
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
''' Actually display stuff '''
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
ui.add_songs_to_display(my_library.songs)
ui.add_albums_to_display(my_library.albums)
ui.MainWindow.show()
sys.exit(app.exec_())

