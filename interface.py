# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Now we are going to get stuff from PyQT6
# Have to tell it what we want because they offer a lot of stuff
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QComboBox
from PyQt6.QtGui import QPalette, QColor

# Creating the color class to customize our interface layout
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# Creating a subclass to customize our application's main window
# This will also create our window that a user interfaces with
class MainWindow(QMainWindow):
    def __init__(self):
        # Since I subclassed a Qtclass, I have to call the super__init__ function to setup my object
        super().__init__()

        # Giving my window a title which is the name of the app
        self.setWindowTitle("ITIT")

        widget = Color('purple')
        self.setCentralWidget(widget)

 
    #     # Adding a Push Button
    #     button = QPushButton("Push Me!")
    #     # Setting a maximum button size. 
    #     button.setMaximumSize(60, 48)
    #     # Checking to see if the button was clicked
    #     button.setCheckable(True)
    #     # Telling the program to connect with the button was clicked to make stuff happen
    #     # Slot one is doing this 
    #     button.clicked.connect(self.the_button_was_clicked)

    #     # Creating my drop down option
    #     dropdown = QComboBox(self)
    #     # Need to add 
    #     dropdown.addItems(["View Inventory", "Edit Inventory", "Export Inventory"])

    #     # Set button to be the central widget of the Window
    #     # Puts it in the middle
    #     self.setCentralWidget(button)
    
    # # Defining what happens when the button is clicked
    # def the_button_was_clicked(self):
    #     print("Clicked.")

# Creating the application
# Passing in sys.argv to allow command line arguements
# Applications handle our event loop
app = QApplication(sys.argv)

# Creating a Qt Widget which will be our window
window = MainWindow()
# IMPORTANT!!! Show the window
# Default is to hide the window
window.show()

# Start the event loop
app.exec()