import json


class MainBase:
    def __init__(self):
        self.all_items: dict = {}
        self.path_of_base_file: str = ""
        self.path_of_backup_folder: str = ""

    def check_main_folder(self) -> bool:
        return self.path_of_backup_folder

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    def add_item(self, temp_dict: dict) -> None:
        self.all_items.update(temp_dict)

    def save_base_to_disk(self):
        pass

    def load_base_from_disk(self):
        pass
