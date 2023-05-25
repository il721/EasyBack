class MainBase:
    def __init__(self):
        self.all_items: dict = {}
        self.list_of_file: list[str] = []
        self.name_item: str = ""

    def check_name(self, name_: str) -> bool:
        return name_ in self.all_items

    def add_item(self, name_: str, list_: list[str]) -> None:
        self.all_items[name_] = list_

    def save_base(self):
        pass

    def load_base(self):
        pass
