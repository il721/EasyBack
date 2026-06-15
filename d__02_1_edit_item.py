from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont, QIcon, )
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QListWidget, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)
import dop_win_rc
from main_base import MainBase
from ui_helpers import msg_one_button, msg_two_button
import backup_lists


class ListBackupItemEdit(object):
    def setupUi(self, Dialog, items, name):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        self.dialog = Dialog
        self.items = items          # working copy of this list's items
        self.name = name            # list (file) name to save back to
        self.base_dir = MainBase.backup_lists_dir()
        Dialog.resize(400, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 800))
        Dialog.setMaximumSize(QSize(400, 800))
        Dialog.setStyleSheet(u"*{\n"
                             "background-color: rgb(30, 30, 30);\n"
                             "font: 16pt \"Lexend Light\";\n"
                             "border: 1px solid;\n"
                             "color: rgb(230, 230, 230);\n"
                             "border-color: #2B79C2;\n"
                             "}\n"
                             "QLabel{\n"
                             "font: 12pt \"Lexend Light\";\n"
                             "color: #2B79C2;\n"
                             "border: no\n"
                             "}\n"
                             "QLineEdit{\n"
                             "background-color: rgb(30, 30, 30);\n"
                             "}\n"
                             "\n"
                             "QPushButton {\n"
                             "border: 2px solid;\n"
                             "color: rgb(230, 230, 230);\n"
                             "border-color: rgb(110, 110, 110);\n"
                             "border-radius: 15px;\n"
                             "background-color: rgba(60,60, 60, 80);\n"
                             "}\n"
                             "\n"
                             "QPushButton:hover {\n"
                             "color: #2B79C2;\n"
                             "border: 3px solid;\n"
                             "background-color: rgba(30, 30, 30, 180);\n"
                             "border-color: rgb(150,150, 150);\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "color: rgb(30, 30, 30);\n"
                             "border: 2px solid;\n"
                             "background-color: #2B79C2;\n"
                             "border-color: rgb(230, 230, 230);\n"
                             "}\n"
                             "QRadioButton {\n"
                             "border: no\n"
                             "}")
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

        self.backup_items = QListWidget(Dialog)
        self.backup_items.setObjectName(u"backup_lists")
        self.backup_items.setMinimumSize(QSize(0, 480))
        self.backup_items.setStyleSheet(u"background-color: rgb(50, 50,50);\n"
                                        "color: rgb(230, 230, 230);\n"
                                        "font: 300 16pt \"Lexend Light\";")

        self.verticalLayout.addWidget(self.backup_items)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)
        self.ok.setMinimumSize(QSize(130, 60))
        self.ok.setMaximumSize(QSize(130, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon)
        self.ok.setIconSize(QSize(50, 50))

        self.del_item = QPushButton(Dialog)
        self.del_item.setObjectName(u"del_item")
        self.del_item.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.del_item)

        self.add_item = QPushButton(Dialog)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.add_item)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.save)

        self.horizontalLayout.addWidget(self.ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        # ************************  MY CODE  *******************************************************

        # ------------------------------------------------------------------------------------------

        # ************************  MY CODE (buttons)  *********************************************

        self.ok.clicked.connect(Dialog.reject)
        self.del_item.clicked.connect(self.del_item_bt)
        self.add_item.clicked.connect(self.add_item_bt)
        self.save.clicked.connect(self.save_bt)
        self._refresh_items()
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Add Item to Backup List", None))
        self.info.setText(
            QCoreApplication.translate("Dialog", u"Please select item you would like to edit",
                                       None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"  back", None))
        self.del_item.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.add_item.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))

    # ************************  MY CODE  *******************************************************
    def _refresh_items(self):
        self.backup_items.clear()
        self.backup_items.addItems(list(self.items))

    def del_item_bt(self):
        row = self.backup_items.currentRow()
        if row < 0:
            return
        key = self.backup_items.currentItem().text()
        if msg_two_button("Delete item",
                          f"Remove '{key}' from this list?") != 'yes':
            return
        self.items.pop(key, None)
        self._refresh_items()

    def add_item_bt(self):
        # Local import avoids a load-time import cycle with d__01_add_item.
        from d__01_add_item import AddItemDial01
        from PySide6.QtWidgets import QDialog
        dialog = QDialog()
        ui = AddItemDial01(target=self.items)   # add into THIS list's copy
        ui.setupUi(dialog)
        dialog.exec()
        self._refresh_items()

    def save_bt(self):
        backup_lists.save_list(self.base_dir, self.name, self.items)
        msg_one_button("Saved", f"Backup list '{self.name}' saved", "info")
        self.dialog.accept()


