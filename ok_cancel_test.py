# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ok_cancel_test.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 800)
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
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 721, 500, 60))
        self.buttonBox.setMaximumSize(QSize(16777188, 16777215))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

