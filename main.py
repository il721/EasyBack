import sys
import winreg
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow


# from MainWindow import MainWindow


def first_time_check():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r'SOFTWARE\EasyBack',
                                 0, winreg.KEY_WRITE)
        print(reg_key)
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
