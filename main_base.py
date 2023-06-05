import json
import winreg
from pathlib import Path
import MainWindow as mw


class MainBase:
    settings_exist: bool = None
    settings: dict = {}
    path_of_main_folder: str = ""
    path_of_settings_folder: str = ""
    path_of_data_folder: str = ""

    @classmethod
    def save_settings(cls):
        cls.settings['main'] = cls.path_of_main_folder
        cls.settings['settings'] = cls.path_of_settings_folder
        cls.settings['data'] = cls.path_of_data_folder

        # check for settings file exist
        path = Path(f'{cls.path_of_settings_folder}\\settings.ini')
        if path.is_file():
            main = f'settings file is already exist in\n {cls.path_of_settings_folder}\n\n' \
                   f'If you want to change backup folders, do this in "Edit Backup List" section'
            mw.msg_one_button("WARNING!", main, 'warn')
            return

        # check for emty settings field
        if not cls.path_of_settings_folder:
            mw.msg_one_button("WARNING!", "You forget set 'SETTINGS' folder", 'warn')
            return

        if not cls.check_folder_exist(cls.path_of_settings_folder):
            Path.mkdir(Path(cls.path_of_settings_folder))
        if cls.path_of_data_folder:  # if DATA not set and needed, don`t create DATA folder
            if not cls.check_folder_exist(cls.path_of_data_folder):
                Path.mkdir(Path(cls.path_of_data_folder))
        path = Path(f"{MainBase.path_of_main_folder}/SETTINGS/settings.ini")
        with open(path, 'w') as f:
            json.dump(cls.settings, f)
        cls.settings_exist = True
        mw.msg_one_button('Congradulation!', 'Settings is successfully saved in '
                                             'settings.ini', 'info')
        # print(cls.settings)

    @classmethod
    def check_reg_key(cls):
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                     r'SOFTWARE\EasyBack',
                                     0, winreg.KEY_READ)
            key_value = winreg.QueryValueEx(reg_key, 'settings_path')[0]
            winreg.CloseKey(reg_key)
            return "key exist", key_value
        except FileNotFoundError:
            return "key not exist"

    @classmethod
    def create_reg_key(cls):
        key = winreg.HKEY_LOCAL_MACHINE
        subkey = r'SOFTWARE\EasyBack'
        name = 'settings_path'
        value = cls.path_of_main_folder
        winreg.CreateKeyEx(key, subkey, 0, winreg.KEY_WRITE)
        reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, name, 0, winreg.REG_SZ, value)
        print(cls.check_reg_key()[1])
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
        name_of_backup_file = Path(f"{MainBase.path_of_main_folder}"
                                   f"//SETTINGS/backup_lists/test.blf")

        with open(name_of_backup_file, 'w') as f:
            json.dump(self.all_items, f)
        # TODO save backup list

    def load_base_from_disk(self):
        pass
    # TODO load backup list
