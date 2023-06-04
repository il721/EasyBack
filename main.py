import sys
import winreg
from PySide6.QtWidgets import QApplication
import MainWindow as mw
from main_base import MainBase


def first_time_check():
    if MainBase.check_reg_key() == "key not exist":
        print("key not exist")
        mw.msg_one_button('Registry key not found', 'It looks like you are entering the program'
                                                    ' for the first time. Please, '
                                                    'go to SETTINGS and set some necessary '
                                                    'parameters', 'warn')


# TODO create main first cheking

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mw.MainWindowDialog()
    window.show()
    first_time_check()
    sys.exit(app.exec())
