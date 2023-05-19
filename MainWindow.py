import sys
# from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog
from ui_MainWindow import Ui_MainWindow
# from ui_01_add_item import AddItemDial01
from ui_01_add_item import AddItemDial01


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_item.clicked.connect(self.add_item_01)
        self.ui.remove_item.clicked.connect(self.remove_item)
        self.ui.exit.clicked.connect(self.exit)

        # self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def add_item_01(self):
        dialog = QDialog()
        ui = AddItemDial01()
        ui.setupUi(dialog)
        dialog.exec()

    def remove_item(self):
        pass

    def open_directory_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.directory_list.extend(filenames)

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

        # self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def cancel_01_05(self):
        dialog = QDialog()
        ui = AddItemDial01()
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
