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
    start_folder_in_dialogs: str = r"F:"

    old_: tuple[str, str] = ('', '')
    new_: tuple[str, str] = ('', '')

    @classmethod
    def save_settings(cls):
        # if backup folders have changed, transfers all (settings and buckups) to a new location.
        # New folder must be an emty folder
        done_list = cls.make_copy_and_del_lists()

        # print('done list:', *done_list, sep='\n')
        # print('************************')
        # print(cls.path_main_folder, cls.path_settings_folder, cls.path_data_folder, sep='\n')
        # print('************************')

        if done_list:
            try:
                msg_text = "ARE YOU SHURE?\n" \
                           "If you press 'Yes' all you backup`s and settings data" \
                           " will be copied " \
                           f"to\n{cls.change_folder[0][1]}\n" \
                           "and source folder will be deleted\n" \
                           "(if you choose 'YES' in next 'Delete dialog')"
                reply = mw.msg_two_button("WARNING!", msg_text)
                if reply == 'no':
                    return
                else:
                    for _ in done_list:
                        cls.copy_to_new_location(_[0], _[1])
                        cls.del_item(_[0])
                        mw.progress_bar(3, f'Copy {_[0]}')

                cls.path_settings_folder, cls.path_data_folder = cls.new_
                cls.change_folder = []
                cls.flag_change_settings = True
                cls.settings_exist = True
                cls.old_ = cls.new_
            except IndexError:
                pass

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
        path = Path(f"{MainBase.path_settings_folder}/settings.ini")
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

    @classmethod
    def make_copy_and_del_lists(cls) -> list:
        temp_zip = zip(cls.old_, cls.new_)
        for _ in temp_zip:
            if _[0] != _[1] and _ not in cls.change_folder and _[0]:
                cls.change_folder.append(_)
        return list(reversed(cls.change_folder))

    @classmethod
    def copy_to_new_location(cls, old: str, new: str) -> None:
        """
        Copy all backup data from "old" folder to "new". Folder SETTINGS in new location must be
        empty. Then, if you choose to delete the source - cleans the "old" folder
        :param old:
        :param new:
        :return:
        """
        shutil.copytree(old, new, dirs_exist_ok=True)

    @classmethod
    def del_item(cls, item: str) -> None:
        """
        Delete sourse files and folders after copy (if accept warnings dialogs)
        :param cls:
        :param item: deleted items
        :return:
        """

        # TODO Problem remove rmtree readonly folder (from old backups. M.b. acces denied)
        msg_txt = f"Are you shure to delete folder\n{item}?"
        reply = mw.msg_two_button("WARNING!", msg_txt)
        if reply == 'no':
            return
        else:
            try:
                shutil.rmtree(item, ignore_errors=False, onerror=cls.rmtree_error)
            except PermissionError:
                mw.msg_one_button("Delete error", "Some files and folders were not deleted. "
                                                  "Please do it manually", "info")

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
    def check_reg_key(cls) -> dict:
        """
        If registry key in 'HKEY_LOCAL_MACHINE\\SOFTWARE' named 'EasyBack' not exist,
        return emty dict MainBase.settings. Else return dict with settings data:
        """
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                     r'SOFTWARE\EasyBack',
                                     0, winreg.KEY_READ)

            cls.get_all_settings_from_regkey(reg_key)

            winreg.CloseKey(reg_key)

        except FileNotFoundError:
            pass

        return MainBase.settings

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
            mw.msg_one_button("Nothing change", "You selected the same folder as it was.",
                              "info")
            return True
        else:
            return False

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    # end of chek section---------------------------------------------------------------------------

    # registry section *****************************************************************************
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

    # end of registry section  ---------------------------------------------------------------------

    @staticmethod
    def load_base_from_disk(path: str) -> dict:
        path_done = Path(path)
        with open(path_done, 'r') as f:
            dict_from_all = json.load(f)
        return dict_from_all

    # init of MainBase *****************************************************************************
    def __init__(self):
        self.all_items: dict = {}
        self.name_of_base_file: str = ""
        self.list_saved: bool = False

    def add_item(self, temp_dict: dict) -> None:
        self.all_items.update(temp_dict)

    def save_base_to_disk(self):
        path_of_backup_file = f"{MainBase.path_settings_folder}\\backup_lists"
        if not self.check_folder_exist(path_of_backup_file):
            Path.mkdir(Path(path_of_backup_file))

        name_of_backup_file = Path(f"{MainBase.path_settings_folder}\\backup_lists\\all")

        with open(name_of_backup_file, 'w') as f:
            json.dump(self.all_items, f)
