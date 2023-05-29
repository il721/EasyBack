from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, )
from PySide6.QtGui import (QIcon, )
from PySide6.QtWidgets import (QFileDialog, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout, )
import dop_win_rc
from main_base import MainBase


class settings_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(600, 540))
        Dialog.setMaximumSize(QSize(600, 540))
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
                             "QFrame{\n"
                             "border-color: #2B79C2;\n"
                             "}\n"
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
                             "QRadioButton{\n"
                             "font: 14pt \"Lexend Light\";\n"
                             "border: no\n"
                             "}\n"
                             "QToolButton{\n"
                             "image: url(:/icon/icons/GREY/info_invert.svg);\n"
                             "border: no\n"
                             "}\n"
                             "QToolB"
                             "utton:hover {\n"
                             "image: url(:/icon/icons/GREY/info.svg);\n"
                             "border: no\n"
                             "}\n"
                             "QToolButton:pressed{\n"
                             "image: url(:/icon/icons/GREY/info_invert.svg);\n"
                             "border: no\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox = QFrame(Dialog)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setMinimumSize(QSize(0, 125))
        self.checkbox.setStyleSheet(u"")
        self.label_info_subfolders = QLabel(self.checkbox)
        self.label_info_subfolders.setObjectName(u"label_info_subfolders")
        self.label_info_subfolders.setGeometry(QRect(10, 10, 541, 16))
        self.label_info_subfolders.setStyleSheet(u"")
        self.default_folder_rad = QRadioButton(self.checkbox)
        self.default_folder_rad.setObjectName(u"default_folder_rad")
        self.default_folder_rad.setGeometry(QRect(11, 36, 385, 24))
        self.default_folder_rad.setStyleSheet(u"")
        self.default_folder_rad.setChecked(True)
        self.default_info = QToolButton(self.checkbox)
        self.default_info.setObjectName(u"default_info")
        self.default_info.setGeometry(QRect(450, 40, 25, 25))
        self.default_info.setStyleSheet(u"")
        self.default_info.setIconSize(QSize(10, 10))
        self.select_folders = QRadioButton(self.checkbox)
        self.select_folders.setObjectName(u"select_folders")
        self.select_folders.setGeometry(QRect(11, 80, 386, 24))
        self.select_folders.setStyleSheet(u"")
        self.select_folders.setChecked(False)
        self.select_info = QToolButton(self.checkbox)
        self.select_info.setObjectName(u"select_info")
        self.select_info.setGeometry(QRect(450, 80, 25, 25))
        self.select_info.setStyleSheet(u"")
        self.select_info.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.checkbox)

        self.sel_main_folder = QPushButton(Dialog)
        self.sel_main_folder.setObjectName(u"sel_main_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sel_main_folder.sizePolicy().hasHeightForWidth())
        self.sel_main_folder.setSizePolicy(sizePolicy1)
        self.sel_main_folder.setMinimumSize(QSize(220, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sel_main_folder.setIcon(icon)
        self.sel_main_folder.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.sel_main_folder)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 160))
        self.frame.setMaximumSize(QSize(16777215, 160))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sett_text = QLabel(self.frame)
        self.sett_text.setObjectName(u"sett_text")
        self.sett_text.setMinimumSize(QSize(85, 30))
        self.sett_text.setMaximumSize(QSize(16777215, 30))
        self.sett_text.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.sett_text)

        self.sett_folder = QLineEdit(self.frame)
        self.sett_folder.setObjectName(u"sett_folder")
        self.sett_folder.setMinimumSize(QSize(465, 0))
        self.sett_folder.setMaximumSize(QSize(460, 16777215))

        self.horizontalLayout_2.addWidget(self.sett_folder)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sett_text_2 = QLabel(self.frame)
        self.sett_text_2.setObjectName(u"sett_text_2")
        self.sett_text_2.setMinimumSize(QSize(85, 30))
        self.sett_text_2.setMaximumSize(QSize(16777215, 30))
        self.sett_text_2.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.sett_text_2)

        self.sett_folder_2 = QLineEdit(self.frame)
        self.sett_folder_2.setObjectName(u"sett_folder_2")
        self.sett_folder_2.setMinimumSize(QSize(465, 0))
        self.sett_folder_2.setMaximumSize(QSize(460, 16777215))

        self.horizontalLayout_3.addWidget(self.sett_folder_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.settings_folder = QPushButton(self.frame)
        self.settings_folder.setObjectName(u"settings_folder")
        sizePolicy.setHeightForWidth(self.settings_folder.sizePolicy().hasHeightForWidth())
        self.settings_folder.setSizePolicy(sizePolicy)
        self.settings_folder.setMinimumSize(QSize(0, 50))
        self.settings_folder.setMaximumSize(QSize(280, 50))

        self.horizontalLayout_4.addWidget(self.settings_folder)

        self.data_folder = QPushButton(self.frame)
        self.data_folder.setObjectName(u"data_folder")
        sizePolicy.setHeightForWidth(self.data_folder.sizePolicy().hasHeightForWidth())
        self.data_folder.setSizePolicy(sizePolicy)
        self.data_folder.setMinimumSize(QSize(280, 50))
        self.data_folder.setMaximumSize(QSize(280, 50))

        self.horizontalLayout_4.addWidget(self.data_folder)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_settings = QPushButton(Dialog)
        self.save_settings.setObjectName(u"save_settings")
        sizePolicy1.setHeightForWidth(self.save_settings.sizePolicy().hasHeightForWidth())
        self.save_settings.setSizePolicy(sizePolicy1)
        self.save_settings.setMinimumSize(QSize(220, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/GREY/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_settings.setIcon(icon1)
        self.save_settings.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.save_settings)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_settings = QPushButton(Dialog)
        self.main_settings.setObjectName(u"main_settings")
        sizePolicy1.setHeightForWidth(self.main_settings.sizePolicy().hasHeightForWidth())
        self.main_settings.setSizePolicy(sizePolicy1)
        self.main_settings.setMinimumSize(QSize(220, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.main_settings.setIcon(icon2)
        self.main_settings.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.main_settings)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        # ************************  MY CODE (buttons)  *********************************************
        self.sel_main_folder.clicked.connect(self.sel_main_folder_bt)
        self.save_settings.clicked.connect(self.save_settings_bt)
        self.main_settings.clicked.connect(Dialog.reject)
        # ------------------------------------------------------------------------------------------

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_info_subfolders.setText(QCoreApplication.translate("Dialog",
                                                                      u"Select what backup subfolders you want to create:",
                                                                      None))
        # if QT_CONFIG(tooltip)
        self.default_folder_rad.setToolTip(QCoreApplication.translate("Dialog",
                                                                      u"\"SETTINGS\" and \"DATA\" was create automaticly in Main Folder",
                                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.default_folder_rad.setText(
            QCoreApplication.translate("Dialog", u"Default (Select only Main Backup Folder)", None))
        # if QT_CONFIG(tooltip)
        self.select_folders.setToolTip(QCoreApplication.translate("Dialog",
                                                                  u"\"SETTINGS\" and \"DATA\" was create automaticly in Main Folder",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.select_folders.setText(
            QCoreApplication.translate("Dialog", u"I want to select existing Folders manualy",
                                       None))
        self.sel_main_folder.setText(
            QCoreApplication.translate("Dialog", u"    Select Main Backup Folder", None))
        self.sett_text.setText(QCoreApplication.translate("Dialog", u"SETTINGS:", None))
        self.sett_text_2.setText(QCoreApplication.translate("Dialog", u"DATA:", None))
        self.settings_folder.setText(
            QCoreApplication.translate("Dialog", u"Select \"SETTINGS\" Folder", None))
        self.data_folder.setText(
            QCoreApplication.translate("Dialog", u"Select \"DATA\" Folder", None))
        self.save_settings.setText(QCoreApplication.translate("Dialog", u"   Save Settings", None))
        self.main_settings.setText(QCoreApplication.translate("Dialog", u"   Main Menu", None))

    # retranslateUi

    # ************************    MY CODE    ***************************************************
    @staticmethod
    def sel_main_folder_bt():
        dialog = QFileDialog()
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                MainBase.path_of_main_folder = "".join(filenames)
                print(MainBase.path_of_main_folder)
                # TODO Add "create default folders" check button

    @staticmethod
    def save_settings_bt():
        MainBase.save_settings()
