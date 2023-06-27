# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_progress_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QProgressBar, QSizePolicy, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(492, 113)
        Form.setStyleSheet(u"*{\n"
                           "background-color: rgb(30, 30, 30);\n"
                           "font: 16pt \"Lexend Light\";\n"
                           "border: 1px solid;\n"
                           "border-color: #2B79C2;\n"
                           "color: rgb(230, 230, 230)}\n"
                           "QLabel{\n"
                           "font: 12pt \"Lexend Light\";\n"
                           "color: #2B79C2;\n"
                           "border: no}\n"
                           "QLineEdit{\n"
                           "background-color: rgb(30, 30, 30);}\n"
                           "QLineEdit:disabled{\n"
                           "background-color: rgb(50,50,50);}\n"
                           "QFrame{\n"
                           "border-color: #2B79C2;}")
        self.progress_bar_line = QProgressBar(Form)
        self.progress_bar_line.setObjectName(u"progress_bar_line")
        self.progress_bar_line.setGeometry(QRect(20, 50, 451, 50))
        self.progress_bar_line.setMinimumSize(QSize(0, 50))
        self.progress_bar_line.setMaximumSize(QSize(16777215, 50))
        self.progress_bar_line.setValue(24)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi
