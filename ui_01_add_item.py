# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_01_add_item.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
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
"}\n"
"\n"
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
"")
        self.verticalLayout = QVBoxLayout(Dialog)
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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.edit_list = QPushButton(Dialog)
        self.edit_list.setObjectName(u"edit_list")
        sizePolicy.setHeightForWidth(self.edit_list.sizePolicy().hasHeightForWidth())
        self.edit_list.setSizePolicy(sizePolicy)
        self.edit_list.setMinimumSize(QSize(180, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/edit_list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_list.setIcon(icon2)
        self.edit_list.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.edit_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.list_files_and_folders = QListWidget(Dialog)
        self.list_files_and_folders.setObjectName(u"list_files_and_folders")
        self.list_files_and_folders.setStyleSheet(u"background-color: rgb(50, 50,50);\n"
"color: rgb(10,10,10);\n"
"font: 300 12pt \"Lexend Light\";")

        self.verticalLayout.addWidget(self.list_files_and_folders)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setMinimumSize(QSize(170, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/GREY/cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel.setIcon(icon4)
        self.cancel.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_folder.setText(QCoreApplication.translate("Dialog", u"  Add Folder", None))
        self.add_file.setText(QCoreApplication.translate("Dialog", u"    Add File", None))
        self.edit_list.setText(QCoreApplication.translate("Dialog", u"    Edit List", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"  Ok", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"  Cancel", None))
    # retranslateUi

