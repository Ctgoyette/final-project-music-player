from PyQt5 import QtCore, QtGui, QtWidgets
from base_gui import *
from music_library import *
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
    def add_songs(self, songs_to_add):
        self.song_list.addItems(songs_to_add)

my_library = MusicLibrary()

#########################################################
''' Actually display stuff '''
#########################################################

app = QtWidgets.QApplication(sys.argv)
ui = PlayerWindow()
ui.add_songs(my_library.songs)
ui.MainWindow.show()
sys.exit(app.exec_())

