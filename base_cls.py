class BuckUpList:
    def __init__(self, ):
        self.app_list: list[AppForBuckup] = []

    def add_app(self):
        """ Add programs to BuckAppList"""
        pass

    #     TODO: add functional

    def remove_app(self):
        """ Remove programs to BuckAppList"""
        pass
    #     TODO: add functional


class AppForBuckup:
    def __init__(self, ):
        self.name: str = ''
        self.items_for_backup: list[tuple[str, str]] = []
        pass
    #     TODO: add functional
