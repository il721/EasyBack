import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
import MainWindow as mw
from main_base import MainBase
import all_styles as ass


def first_time_check():
    """
    If registry key 'EasyBack' or (and) folder SETTINGS not exist, show warning dialog and then
    run Settings menu. Else set some variables (taken from registry key) and flags in True
    """
    rez = MainBase.check_reg_key()

    # if no exist reg key EasyBack in HKEY_LOCAL_MACHINE\SOFTWARE\
    if rez == "key not exist":
        MainBase.flag_change_settings = True
        path_or_regkey_not_exsit()

    # reg key is exist, but SETTINGS folder is not exist or empty
    elif MainBase.settings_exist:
        try:
            sett_path = tuple(Path.iterdir(Path(f'{rez["settings_path"]}')))

            # If folder SETTINGS exist on disk, but emty
            if not sett_path:
                appearance_initial(rez)
                MainBase.flag_change_settings = True
                path_or_regkey_not_exsit()

            # If folder SETTINGS exist on disk and not emty
            else:
                # Initial set of some programm settings. Taken from registry key
                MainBase.settings_exist = True
                MainBase.path_main_folder = rez["main_path"]
                MainBase.path_settings_folder = rez["settings_path"]
                MainBase.path_data_folder = rez["data_path"]
                appearance_initial(rez)

        # If folder SETTINGS in reg key is not find in disk
        except FileNotFoundError:
            appearance_initial(rez)
            MainBase.flag_change_settings = True
            path_or_regkey_not_exsit()


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
