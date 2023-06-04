import json
from pathlib import Path
import MainWindow as mw


class MainBase:
    settings: dict = {}
    path_of_main_folder: str = ""
    path_of_settings_folder: str = ""
    path_of_data_folder: str = ""

    @classmethod
    def save_settings(cls):
        cls.settings['main'] = cls.path_of_main_folder
        cls.settings['settings'] = cls.path_of_settings_folder
        cls.settings['data'] = cls.path_of_data_folder
        if not cls.check_folder_exist(cls.path_of_settings_folder):
            Path.mkdir(Path(cls.path_of_settings_folder))
        if cls.path_of_data_folder:  # if DATA not set and needed, don`t create DATA folder
            if not cls.check_folder_exist(cls.path_of_data_folder):
                Path.mkdir(Path(cls.path_of_data_folder))
        path = Path(f"{MainBase.path_of_main_folder}/SETTINGS/settings.ini")
        with open(path, 'w') as f:
            json.dump(cls.settings, f)
        mw.msg_one_button('Congradulation!', 'Settings is successfully saved in '
                                             'settings.ini', 'info')
        print(cls.settings)

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
