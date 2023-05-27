import json
from pathlib import Path


class MainBase:
    path_of_backup_folder: str = "F:/!_____back_test"

    # TODO remove default test path

    def __init__(self):
        self.all_items: dict = {}
        self.path_of_base_file: str = ""
        self.name_of_base_file: str = ""
        self.list_saved: bool = False

    def check_main_folder(self) -> bool:
        return bool(self.path_of_backup_folder)

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    def add_item(self, temp_dict: dict) -> None:
        self.all_items.update(temp_dict)

    def save_base_to_disk(self):
        name_of_backup_file = Path(f"{MainBase.path_of_backup_folder}/backup_lists/test.blf")

        with open(name_of_backup_file, 'w') as f:
            json.dump(self.all_items, f)

    def load_base_from_disk(self):
        pass
