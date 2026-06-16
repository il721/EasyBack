"""Shared dialog helpers (file pickers, styled message boxes, progress bar).

Extracted from MainWindow.py so the model/dialog layers (main_base, the d__*.py
controllers, main.py) can use these without importing the top-level MainWindow
module - which previously created an import cycle
(main_base <-> MainWindow <-> dialogs).

MainBase and UiProgressBar are imported lazily inside the functions, so this
module has no project imports at load time (it is an import-time leaf) and can
therefore be imported safely from main_base.py.
"""
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog
import all_styles as st


class MovableDialog(QDialog):
    """A frameless dialog the user can reposition by dragging its body.

    The custom dialogs are shown with FramelessWindowHint (no title bar), so Qt
    gives them no built-in way to move. Pressing the left mouse button on the
    dialog background (anywhere a child widget does not consume the event) and
    dragging now moves the whole window.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._drag_offset = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._drag_offset = (event.globalPosition().toPoint()
                                 - self.frameGeometry().topLeft())
            event.accept()

    def mouseMoveEvent(self, event):
        if (self._drag_offset is not None
                and event.buttons() & QtCore.Qt.MouseButton.LeftButton):
            self.move(event.globalPosition().toPoint() - self._drag_offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_offset = None
        event.accept()


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
    from main_base import MainBase

    msg_box = QMessageBox()
    # msg_box.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    msg_box.setStyleSheet(
        'background-color: rgb(30, 30, 30);'
        f'color: {MainBase.font_color_info};'
        f'font: {MainBase.font_size_dialog}\"Lexend Light\";'
        'QDialogButtonBox {'
        'border: 10px solid;'
        'border-color: #FFFFFF;}')

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
    from main_base import MainBase

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
    from d__progress_bar import UiProgressBar

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
