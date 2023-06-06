import sys
import winreg
from PySide6.QtWidgets import QApplication
import MainWindow as mw
from main_base import MainBase


def first_time_check():
    rez = MainBase.check_reg_key()
    if rez == "key not exist":
        print("key not exist")
        mw.msg_one_button('Settings not found', 'It looks like you are entering the program'
                                                ' for the first time. Please, '
                                                'go to SETTINGS and set some necessary '
                                                'parameters', 'warn')
        MainBase.settings_exist = False
        mw.MainWindowDialog.settings_bt(mw.MainWindowDialog)
    else:
        MainBase.settings_exist = True
        MainBase.path_of_main_folder = f'{rez[1]}'
        MainBase.path_of_settings_folder = f'{rez[1]}/SETTINGS'
        MainBase.path_of_data_folder = f'{rez[2]}'
        print(MainBase.path_of_data_folder)

    # TODO create folder settings exist


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mw.MainWindowDialog()
    window.show()
    first_time_check()
    sys.exit(app.exec())
