# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Now we are going to get stuff from PyQT6
# Have to tell it what we want because they offer a lot of stuff
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QComboBox, QGridLayout, QCheckBox, QLabel, QStatusBar, QToolBar
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon

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
        super(MainWindow, self).__init__()

        # Giving my window a title which is the name of the app
        self.setWindowTitle("ITIT")

        # Creating the page layout.
        layout = QGridLayout()

        # Creating the margins for the layout
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(10)

        # Grids start at (0,0) which is the top left-hand corner
        # I want mine to be 4 X 4

        # First Row aka my Navigation bar.
        layout.addWidget(Color('purple'), 0, 0)
        layout.addWidget(Color('blue'), 0, 1)
        layout.addWidget(Color('green'), 0, 2)
        layout.addWidget(Color('brown'), 0, 3)
        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        # Tool Bar
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #self.setCentralWidget(label)

        #Creating the toolbar
        toolbar = QToolBar("ITIT Toolbar")
        # I want my toolbar to have icons
        # Setting the icon size
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # My toolbar will need 4 buttons
        # 1 to search, 2 to add, 3 to update, and 4 to search

        # Creating the first button
        button_action = QAction(QIcon("SearchIcon.png"),"Search", self)
        button_action.setStatusTip("Search for Items in Inventory")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        # Making a space on my toolbar
        toolbar.addSeparator()

        # Creating the second button
        button_action2 = QAction(QIcon("PlusIcon"),"Add", self)
        button_action2.setStatusTip("Add Items to Inventory")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # Making a space on my toolbar
        toolbar.addSeparator()

        # Creating the third button
        button_action3 = QAction(QIcon("UpdateIcon"),"Update", self)
        button_action3.setStatusTip("Update Items in Inventory")
        button_action3.triggered.connect(self.onMyToolBarButtonClick)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        # Making a space on my toolbar
        toolbar.addSeparator()

        # Creating the fourth button
        button_action4 = QAction(QIcon("DeleteIcon.png"),"Delete", self)
        button_action4.setStatusTip("Delete Items in Inventory")
        button_action4.triggered.connect(self.onMyToolBarButtonClick)
        button_action4.setCheckable(True)
        toolbar.addAction(button_action4)

        # Making a space on my toolbar
        toolbar.addSeparator()

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


    #     # Adding a Push Button
    #     button = QPushButton("Push Me!")
    #     # Setting a maximum button size. 
    #     button.setMaximumSize(60, 48)
    #     # Checking to see if the button was clicked
    #     button.setCheckable(True)
    #     # Telling the program to connect with the button was clicked to make stuff happen
    #     # Slot one is doing this 
    #     button.clicked.connect(self.the_button_was_clicked)

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