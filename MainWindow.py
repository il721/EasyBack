import sys

from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog
from d_MainWindow import Ui_MainWindow
from d__01_add_item import AddItemDial01
from d__07_settings import settings_Dialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_item.clicked.connect(self.add_item_01)
        self.ui.remove_item.clicked.connect(self.remove_item)

        self.ui.settings.clicked.connect(self.settings_bt)
        self.ui.exit.clicked.connect(self.exit)

        # self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def add_item_01(self):
        """
        Open 'Add Item To Base' dialog window
        """
        dialog = QDialog()
        ui = AddItemDial01()
        ui.setupUi_(dialog)
        dialog.exec()

    def remove_item(self):
        """
        Open 'Edit Item In Base' dialog window
        """
        pass

    def settings_bt(self):
        dialog = QDialog()
        ui = settings_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def exit(self):
        sys.exit()


class AddItem(MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = AddItemDial01()
        self.ui.setupUi(self)
        self.directory_list: list = []
        self.file_list: list = []

        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_folder.clicked.connect(self.remove_item)
        # self.ui.add_file.clicked.connect(self.open_file_dialog)

    def cancel_01_05(self):
        dialog = QDialog()
        ui = Ui_Dialog_ok()
        # ui = AddItemDial01()
        ui.setupUi(dialog)
        dialog.close()

    # def open_directory_dialog(self):
    #     dialog = QFileDialog(self)
    #     dialog.setDirectory(r'F:')
    #     dialog.setFileMode(QFileDialog.FileMode.Directory)
    #     dialog.setViewMode(QFileDialog.ViewMode.List)
    #     if dialog.exec():
    #         filenames = dialog.selectedFiles()
    #         if filenames:
    #             self.directory_list.extend(filenames)

    # def open_file_dialog(self):
    #     dialog = QFileDialog(self)
    #     dialog.setDirectory(r'F:')
    #     dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
    #     dialog.setViewMode(QFileDialog.ViewMode.List)
    #     dialog.setViewMode(QFileDialog.ViewMode.List)
    #     if dialog.exec():
    #         filenames = dialog.selectedFiles()
    #         if filenames:
    #             self.file_list.extend(filenames)

    def show_files_and_dir(self):
        pass
