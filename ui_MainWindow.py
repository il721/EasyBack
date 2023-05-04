# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.out = QLabel(self.centralwidget)
        self.out.setObjectName(u"out")
        self.out.setGeometry(QRect(20, 20, 360, 75))
        self.out.setStyleSheet(u"background-color: rgb(32, 28, 139);\n"
"font: 20pt \"Segoe UI\";\n"
"color: rgb(209, 209, 209);")
        self.out.setScaledContents(False)
        self.dir = QPushButton(self.centralwidget)
        self.dir.setObjectName(u"dir")
        self.dir.setEnabled(True)
        self.dir.setGeometry(QRect(20, 140, 361, 71))
        self.files = QPushButton(self.centralwidget)
        self.files.setObjectName(u"files")
        self.files.setGeometry(QRect(20, 230, 361, 71))
        self.test = QPushButton(self.centralwidget)
        self.test.setObjectName(u"test")
        self.test.setGeometry(QRect(110, 360, 221, 41))
        self.test.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"\n"
"background-color: rgb(156, 104, 0);")
        self.test.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.out.setText("")
        self.dir.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.files.setText(QCoreApplication.translate("MainWindow", u"files", None))
        self.test.setText(QCoreApplication.translate("MainWindow", u"test", None))
    # retranslateUi

