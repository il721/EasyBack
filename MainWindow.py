import sys
import time
import shutil
from  pathlib import Path

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog, QMessageBox, QProgressDialog, \
    QPushButton
from d_MainWindow import UiMainWindow
from d__01_add_item import AddItemDial01
from d__02_edit_list_main import EditListMain
from d__07_settings import SettingsDialog
from d__progress_bar import UiProgressBar
import all_styles as st
from main_base import MainBase


class MainWindowDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_item.clicked.connect(self.add_item_01_bt)
        self.ui.edit_list.clicked.connect(self.edit_list_bt)
        self.ui.backup_all.clicked.connect(self.backup_all_bt)

        self.ui.settings.clicked.connect(self.settings_bt)
        self.ui.exit.clicked.connect(self.exit_bt)

        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    @staticmethod
    def add_item_01_bt():
        """
        Open 'Add Item To Base' dialog window
        """
        dialog = QDialog()
        ui = AddItemDial01()
        ui.setupUi(dialog)
        dialog.exec()

    @staticmethod
    def edit_list_bt():
        """
        Open 'Edit Item In Base' dialog window
        """
        dialog = QDialog()
        ui = EditListMain()
        ui.setupUi(dialog)
        dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        dialog.exec()

    @staticmethod
    def backup_all_bt():
        """
        Make backup list and copy files and folders from it in main backup folder
        """
        path = f"{MainBase.path_settings_folder}\\backup_lists\\all"
        all_dict = MainBase.load_base_from_disk(path)
        data_dict = {}

        settings_dict = {k[2:]: v for k, v in all_dict.items() if k[0] == 's'}
        if len(settings_dict) != len(all_dict):
            data_dict = {k[2:]: v for k, v in all_dict.items() if k[0] == 'd'}
        # print(settings_dict, data_dict, all_dict, sep="\n")

        for name_item, value_item, in settings_dict.items():
            # print(name_item, value_item)

            dst_path = Path(f"{MainBase.path_settings_folder}\\{name_item}")
            for _ in value_item:
                if Path.is_file(Path(_)):
                    shutil.copy2(_, dst_path)
                    print(_)
                else:
                    shutil.copytree(_, dst_path, dirs_exist_ok=True)
                    print(_)
        # TODO Add "delete list"
        # TODO Split to smallest functions

    @staticmethod
    def settings_bt():
        dialog = QDialog()
        ui = SettingsDialog()
        ui.setupUi(dialog)
        # dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        dialog.exec()

    @staticmethod
    def exit_bt():
        sys.exit()


# Shared dialog helpers (q_file_dialog_begin, msg_one_button, msg_two_button,
# progress_bar) now live in ui_helpers.py so that main_base and the dialog
# controllers can use them without importing this top-level module.

def progress_dialog(num_files):
    progress = QProgressDialog("Copying files...", "Abort Copy", 0, num_files)
    progress.setMinimum(0.1)
    # progress.setMaximum(10)
    progress.setWindowModality(Qt.WindowModal)
    progress.setStyleSheet(st.PROGRESS_BAR_LINE)
    progress.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    for i in range(num_files):
        progress.setValue(i)
        time.sleep(0.5)

        if progress.wasCanceled():
            break

    progress.setValue(num_files)
