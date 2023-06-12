import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
import MainWindow as mw
from main_base import MainBase


def first_time_check():
    """
    If registry key 'EasyBack' or (and) folder SETTINGS not exist, show warning dialog and then
    run Settings menu. Else set some path variables (taken from registry key) and flag 'settings
    exist' in True
    """
    rez = MainBase.check_reg_key()
    if rez == "key not exist":
        path_or_regkey_not_exsit()
    elif not Path.is_dir(Path(f'{rez[1]}/SETTINGS')):
        path_or_regkey_not_exsit()
    else:
        MainBase.settings_exist = True
        MainBase.path_main_folder = f'{rez[1]}'
        MainBase.path_settings_folder = f'{rez[1]}/SETTINGS'
        MainBase.path_data_folder = f'{rez[2]}'


def path_or_regkey_not_exsit():
    mw.msg_one_button('Settings not found', 'It looks like you are entering the program'
                                            ' for the first time. Please, '
                                            'go to SETTINGS and set some necessary '
                                            'parameters', 'warn')
    MainBase.settings_exist = False
    mw.MainWindowDialog.settings_bt(mw.MainWindowDialog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mw.MainWindowDialog()
    window.show()
    first_time_check()
    sys.exit(app.exec())
