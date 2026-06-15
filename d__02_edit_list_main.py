import json.decoder

from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont, QIcon, )
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QListWidget, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QInputDialog)
from pathlib import Path
import os
import dop_win_rc
from ui_helpers import msg_one_button, msg_two_button
from d__02_1_edit_item import ListBackupItemEdit
from main_base import MainBase
from all_styles import SETTINGS_MAIN
import backup_lists


class EditListMain(object):
    def __init__(self):
        self.list_of_backup_lists: list = []
        self.backup_list_path = Path(f"{MainBase.path_settings_folder}\\backup_lists")

    def setupUi(self, Dialog):

        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 400))
        Dialog.setMaximumSize(QSize(400, 600))
        Dialog.setStyleSheet(SETTINGS_MAIN)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.info.setFont(font)
        self.info.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info)

        self.backup_lists = QListWidget(Dialog)
        self.backup_lists.setObjectName(u"backup_lists")
        self.backup_lists.setMinimumSize(QSize(0, 200))
        self.backup_lists.setStyleSheet(u"background-color: rgb(50, 50,50);\n"
                                        "color: rgb(230, 230, 230);\n"
                                        "font: 300 16pt \"Lexend Light\";")

        self.verticalLayout.addWidget(self.backup_lists)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QSize(180, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon)
        self.ok.setIconSize(QSize(50, 50))

        self.rename_bt = QPushButton(Dialog)
        self.rename_bt.setObjectName(u"rename_bt")
        self.rename_bt.setMinimumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.rename_bt)

        self.delete_bt = QPushButton(Dialog)
        self.delete_bt.setObjectName(u"delete_bt")
        self.delete_bt.setMinimumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.delete_bt)

        self.horizontalLayout.addWidget(self.ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        # ************************  MY CODE  *******************************************************

        self.refresh()

        # ------------------------------------------------------------------------------------------

        # ************************  MY CODE (buttons)  *********************************************
        self.backup_lists.clicked.connect(self.edit_item_bt)
        self.rename_bt.clicked.connect(self.rename_bt_clicked)
        self.delete_bt.clicked.connect(self.delete_bt_clicked)

        self.ok.clicked.connect(Dialog.reject)
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Add Item to Backup List", None))
        self.info.setText(QCoreApplication.translate("Dialog",
                                                     u"Please select the backup list you would like to edit",
                                                     None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"Main Menu", None))
        self.rename_bt.setText(QCoreApplication.translate("Dialog", u"Rename", None))
        self.delete_bt.setText(QCoreApplication.translate("Dialog", u"Delete", None))

    # ************************    MY CODE    ***************************************************
    def edit_item_bt(self):
        """
        When clicked on line in list, run dialog for edit this item
        """
        row = self.backup_lists.currentRow()
        path = f"{self.backup_list_path}\\{self.list_of_backup_lists[row]}"
        try:
            backup_items: dict = MainBase.load_base_from_disk(path)
            dialog = QDialog()
            ui = ListBackupItemEdit()
            ui.setupUi(dialog, backup_items)
            dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
            dialog.exec()
        except json.decoder.JSONDecodeError:
            msg_one_button("Warning!", "Backup lists file is empty!", "warn")
            return



    def del_row(self):
        """
        Add/Remove row from opened backup list
        """
        row = self.backup_lists.currentRow()
        reply = msg_two_button("Remove Item", "Do You Want to Remove Item?")
        if reply == 'yes':
            print(row, "TEST****************************")
            self.backup_lists.takeItem(row)

        else:
            return
        #     self.list_of_file.remove(removed_row.text())

    def refresh(self):
        """Reload the list widget from disk."""
        base_dir = MainBase.backup_lists_dir()
        self.list_of_backup_lists = backup_lists.list_names(base_dir)
        self.backup_lists.clear()
        self.backup_lists.addItems(self.list_of_backup_lists)

    def _selected_name(self):
        row = self.backup_lists.currentRow()
        if row < 0:
            return None
        return self.list_of_backup_lists[row]

    def delete_bt_clicked(self):
        name = self._selected_name()
        if name is None:
            return
        if msg_two_button("Delete list",
                          f"Delete the backup list '{name}'?") != 'yes':
            return
        base_dir = MainBase.backup_lists_dir()
        if backup_lists.list_exists(base_dir, name):
            backup_lists.delete_list(base_dir, name)
        self.refresh()

    def rename_bt_clicked(self):
        name = self._selected_name()
        if name is None:
            return
        new_name, ok = QInputDialog.getText(None, "Rename list",
                                            f"New name for '{name}':")
        if ok:
            self.do_rename(name, new_name)

    def do_rename(self, old_name, new_name):
        new_name = (new_name or "").strip()
        base_dir = MainBase.backup_lists_dir()
        if not backup_lists.valid_list_name(new_name):
            msg_one_button("Invalid name",
                           "Please enter a valid list name "
                           "(no \\ / : * ? \" < > | characters).", "warn")
            return
        if backup_lists.list_exists(base_dir, new_name):
            msg_one_button("Name taken",
                           f"A backup list named '{new_name}' already exists.",
                           "warn")
            return
        backup_lists.rename_list(base_dir, old_name, new_name)
        self.refresh()
