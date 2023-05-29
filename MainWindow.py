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


def msg_info(title: str, main: str):
    msg_box = QMessageBox()
    # msg_box.setStyleSheet("background-color: rgb(30, 30, 30);\n"
    #                       "color: rgb(230, 230, 230);\n"
    #                       "font: 300 19pt \"Lexend Light\";")
    msg_box.setStyleSheet(st.MSG_MAIN)

    icon = QtGui.QPixmap(":/icon/icons/GREY/msg_info.svg")
    msg_box.setIconPixmap(icon)
    msg_box.setText(main)
    msg_box.setWindowTitle(title)

    ok = QPushButton()
    ok.setStyleSheet(st.MSG_PUSH_BUTTON)
    ok.setText("Ok")
    ok.setMinimumSize(QSize(60, 50))
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
