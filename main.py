import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
import MainWindow as mw
from main_base import MainBase


def first_time_check():
    """
    If registry key 'EasyBack' or (and) folder SETTINGS or (and) settings.ini not exist,
    show warning dialog and then run Settings menu.
    Else set some variables (taken from registry key) and flags in True
    """
    rez = MainBase.check_reg_key()

    # if no exist reg key EasyBack in HKEY_LOCAL_MACHINE\SOFTWARE\
    if not rez:
        MainBase.flag_change_settings = True
        path_or_regkey_not_exsit()  # show warning and start "settings" dialog

    # reg key is exist, but settings.ini is not exist
    elif MainBase.settings_exist:
        MainBase.settings_file_path = Path(f'{rez["settings_path"]}\\settings.ini')
        # settings_folder = Path(f'{rez["settings_path"]}')
        # print(Path.is_file(MainBase.settings_file_path))
        # print(Path.is_dir(settings_folder))
        # print(MainBase.settings_file_path)
        # print(settings_folder)
        # print(MainBase.settings_exist)

        # If file settings.ini not exist on MAIN folder
        if not Path.is_file(MainBase.settings_file_path):
            appearance_initial(rez)
            MainBase.flag_change_settings = True
            path_or_regkey_not_exsit()  # show warning and start "settings" dialog

        # If settings.ini is existing in MAIN folder
        else:
            # Initial set of some programm settings. Taken from registry key
            MainBase.settings_exist = True
            MainBase.path_main_folder = rez["main_path"]
            MainBase.path_settings_folder = rez["settings_path"]
            MainBase.path_data_folder = rez["data_path"]
            appearance_initial(rez)


def appearance_initial(rez):
    MainBase.start_folder_in_dialogs = rez["start_folder"]
    MainBase.font_size_dialog = rez["font_size_dialog"]
    MainBase.font_combo_index = int(rez["font_combo_index"])
    MainBase.font_color_info = rez["font_color_info"]
    MainBase.font_color_warn = rez["font_color_warn"]


def path_or_regkey_not_exsit():
    mw.msg_one_button('Settings not found', 'It looks like you are entering the program'
                                            ' for the first time. Please, '
                                            'go to SETTINGS and set some necessary '
                                            'parameters', 'warn')
    MainBase.settings_exist = False
    mw.MainWindowDialog.settings_bt()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mw.MainWindowDialog()
    window.show()
    first_time_check()
    sys.exit(app.exec())
