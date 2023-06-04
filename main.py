import sys
import winreg
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow


# from MainWindow import MainWindow


def first_time_check():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r'SOFTWARE\EasyBack',
                                 0, winreg.KEY_READ)
        print(winreg.QueryValueEx(reg_key, 'settings_path')[0])
    except FileNotFoundError:
        pass


# TODO create main first cheking

if __name__ == '__main__':
    first_time_check()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
