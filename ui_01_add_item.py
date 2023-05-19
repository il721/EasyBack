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
from PySide6.QtWidgets import (QApplication, QListView, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 800)
        Form.setStyleSheet(u"*{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 21, 106, 255), stop:1 rgba(0, 14, 13, 255));\n"
"	font: 300 20pt \"Lexend Light\";\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"border: 2px solid;\n"
"color: rgb(230, 230, 115);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(69, 246, 255);\n"
"border: 3px solid;\n"
"background-color: rgba(4, 7, 208, 80);\n"
"border-color: rgb(0, 36, 109);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 2px solid;\n"
"background-color: rgba(4, 7, 208, 100);\n"
"border-color: rgb(170, 170 ,170);\n"
"}\n"
"\n"
"page {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 21, 106, 255), stop:1 rgba(0, 14, 13, 255));\n"
"}")
        self.list_files_and_folders = QListView(Form)
        self.list_files_and_folders.setObjectName(u"list_files_and_folders")
        self.list_files_and_folders.setGeometry(QRect(20, 171, 560, 491))
        self.list_files_and_folders.setStyleSheet(u"background-color: rgb(0, 0, 75);\n"
"color: rgb(227, 227, 227);\n"
"font: 300 12pt \"Lexend Light\";")
        self.ok = QPushButton(Form)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(120, 710, 150, 50))
        self.cancel = QPushButton(Form)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(360, 710, 150, 50))
        self.add_folder = QPushButton(Form)
        self.add_folder.setObjectName(u"add_folder")
        self.add_folder.setGeometry(QRect(20, 80, 271, 61))
        self.add_file = QPushButton(Form)
        self.add_file.setObjectName(u"add_file")
        self.add_file.setGeometry(QRect(310, 80, 271, 61))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"cancel", None))
        self.add_folder.setText(QCoreApplication.translate("Form", u"add folder", None))
        self.add_file.setText(QCoreApplication.translate("Form", u"add file", None))
    # retranslateUi

