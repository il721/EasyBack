import json
import os
import stat
import winreg
from pathlib import Path
import shutil
import MainWindow as mw


class MainBase:
    settings_exist: bool = False
    change_folder: list = []
    flag_change_settings: bool = False
    settings: dict = {}  # set up new items in save_settings(cls)
    font_size_dialog: str = "18Pt"
    font_color_info: str = "#e6e6e6"
    font_color_warn: str = "#ff4f1a"
    font_combo_index: int = 0
    settings_file_path = ""
    path_main_folder: str = ""
    path_settings_folder: str = ""
    path_data_folder: str = ""
    old_path_main_folder: str = ""
    old_path_settings_folder: str = ""
    old_path_data_folder: str = ""
    start_folder_in_dialogs: str = r"F:"

    @classmethod
    def save_settings(cls):
        # if backup folders have changed, transfers all (settings and buckups) to a new location.
        # New folder must be an emty folder
        copy_list = list(zip(cls.change_folder[0::2], cls.change_folder[1::2]))
        del_list = reversed(copy_list)
        for _ in copy_list:
            print(f"{_[0]}\t-->\t{_[1]}")
        print()
        for _ in del_list:
            if _[0]:
                print(f"{_[0]}")
        # if cls.change_folder:
        #     msg_text = "ARE YOU SHURE?\n" \
        #                "If you press 'Yes' all you backup`s and settings data will be copied " \
        #                "to new location."
        #     reply = mw.msg_two_button("WARNING!", msg_text)
        #     if reply == 'no':
        #         return
        #     else:
        #         cls.change_folder = []
        #         cls.flag_change_settings = True
        #
        #         # If SETTINGS folder is in Main folder (SETT. and DATA both)
        #         if cls.path_main_folder != cls.path_settings_folder:
        #             cls.copy_move_to_new_location(cls.old_path_main_folder, cls.path_main_folder, 0)
        #
        #         # If SETTINGS folder is Main folder
        #         else:
        #             cls.copy_move_to_new_location(cls.old_path_settings_folder,
        #                                           cls.path_settings_folder, 1)
        #             if cls.path_data_folder and \
        #                     cls.old_path_data_folder != cls.path_data_folder:
        #                 cls.copy_move_to_new_location(cls.old_path_data_folder,
        #                                               cls.path_data_folder, 1)

        # check for emty settings field
        if not cls.path_settings_folder:
            mw.msg_one_button("WARNING!", "You forget set the 'SETTINGS' folder", 'warn')
            return

        # add keys to settings dictionary and regkey. ALL values must be str!!!---------------------
        cls.settings['main_path'] = cls.path_main_folder
        cls.settings['settings_path'] = cls.path_settings_folder
        cls.settings['data_path'] = cls.path_data_folder
        cls.settings['start_folder'] = cls.start_folder_in_dialogs
        cls.settings['font_size_dialog'] = cls.font_size_dialog
        cls.settings['font_combo_index'] = str(cls.font_combo_index)
        cls.settings['font_color_info'] = str(cls.font_color_info)
        cls.settings['font_color_warn'] = str(cls.font_color_warn)
        # !!!Don`t forget adding new key`s in main.py appearance_initial ---------------------------

        if not cls.check_folder_exist(cls.path_settings_folder):
            Path.mkdir(Path(cls.path_settings_folder))
        if cls.path_data_folder:  # if DATA not set and needed, don`t create DATA folder
            if not cls.check_folder_exist(cls.path_data_folder):
                Path.mkdir(Path(cls.path_data_folder))
        path = Path(f"{MainBase.path_main_folder}/settings.ini")
        with open(path, 'w') as f:
            json.dump(cls.settings, f)
        cls.settings_exist = True
        cls.create_reg_key(cls.settings)
        if cls.flag_change_settings or cls.change_folder:
            mw.msg_one_button('Congradulation!', 'Settings is successfully saved in '
                                                 'settings.ini', 'info')
            cls.change_folder = []
            cls.flag_change_settings = False
        else:
            mw.msg_one_button("Nothing changed", "You haven't changed anything in the settings. "
                                                 "Nothing to save", "info")

    # @classmethod
    # def save_settings_old(cls):
    #     # if backup folders have changed, transfers all (settings and buckups) to a new location.
    #     # New folder must be an emty folder
    #     if cls.change_folder:
    #
    #         msg_text = "ARE YOU SHURE?\n" \
    #                    "If you press 'Yes' all you backup`s and settings data will be copied " \
    #                    "to new location."
    #         reply = mw.msg_two_button("WARNING!", msg_text)
    #         if reply == 'no':
    #             return
    #         else:
    #             cls.change_folder = False
    #             cls.flag_change_settings = True
    #
    #             # If SETTINGS folder is in Main folder (SETT. and DATA both)
    #             if cls.path_main_folder != cls.path_settings_folder:
    #                 cls.copy_move_to_new_location(cls.old_path_main_folder, cls.path_main_folder, 0)
    #
    #             # If SETTINGS folder is Main folder
    #             else:
    #                 cls.copy_move_to_new_location(cls.old_path_settings_folder,
    #                                               cls.path_settings_folder, 1)
    #                 if cls.path_data_folder and \
    #                         cls.old_path_data_folder != cls.path_data_folder:
    #                     cls.copy_move_to_new_location(cls.old_path_data_folder,
    #                                                   cls.path_data_folder, 1)
    #
    #     # check for emty settings field
    #     if not cls.path_settings_folder:
    #         mw.msg_one_button("WARNING!", "You forget set the 'SETTINGS' folder", 'warn')
    #         return
    #
    #     # add keys to settings dictionary and regkey. ALL values must be str!!!---------------------
    #     cls.settings['main_path'] = cls.path_main_folder
    #     cls.settings['settings_path'] = cls.path_settings_folder
    #     cls.settings['data_path'] = cls.path_data_folder
    #     cls.settings['start_folder'] = cls.start_folder_in_dialogs
    #     cls.settings['font_size_dialog'] = cls.font_size_dialog
    #     cls.settings['font_combo_index'] = str(cls.font_combo_index)
    #     cls.settings['font_color_info'] = str(cls.font_color_info)
    #     cls.settings['font_color_warn'] = str(cls.font_color_warn)
    #     # !!!Don`t forget adding new key`s in main.py appearance_initial ---------------------------
    #
    #     if not cls.check_folder_exist(cls.path_settings_folder):
    #         Path.mkdir(Path(cls.path_settings_folder))
    #     if cls.path_data_folder:  # if DATA not set and needed, don`t create DATA folder
    #         if not cls.check_folder_exist(cls.path_data_folder):
    #             Path.mkdir(Path(cls.path_data_folder))
    #     path = Path(f"{MainBase.path_main_folder}/settings.ini")
    #     with open(path, 'w') as f:
    #         json.dump(cls.settings, f)
    #     cls.settings_exist = True
    #     cls.create_reg_key(cls.settings)
    #     if cls.flag_change_settings or cls.flag_change_settings:
    #         mw.msg_one_button('Congradulation!', 'Settings is successfully saved in '
    #                                              'settings.ini', 'info')
    #         cls.change_folder = False
    #         cls.flag_change_settings = False
    #     else:
    #         mw.msg_one_button("Nothing changed", "You haven't changed anything in the settings. "
    #                                              "Nothing to save", "info")

    # TODO ^^^^^^^^^^^!!!!!REMOVE AFTER ALL TESTING^^^^^^^^^^^^

    @classmethod
    def copy_move_to_new_location(cls, old: str, new: str, type_del: int) -> None:
        """
        Copy all backup data from "old" folder to "new". Folder SETTINGS in new location must be
        empty. Then, if you choose to delete the source - cleans the "old" folder
        :param type_del: chose what folders are was deleted.
            0 - both DATA and SETTINGS
            1 - SETTINGS or DATA separately
        :param old:
        :param new:
        :return:
        """
        # print('old: ', old, 'new: ', new)
        mw.progress_bar(5, 'Copy files...')
        shutil.copytree(old, new, dirs_exist_ok=True)

        # Delete block
        msg_text = "Remove old data?\n" \
                   "If you press 'Yes' all you backup`s and settings data in old folder will be " \
                   "deleted."
        reply = mw.msg_two_button("WARNING!", msg_text)
        if reply == 'no':
            return
        else:
            if type_del == 0:
                msg_text = f"Delete all in folder\n{old}?"
                reply = mw.msg_two_button("WARNING!", msg_text)
                if reply == 'no':
                    return
                else:
                    cls.del_source(old)
                    mw.progress_bar(5, 'Delete files...')
            elif type_del == 1:
                del_folder = f"{old}"
                # print(del_folder)
                msg_text = f"Delete all in folder\n{del_folder}?"
                reply = mw.msg_two_button("WARNING!", msg_text)
                if reply == 'no':
                    return
                else:
                    shutil.rmtree(old)
                    mw.progress_bar(5, 'Delete files...')

    @classmethod
    def del_source(cls, old: str) -> None:
        for _ in Path.iterdir(Path(old)):

            # TODO Problem remove rmtree readonly folder
            if _.is_dir():
                try:
                    shutil.rmtree(_, ignore_errors=False, onerror=cls.rmtree_error)
                    # TODO Insert progress bar
                except PermissionError:
                    mw.msg_one_button("Delete error", "Some files and folders were not deleted. "
                                                      "Please do it manually", "info")
            else:
                try:
                    _.unlink()
                    # TODO Insert progress bar
                except PermissionError:
                    os.chmod(_, stat.S_IWRITE)
                    os.unlink(_)

    @staticmethod
    def rmtree_error(func, path_err, exc_info):
        os.chmod(path_err, stat.S_IWRITE)
        os.unlink(path_err)

    # Check section--------------------------------------------------------------------------------
    @classmethod
    def check_file_exist(cls, path_str: str) -> bool:
        path = Path(path_str)
        return path.is_file()

    @classmethod
    def check_reg_key(cls):
        """
        If registry key in 'HKEY_LOCAL_MACHINE\\SOFTWARE' named 'EasyBack' not exist,
        return 'key not exist'. Else return tuple:
        ('key exist',main_path value, data_path value)
        """
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                     r'SOFTWARE\EasyBack',
                                     0, winreg.KEY_READ)

            cls.get_all_settings_from_regkey(reg_key)

            # print(*[[key, val] for key, val in MainBase.settings.items() if
            #         key in ('main_path', 'settings_path', 'data_path')], sep="\n")
            # print(*[[key, val] for key, val in MainBase.settings.items()], sep="\n")

            winreg.CloseKey(reg_key)

            return MainBase.settings
        except FileNotFoundError:
            return "key not exist"

    @classmethod
    def check_folder_for_empty(cls, folder_path: str) -> bool:
        """
        Checks if a folder is empty. Is answer - yes return True
        :param folder_path:
        :return:
        """
        if tuple(Path(folder_path).iterdir()):
            main_text = f"Destination folder is not empty!!! Please select an emty folder"
            mw.msg_one_button("Destination folder not empty!!!", main_text, 'warn')
            return True
        else:
            return False

    @classmethod
    def check_folder_exist(cls, folder: str) -> bool:
        """
        Check exist or no on disk folder with given "folder" path
        :param folder: str (path of checking folder)
        :return:
        """
        return Path(folder).exists()

    @classmethod
    def check_select_same_folder(cls, old_folder_path: str, new_folder_path: str) -> bool:
        """
        Checks if the selected folder is the same as it was. If yes - return True
        :param new_folder_path:
        :param old_folder_path:
        :return:
        """
        if old_folder_path == new_folder_path:
            MainBase.change_folder = ''
            mw.msg_one_button("Nothing change", "You selected the same folder as it was. Try again",
                              "info")
            return True
        else:
            return False

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    # end of chek section---------------------------------------------------------------------------

    @classmethod
    def get_all_settings_from_regkey(cls, key: winreg.OpenKey) -> None:
        """
        Fills the settings dictionary with values from subkeys of EasyBack registry key
        :param key:
        :return:
        """
        # number of subkey (settings item) in main regkey EasyBack
        num = winreg.QueryInfoKey(key)[1]

        for _ in range(num):
            MainBase.settings[winreg.EnumValue(key, _)[0]] = winreg.EnumValue(key, _)[1]
        MainBase.settings_exist = True

    @classmethod
    def create_reg_key(cls, keys):
        key = winreg.HKEY_LOCAL_MACHINE
        subkey = r'SOFTWARE\EasyBack'
        winreg.CreateKeyEx(key, subkey, 0, winreg.KEY_WRITE)
        reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
        for name, value in keys.items():
            winreg.SetValueEx(reg_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)

    def __init__(self):
        self.all_items: dict = {}
        self.name_of_base_file: str = ""
        self.list_saved: bool = False

    def add_item(self, temp_dict: dict) -> None:
        self.all_items.update(temp_dict)

    def save_base_to_disk(self):
        name_of_backup_file = Path(f"{MainBase.path_main_folder}"
                                   f"//SETTINGS/backup_lists/test.blf")

        with open(name_of_backup_file, 'w') as f:
            json.dump(self.all_items, f)
        # TODO save backup list

    def load_base_from_disk(self):
        pass
    # TODO load backup list
