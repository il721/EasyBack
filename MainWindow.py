from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMainWindow
from PySide6.QtCore import Slot
from ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        self.directory_list: list = []
        self.file_list: list = []

        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def open_directory_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.directory_list.extend(filenames)

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.extend(filenames)
    def show_files_and_dir(self):
        pass
