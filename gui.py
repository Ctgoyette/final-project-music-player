from PyQt5 import QtCore, QtGui, QtWidgets 
from base_gui import *
from music_library import *
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.artist_view_index = 0
        self.album_view_index = 1
        self.song_view_index = 2
        self.playlist_view_index = 3
        self.button_artist_view.clicked.connect(lambda: self.switch_list_view(self.artist_view_index))
        self.button_album_view.clicked.connect(lambda: self.switch_list_view(self.album_view_index))
        self.button_song_view.clicked.connect(lambda: self.switch_list_view(self.song_view_index))
        self.button_playlist_view.clicked.connect(lambda: self.switch_list_view(self.playlist_view_index))

    def add_table_row(self, table):
        rowCount = table.rowCount()
        table.insertRow(rowCount)

    def add_songs(self, songs_to_add):
        self.song_list.setItem(0, 0, QtWidgets.QTableWidgetItem('Title'))
        self.song_list.setItem(0, 1, QtWidgets.QTableWidgetItem('Artist'))
        self.song_list.setItem(0, 2, QtWidgets.QTableWidgetItem('Album'))
        self.song_list.setItem(0, 3, QtWidgets.QTableWidgetItem('Duration'))
        row = 1
        for song in songs_to_add:
            self.add_table_row(self.song_list)
            self.song_list.setItem(row, 0, QtWidgets.QTableWidgetItem(song.song_title))
            self.song_list.setItem(row, 1, QtWidgets.QTableWidgetItem(song.song_artist))
            self.song_list.setItem(row, 2, QtWidgets.QTableWidgetItem(song.song_album))
            self.song_list.setItem(row, 3, QtWidgets.QTableWidgetItem(str(song.song_duration_formatted)))
            row += 1
        self.song_list.resizeColumnsToContents()


    
    def switch_list_view(self, page_index):
        self.list_view_stack.setCurrentIndex(page_index)


my_library = MusicLibrary()

#########################################################
''' Actually display stuff '''
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
ui.add_songs(my_library.songs)
ui.MainWindow.show()
sys.exit(app.exec_())

