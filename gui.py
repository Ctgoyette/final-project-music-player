from PyQt5 import QtCore, QtGui, QtWidgets
from base_gui import *
from music_library import *
import sys
import os

class PlayerWindow(Ui_MainWindow):
    def add_songs(self, songs_to_add):
        self.song_list.addItems(songs_to_add)

my_library = MusicLibrary()

#########################################################
''' Actually display stuff '''
#########################################################

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = PlayerWindow()
ui.setupUi(MainWindow)
ui.add_songs(my_library.songs)
MainWindow.show()
sys.exit(app.exec_())

