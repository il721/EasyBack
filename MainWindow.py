import sys
import time

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog, QMessageBox, QProgressDialog, \
    QPushButton
from d_MainWindow import UiMainWindow
from d__01_add_item import AddItemDial01
from d__07_settings import SettingsDialog
# from d__progress_bar_cirkle import UiProgressBarCirkle
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
        progress_bar(5, 'Copy files...')

    @staticmethod
    def backup_all_bt():
        """
        Open 'Edit Item In Base' dialog window
        """
        progress_dialog(10)

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


def progress_bar(all_time: int, text: str) -> None:
    dialog = QDialog()
    ui = UiProgressBar(all_time, text)
    ui.setupUi(dialog)
    dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    ## ==> APPLY DROP SHADOW EFFECT
    # dialog.shadow = QGraphicsDropShadowEffect()
    # dialog.shadow.setBlurRadius(20)
    # dialog.shadow.setXOffset(5)
    # dialog.shadow.setYOffset(5)
    # dialog.shadow.setColor(QColor(0, 0, 0, 120))
    # dialog.setGraphicsEffect(dialog.shadow)
    dialog.exec()


# TODO !!MAKE progress bar

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
