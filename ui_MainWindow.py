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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import main_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMaximumSize(QSize(600, 800))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 21, 106, 255), stop:1 rgba(0, 14, 13, 255));\n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 800))
        self.centralwidget.setMaximumSize(QSize(600, 800))
        self.centralwidget.setStyleSheet(u"")
        self.backup_all = QPushButton(self.centralwidget)
        self.backup_all.setObjectName(u"backup_all")
        self.backup_all.setEnabled(True)
        self.backup_all.setGeometry(QRect(20, 340, 559, 90))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_all.sizePolicy().hasHeightForWidth())
        self.backup_all.setSizePolicy(sizePolicy)
        self.backup_all.setMinimumSize(QSize(559, 90))
        self.backup_all.setMaximumSize(QSize(559, 45))
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.backup_all.setFont(font)
        self.backup_all.setLayoutDirection(Qt.LeftToRight)
        self.backup_all.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/safe_in_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backup_all.setIcon(icon)
        self.backup_all.setIconSize(QSize(115, 115))
        self.add_item = QPushButton(self.centralwidget)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setEnabled(True)
        self.add_item.setGeometry(QRect(20, 60, 559, 90))
        sizePolicy.setHeightForWidth(self.add_item.sizePolicy().hasHeightForWidth())
        self.add_item.setSizePolicy(sizePolicy)
        self.add_item.setMinimumSize(QSize(559, 90))
        self.add_item.setMaximumSize(QSize(559, 45))
        self.add_item.setFont(font)
        self.add_item.setLayoutDirection(Qt.LeftToRight)
        self.add_item.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add_item.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon1)
        self.add_item.setIconSize(QSize(80, 80))
        self.remove_item = QPushButton(self.centralwidget)
        self.remove_item.setObjectName(u"remove_item")
        self.remove_item.setEnabled(True)
        self.remove_item.setGeometry(QRect(20, 210, 559, 90))
        sizePolicy.setHeightForWidth(self.remove_item.sizePolicy().hasHeightForWidth())
        self.remove_item.setSizePolicy(sizePolicy)
        self.remove_item.setMinimumSize(QSize(559, 90))
        self.remove_item.setMaximumSize(QSize(559, 45))
        self.remove_item.setFont(font)
        self.remove_item.setLayoutDirection(Qt.LeftToRight)
        self.remove_item.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/remove_item.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_item.setIcon(icon2)
        self.remove_item.setIconSize(QSize(72, 72))
        self.restore_all = QPushButton(self.centralwidget)
        self.restore_all.setObjectName(u"restore_all")
        self.restore_all.setEnabled(True)
        self.restore_all.setGeometry(QRect(20, 470, 559, 90))
        sizePolicy.setHeightForWidth(self.restore_all.sizePolicy().hasHeightForWidth())
        self.restore_all.setSizePolicy(sizePolicy)
        self.restore_all.setMinimumSize(QSize(559, 90))
        self.restore_all.setMaximumSize(QSize(559, 45))
        self.restore_all.setFont(font)
        self.restore_all.setLayoutDirection(Qt.LeftToRight)
        self.restore_all.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/restore_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_all.setIcon(icon3)
        self.restore_all.setIconSize(QSize(110, 110))
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(50, 620, 260, 70))
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QSize(260, 70))
        self.settings.setMaximumSize(QSize(260, 70))
        font1 = QFont()
        font1.setFamilies([u"Lexend Light"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.settings.setFont(font1)
        self.settings.setLayoutDirection(Qt.LeftToRight)
        self.settings.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.settings.setIconSize(QSize(42, 42))
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setEnabled(True)
        self.exit.setGeometry(QRect(320, 620, 260, 70))
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(260, 70))
        self.exit.setMaximumSize(QSize(260, 70))
        self.exit.setFont(font1)
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.exit.setIconSize(QSize(42, 42))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backup_all.setText(QCoreApplication.translate("MainWindow", u"                        Back Up All", None))
        self.add_item.setText(QCoreApplication.translate("MainWindow", u"                    Add Item To Base", None))
        self.remove_item.setText(QCoreApplication.translate("MainWindow", u"        Remove Item From Base", None))
        self.restore_all.setText(QCoreApplication.translate("MainWindow", u"                          Restore All", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

