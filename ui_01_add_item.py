# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_01_add_item.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import dop_win_rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 800)
        Dialog.setMaximumSize(QSize(600, 800))
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

        self.checkbox = QFrame(Dialog)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setStyleSheet(u"border-color: #2B79C2;")
        self.verticalLayout_2 = QVBoxLayout(self.checkbox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.checkbox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.settings_radio = QRadioButton(self.checkbox)
        self.settings_radio.setObjectName(u"settings_radio")
        self.settings_radio.setChecked(True)

        self.verticalLayout_2.addWidget(self.settings_radio)

        self.data_radio = QRadioButton(self.checkbox)
        self.data_radio.setObjectName(u"data_radio")

        self.verticalLayout_2.addWidget(self.data_radio)


        self.verticalLayout.addWidget(self.checkbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.view_list = QPushButton(Dialog)
        self.view_list.setObjectName(u"view_list")
        sizePolicy.setHeightForWidth(self.view_list.sizePolicy().hasHeightForWidth())
        self.view_list.setSizePolicy(sizePolicy)
        self.view_list.setMinimumSize(QSize(180, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_list.setIcon(icon2)
        self.view_list.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.view_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        font1 = QFont()
        font1.setFamilies([u"Lexend Light"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"")

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
        self.add_item.setMinimumSize(QSize(180, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/GREY/gr_add_item.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon3)
        self.add_item.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.add_item)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_backup_list = QPushButton(Dialog)
        self.save_backup_list.setObjectName(u"save_backup_list")
        sizePolicy.setHeightForWidth(self.save_backup_list.sizePolicy().hasHeightForWidth())
        self.save_backup_list.setSizePolicy(sizePolicy)
        self.save_backup_list.setMinimumSize(QSize(180, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/GREY/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_backup_list.setIcon(icon4)
        self.save_backup_list.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.save_backup_list)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QSize(180, 60))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon5)
        self.ok.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Item to Backup List", None))
        self.input_name.setText("")
        self.input_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Input name of backup item here", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Please, select backup item type (by default you item has SETTINS type):", None))
#if QT_CONFIG(tooltip)
        self.settings_radio.setToolTip(QCoreApplication.translate("Dialog", u"Select this if you want to backup programm settings like MS Word, Adobe Photoshop etc.", None))
#endif // QT_CONFIG(tooltip)
        self.settings_radio.setText(QCoreApplication.translate("Dialog", u"SETTINGS Backup", None))
#if QT_CONFIG(tooltip)
        self.data_radio.setToolTip(QCoreApplication.translate("Dialog", u"Select this if you want to backup some personal data like MyWork, Foto, Doc`s etc.", None))
#endif // QT_CONFIG(tooltip)
        self.data_radio.setText(QCoreApplication.translate("Dialog", u"DATA Backup", None))
        self.add_folder.setText(QCoreApplication.translate("Dialog", u" Add Folder", None))
        self.add_file.setText(QCoreApplication.translate("Dialog", u"   Add Files", None))
        self.view_list.setText(QCoreApplication.translate("Dialog", u"   View All", None))
        self.info.setText(QCoreApplication.translate("Dialog", u"To remove line from list below just select them", None))
        self.add_item.setText(QCoreApplication.translate("Dialog", u"   Add Item", None))
        self.save_backup_list.setText(QCoreApplication.translate("Dialog", u"   Save List", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"Main Menu", None))
    # retranslateUi

