import sys
from PySide6.QtWidgets import QApplication
from ui.MainWindow import PySideMainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = PySideMainWindow()
    window.show()
    sys.exit(app.exec())

