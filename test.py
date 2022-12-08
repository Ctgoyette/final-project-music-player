import os
from PyQt5 import QtWidgets

# Create a QApplication object to handle the GUI event loop
app = QtWidgets.QApplication([])

# Use the QFileDialog.getExistingDirectory() method to open a folder
folder = QtWidgets.QFileDialog.getExistingDirectory()

# Print the path of the selected folder to the console
print(folder)

# You can also access the contents of the selected folder
# by using the os.listdir() method to get a list of files
# in the folder
for file in os.listdir(folder):
    print(file)