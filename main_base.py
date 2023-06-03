import json
from pathlib import Path


class MainBase:
    settings: dict = {}
    path_of_main_folder: str = ""
    path_of_settings_folder: str = ""
    path_of_data_folder: str = ""
    @classmethod
    def save_settings(cls):
        print("settings saved")

    def __init__(self):
        self.all_items: dict = {}
        self.name_of_base_file: str = ""
        self.list_saved: bool = False

    def check_main_folder(self) -> bool:
        return bool(self.path_of_main_folder)

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    def add_item(self, temp_dict: dict) -> None:
        self.all_items.update(temp_dict)

    def save_base_to_disk(self):
        name_of_backup_file = Path(f"{MainBase.path_of_main_folder}"
                                   f"//SETTINGS/backup_lists/test.blf")

        with open(name_of_backup_file, 'w') as f:
            json.dump(self.all_items, f)

    def load_base_from_disk(self):
        pass
