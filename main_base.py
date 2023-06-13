import json
import winreg
from pathlib import Path
import shutil
import MainWindow as mw


class MainBase:
    settings_exist: bool = False
    flag_change_settings: bool = False
    settings: dict = {}
    path_main_folder: str = ""
    path_settings_folder: str = ""
    path_data_folder: str = ""
    old_path_main_folder: str = ""
    old_path_settings_folder: str = ""
    old_path_data_folder: str = ""
    start_folder_in_dialogs: str = r"F:"

    @classmethod
    def save_settings(cls):
        # if backup folders have changed, transfers all (settings and buckups) to a new location
        # after double confirmation
        if cls.flag_change_settings:
            path = f'{cls.path_settings_folder}\\settings.ini'
            msg_text = f'settings file is already exist in\n {path}\n\n' \
                       f'A you want to change backup folders?'
            reply = mw.msg_two_button("WARNING!", msg_text)
            if reply == 'no':
                return
            else:
                msg_text = "ARE YOU SHURE?\n" \
                           " If you press 'Yes' all you backup`s and settings fail will be move " \
                           "to new location. \n Old one will be deleted"
                reply = mw.msg_two_button("WARNING!!!", msg_text)
                if reply == 'no':
                    return
                else:
                    cls.flag_change_settings = False
                    cls.move_to_new_location(cls.old_path_main_folder, cls.path_main_folder)

        # check for emty settings field
        if not cls.path_settings_folder:
            mw.msg_one_button("WARNING!", "You forget set the 'SETTINGS' folder", 'warn')
            return

        # add keys to settings dictionary. ALL values must be str!!!
        cls.settings['main_path'] = cls.path_main_folder
        cls.settings['settings_path'] = cls.path_settings_folder
        cls.settings['data_path'] = cls.path_data_folder
        cls.settings['start_folder'] = cls.start_folder_in_dialogs

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
        mw.msg_one_button('Congradulation!', 'Settings is successfully saved in '
                                             'settings.ini', 'info')

    # TODO ADD move to new location all backups fuctional

    @classmethod
    def move_to_new_location(cls, old: str, new: str) -> None:
        """
        Move all backup data from "old" folder to "new". If folder SETTINGS is already exist in
        new location, clear everything inside "new"
        :param old:
        :param new:
        :return:
        """
        if Path(f"{new}/SETTINGS"):
            main_text = f"Destination folder is not empty!!! If you choose 'Yes' everything " \
                        f"inside the folder:\n {new}\n will be deleted"
            replay = mw.msg_two_button("Destination folder not empty!!!", main_text)
            if replay == 'yes':
                for _ in Path.iterdir(Path(new)):
                    shutil.rmtree(_)
            else:
                cls.flag_change_settings = False
                cls.path_main_folder = cls.old_path_main_folder
                cls.path_settings_folder = cls.old_path_settings_folder
                cls.path_data_folder = cls.old_path_data_folder
                return
        else:
            for _ in Path.iterdir(Path(old)):
                shutil.move(_, new)

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
            print(*[[key, val] for key, val in MainBase.settings.items()], sep="\n")

            winreg.CloseKey(reg_key)

            return MainBase.settings
        except FileNotFoundError:
            return "key not exist"

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

    @classmethod
    def create_reg_key(cls, keys):
        key = winreg.HKEY_LOCAL_MACHINE
        subkey = r'SOFTWARE\EasyBack'
        winreg.CreateKeyEx(key, subkey, 0, winreg.KEY_WRITE)
        reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
        for name, value in keys.items():
            winreg.SetValueEx(reg_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)

    @classmethod
    def check_folder_exist(cls, folder: str) -> bool:
        """
        Check exist or no on disk folder with given "folder" path
        :param folder: str (path of checking folder)
        :return:
        """
        return Path(folder).exists()

    def __init__(self):
        self.all_items: dict = {}
        self.name_of_base_file: str = ""
        self.list_saved: bool = False

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

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
