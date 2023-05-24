from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, )
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QDialogButtonBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit,
                               QListWidget, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QMessageBox, )
import dop_win_rc


class AddItemDial01(object):
    def __init__(self):
        self.all_backup_item: dict = {"q": ["zsdxg"]}  # TODO !!!!! DON`T REMEMBER MAKE {}
        self.backup_item_list: list = []
        self.name_item: str = ""

    def setupUi_(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Add Item")
        Dialog.resize(600, 800)
        Dialog.setMaximumSize(QSize(600, 800))
        Dialog.setStyleSheet(u"*{\n"
                             "background-color: rgb(30, 30, 30);\n"
                             "font: 16pt \"Lexend Light\";\n"
                             "border: 2px solid;\n"
                             "color: rgb(230, 230, 230);\n"
                             "border-color: rgb(110, 110, 110);\n"
                             "}\n"
                             "\n"
                             "QLineEdit{\n"
                             "background-color: rgb(30, 30, 30);\n"
                             "}\n"
                             "\n"
                             "QPushButton {\n"
                             "border: 2px solid;\n"
                             "color: rgb(230, 230, 230);\n"
                             "border-color: rgb(110, 110, 110);\n"
                             "border-radius: 20px;\n"
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
                             "QMessageBox {\n"
                             "border: no\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_folder = QPushButton(Dialog)
        self.add_folder.setObjectName(u"add_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_folder.sizePolicy().hasHeightForWidth())
        self.add_folder.setSizePolicy(sizePolicy)
        self.add_folder.setMinimumSize(QSize(180, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_folder.setIcon(icon)
        self.add_folder.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.add_folder)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.add_file = QPushButton(Dialog)
        self.add_file.setObjectName(u"add_file")
        sizePolicy.setHeightForWidth(self.add_file.sizePolicy().hasHeightForWidth())
        self.add_file.setSizePolicy(sizePolicy)
        self.add_file.setMinimumSize(QSize(180, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/GREY/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_file.setIcon(icon1)
        self.add_file.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.add_file)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.input_name = QLineEdit(Dialog)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setMinimumSize(QSize(0, 40))
        self.input_name.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.input_name.setFont(font)
        self.input_name.setStyleSheet(u"color: rgb(202, 202, 202);\n"
                                      "border-color: #2B79C2;\n"
                                      "")

        self.verticalLayout.addWidget(self.input_name)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        self.info.setStyleSheet(u"color: rgb(255, 255, 127);\n"
                                "border: no")

        self.verticalLayout.addWidget(self.info)

        self.list_files_and_folders = QListWidget(Dialog)
        self.list_files_and_folders.setObjectName(u"list_files_and_folders")
        self.list_files_and_folders.setMinimumSize(QSize(0, 480))
        self.list_files_and_folders.setStyleSheet(u"background-color: rgb(50, 50,50);\n"
                                                  "color: rgb(230, 230, 230);\n"
                                                  "font: 300 16pt \"Lexend Light\";")

        self.verticalLayout.addWidget(self.list_files_and_folders)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_item = QPushButton(Dialog)
        self.add_item.setObjectName(u"add_item")
        sizePolicy.setHeightForWidth(self.add_item.sizePolicy().hasHeightForWidth())
        self.add_item.setSizePolicy(sizePolicy)
        self.add_item.setMinimumSize(QSize(170, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/gr_add_item.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon2)
        self.add_item.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.add_item)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QSize(170, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/GREY/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon3)
        self.ok.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        # setupUi

        # ************************    MY CODE    ***************************************************
        # self.buttonBox = QDialogButtonBox(Dialog)
        # self.buttonBox.setObjectName(u"buttonBox")
        # self.buttonBox.addButton(self.ok, QDialogButtonBox.AcceptRole)
        # self.buttonBox.addButton(self.cancel, QDialogButtonBox.RejectRole)
        # ------------------------------------------------------------------------------------------
        # self.retranslateUi(Dialog)
        # ************************    MY CODE    ***************************************************
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)
        # ------------------------------------------------------------------------------------------

        # ************************  MY CODE (buttons)  *********************************************
        self.add_folder.clicked.connect(self.add_folder_bt)
        self.add_file.clicked.connect(self.add_file_bt)
        self.list_files_and_folders.clicked.connect(self.remove_line_bt)
        self.add_item.clicked.connect(self.add_item_01_bt)
        self.ok.clicked.connect(Dialog.reject)
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_folder.setText(QCoreApplication.translate("Dialog", u"  Add Folder", None))
        self.add_file.setText(QCoreApplication.translate("Dialog", u"    Add File", None))
        self.input_name.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"Input name of backup item here", None))
        self.info.setText(
            QCoreApplication.translate("Dialog", u"To remove line from list below just select them",
                                       None))
        self.add_item.setText(QCoreApplication.translate("Dialog", u"  Add Item", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"    Ok", None))

    # ************************    MY CODE    ***************************************************
    def add_folder_bt(self):
        """
        Add folder (only one in each time, when press "Add folder" button) to ListWidget and
        backup_list_item
        """
        dialog = QFileDialog()
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.backup_item_list.extend(filenames)
                self.list_files_and_folders.addItem(f"{' '.join(filenames)}")

    def add_file_bt(self):
        """
        Add file(`s) to ListWidget and backup_list_item when press "Add file" button
        """
        dialog = QFileDialog()
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            for _ in filenames:
                self.backup_item_list.append(_)
                self.list_files_and_folders.addItem(_)

    def remove_line_bt(self):
        """
        Remove line from ListWidget and backup_list_item whem it will be selected in ListWidget
        """
        row = self.list_files_and_folders.currentRow()

        # icon1 = QPixmap()
        # icon1.load(u":/icon/icons/GREY/info.svg")
        # QMessageBox.setIconPixmap(icon1)
        # self.add_file.setIconSize(QSize(35, 35))

        reply = QMessageBox.question(self.list_files_and_folders, "Remove Item",
                                     "Do You Want to Remove Item?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            removed_row = self.list_files_and_folders.takeItem(row)
            self.backup_item_list.remove(removed_row.text())
        # TODO chenge style of question message

    def add_item_01_bt(self):
        """
        Checking fields and if all of them is not emty - add new entry of backup item to
        main dict (all_backup_item):
        "name_item": [list_files_and_folders]
        If "name_item" is already exist in all_backup_item, open warning dialog and? if "ok"
        pressed, owerwrite key in dict
        """
        # TODO check all fields and open warning dialog if some of it was empty
        # TODO change style of wrning window
        self.name_item = self.input_name.text()
        if self.name_item in self.all_backup_item:
            reply = QMessageBox.question(self.list_files_and_folders, "WARNING!",
                                         "This name is already exist in base and wil be "
                                         "owerwrited if you press 'Ok'.\n Are you shure?",
                                         QMessageBox.StandardButton.Yes |
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.all_backup_item[self.name_item] = self.backup_item_list

        print(self.name_item)
        # print(self.backup_item_list)
        print(self.all_backup_item)
        # print(self.backup_item_list, sep="\n")
