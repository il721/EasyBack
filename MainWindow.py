import sys

from PySide6 import QtGui
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog, QMessageBox, QPushButton
from d_MainWindow import Ui_MainWindow
from d__01_add_item import AddItemDial01
from d__07_settings import settings_Dialog
import all_styles as st
from main_base import MainBase


class MainWindowDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.add_item.clicked.connect(self.add_item_01)
        self.ui.edit_list.clicked.connect(self.edit_list)

        self.ui.settings.clicked.connect(self.settings_bt)
        self.ui.exit.clicked.connect(self.exit)

        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # self.ui.add_item.clicked.connect(self.open_directory_dialog)
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    @staticmethod
    def add_item_01():
        """
        Open 'Add Item To Base' dialog window
        """
        dialog = QDialog()
        ui = AddItemDial01()
        ui.setupUi_(dialog)
        dialog.exec()

    def edit_list(self):
        """
        Open 'Edit Item In Base' dialog window
        """
        pass

    @staticmethod
    def settings_bt():
        dialog = QDialog()
        ui = settings_Dialog()
        ui.setupUi(dialog)
        # dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        dialog.exec()

    @staticmethod
    def exit():
        sys.exit()


def q_file_dialog_begin(start_folder: str, type_select: QFileDialog.FileMode) -> QFileDialog:
    """
    Repeted part of code in some file select dialog`s

    :param start_folder: parametr *** in dialog.setDirectory(***) (for eaxmple - r"F:"
    and dialog starts from root of disc F:)
    :param type_select: one of the types allowed in FileMode(enum.Enum) in dialog.setFileMode:
            QFileDialog.FileMode.AnyFile
            QFileDialog.FileMode.ExistingFile
            QFileDialog.FileMode.Directory
            QFileDialog.FileMode.ExistingFiles
    :return: QFileDialog
    """
    dialog = QFileDialog()
    dialog.setDirectory(start_folder)
    dialog.setFileMode(type_select)
    dialog.setViewMode(QFileDialog.ViewMode.List)
    return dialog


def msg_one_button(title: str, main: str, type_of_msg: str):
    """
    Standart MessageBox dialog. type_of_msg is "info" or "warm" for corresponding dialog type.
    Button is "Ok"

    :param title:
    :param main:
    :param type_of_msg:
    :return:
    """
    msg_box = QMessageBox()
    # msg_box.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    msg_box.setStyleSheet(
        'background-color: rgb(30, 30, 30);'
        f'color: {MainBase.font_color_info};'
        f'font: {MainBase.font_size_dialog}\"Lexend Light\";'
        'QDialogButtonBox {'
        'border: 10px solid;'
        'border-color: #FFFFFF;}'
        '')

    msg_type = f":/icon/icons/GREY/msg_{type_of_msg}.svg"
    icon = QtGui.QPixmap(msg_type)
    msg_box.setIconPixmap(icon)
    msg_box.setText(main)
    msg_box.setWindowTitle(title)

    ok = QPushButton()
    ok.setStyleSheet(st.MSG_PUSH_BUTTON)
    ok.setText("Ok")
    ok.setMinimumSize(QSize(80, 50))
    msg_box.addButton(ok, msg_box.ButtonRole.YesRole)
    msg_box.exec()


def msg_two_button(title: str, main: str) -> str:
    """
    Standart MessageBox dialog with two buttons "Yes" and "No".
    Return 'yes' if button "Yes" pressed, else, if "No" pressed return 'no'
    :param title:
    :param main:
    :return:
    """
    msg_box = QMessageBox()
    msg_box.setStyleSheet(
        f'background-color: rgb(30, 30, 30);\n'
        f'color: {MainBase.font_color_warn};\n'
        f'font: {MainBase.font_size_dialog}\"Lexend Light\";')

    icon = QtGui.QPixmap(":/icon/icons/GREY/msg_question.svg")
    msg_box.setIconPixmap(icon)
    msg_box.setText(main)
    msg_box.setWindowTitle(title)

    ok = QPushButton()
    ok.setStyleSheet(st.MSG_PUSH_BUTTON)
    ok.setText("  Yes")
    ok.setMinimumSize(QSize(110, 50))
    icon1 = QIcon()
    icon1.addFile(u":/icon/icons/GREY/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
    ok.setIcon(icon1)
    ok.setIconSize(QSize(35, 35))
    cancel = QPushButton()
    cancel.setStyleSheet(st.MSG_PUSH_BUTTON)
    cancel.setText("  No")
    cancel.setMinimumSize(QSize(110, 50))
    icon2 = QIcon()
    icon2.addFile(u":/icon/icons/GREY/cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
    cancel.setIcon(icon2)
    cancel.setIconSize(QSize(35, 35))
    msg_box.addButton(ok, msg_box.ButtonRole.YesRole)
    msg_box.addButton(cancel, msg_box.ButtonRole.NoRole)
    msg_box.exec()
    if msg_box.clickedButton() == ok:
        return 'yes'
    elif msg_box.clickedButton() == cancel:
        return 'no'

    #
    # if box.clickedButton() == buttonY:
    # # YES pressed
    # elif box.clickedButton() == buttonN:
    # # NO pressed

    # msg_box.information(self.list_files_and_folders, title, main)
