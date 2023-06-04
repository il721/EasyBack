import sys

from PySide6 import QtGui
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QAbstractButton, QFileDialog, QMainWindow, QDialog, QMessageBox, \
    QPushButton
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

    def edit_list(self):
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
    msg_box.setStyleSheet(st.MSG_MAIN)

    msg_type = f":/icon/icons/GREY/msg_{type_of_msg}.svg"
    icon = QtGui.QPixmap(msg_type)
    msg_box.setIconPixmap(icon)
    msg_box.setText(main)
    msg_box.setWindowTitle(title)

    ok = QPushButton()
    ok.setStyleSheet(st.MSG_PUSH_BUTTON)
    ok.setText("Ok")
    ok.setMinimumSize(QSize(80, 50))
    # icon1 = QIcon()
    # icon1.addFile(u":/icon/icons/GREY/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
    # ok.setIcon(icon1)
    msg_box.addButton(ok, msg_box.ButtonRole.YesRole)
    # msg_box.setStandardButtons(msg_box.StandardButton.Yes | msg_box.StandardButton.No)
    # ok = msg_box.button(msg_box.StandardButton.Yes)
    msg_box.exec()

    #
    # if box.clickedButton() == buttonY:
    # # YES pressed
    # elif box.clickedButton() == buttonN:
    # # NO pressed

    # msg_box.information(self.list_files_and_folders, title, main)


def msg_two_button(title: str, main: str) -> bool:
    """
    Standart MessageBox dialog with two buttons "Yes" and "No".
    Return True if button "Yes" pressed, else, if "No" pressed return False
    :param title:
    :param main:
    :return:
    """
    msg_box = QMessageBox()
    msg_box.setStyleSheet(st.MSG_MAIN)

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
        return True
    elif msg_box.clickedButton() == cancel:
        return False

    #
    # if box.clickedButton() == buttonY:
    # # YES pressed
    # elif box.clickedButton() == buttonN:
    # # NO pressed

    # msg_box.information(self.list_files_and_folders, title, main)
