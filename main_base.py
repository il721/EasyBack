class MainBase:
    def __init__(self):
        self.all_items: dict = {}
        self.list_of_file: list[str] = []
        self.name_item: str = ""

    @staticmethod
    def check_name(name_: str, dict_: dict):
        if name_ in dict_:
            return True
        return False

    def add_item(self, name_: str, list_: list[str]) -> None:
        self.all_items[name_] = list_

    def save_base(self):
        pass
