# With the help of GitHub Copilot:

# Create a PySide6 calculator application
# The application will have a window with a display for showing the result
# of the calculation and a set of buttons for the calculation.
# The buttons will be:
# - 7, 8, 9, +, -, *, /, =, C, CE, %
# The user can enter a calculation in the display and press the buttons to
# perform the calculation.
# The result will be shown in the display.
# The user can also press the CE button to clear the display.
# The user can also press the % button to show the percentage of the result.

# Import the PySide6 module
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QLabel
from PySide6.QtCore import Qt
# Import qfont
from PySide6.QtGui import QFont
# Import sys
import sys


# Create a class for the calculator
class PyQtCalculator(QWidget):
    # Create the constructor
    def __init__(self):
        # Create an instance of the QWidget class
        super().__init__()
        # Set the window title
        self.setWindowTitle('PyQt Calculator')
        # Set the window size
        self.resize(300, 300)
        # Create a grid layout
        self.grid = QGridLayout()
        # Create a label to show the result
        self.label = QLabel('0', self)
        # Set the font of the label
        self.label.setFont(QFont('Arial', 20))
        # Add the label to the grid layout
        self.grid.addWidget(self.label, 0, 0, 1, 4)
        # Create a button for the 7
        self.button_7 = QPushButton('7', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_7, 1, 0)
        # Create a button for the 8
        self.button_8 = QPushButton('8', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_8, 1, 1)
        # Create a button for the =
        self.button_equal = QPushButton('=', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_equal, 4, 1)
        # Create a button for the /
        self.button_divide = QPushButton('/', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_divide, 4, 2)
        # Create a button for the CE
        self.button_CE = QPushButton('CE', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_CE, 5, 0)
        # Create a button for the C
        self.button_C = QPushButton('C', self)
        # Add the button to the grid layout
        self.grid.addWidget(self.button_C, 5, 1)

        # Set the layout of the window
        self.setLayout(self.grid)
        # Connect the buttons to the functions
        self.button_7.clicked.connect(self.button_7_clicked)
        self.button_8.clicked.connect(self.button_8_clicked)
        self.button_equal.clicked.connect(self.button_equal_clicked)
        self.button_divide.clicked.connect(self.button_divide_clicked)
        self.button_CE.clicked.connect(self.button_CE_clicked)
        self.button_C.clicked.connect(self.button_C_clicked)

    # Define the functions for the buttons
    def button_7_clicked(self):
        self.label.setText(self.label.text() + '7')

    def button_8_clicked(self):
        self.label.setText(self.label.text() + '8')

    def button_0_clicked(self):
        self.label.setText(self.label.text() + '0')

    def button_equal_clicked(self):
        # self.label.setText(self.label.text() + '=')
        # Remove leading zeros from the string
        self.label.setText(self.label.text().lstrip('0'))
        # Calculate the result
        self.label.setText(str(eval(self.label.text())))

    def button_divide_clicked(self):
        self.label.setText(self.label.text() + '/')

    def button_ce_clicked(self):
        self.label.setText('')

    def button_c_clicked(self):
        self.label.setText(self.label.text()[:-1])


# Create an instance of the application window and run it
app = QApplication(sys.argv)
window = PyQtCalculator()
window.show()
sys.exit(app.exec_())
