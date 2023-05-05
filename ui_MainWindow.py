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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMaximumSize(QSize(600, 800))
        MainWindow.setWindowOpacity(0.900000000000000)
        MainWindow.setStyleSheet(u"*{\n"
"	background-image: url(:/images/images/bg_Main.png);\n"
"}\n"
"\n"
"centralwidget {\n"
"	background-image: url(:/images/images/bg_Main.png);\n"
"}\n"
"QPushBatton {\n"
"	background-color: rgb(0, 13, 40);\n"
"	border-color: rgb(0, 36, 109);\n"
"}\n"
"QPushBatton:hover {\n"
"	background-color: rgb(63, 121, 197);\n"
"	border-color: rgb(0, 36, 109);\n"
"}\n"
"QPushBatton:pressed {\n"
"	background-color: rgb(100,100,100);\n"
"	border-color: rgb(0, 36, 109);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 0, 561, 763))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dir = QPushButton(self.widget)
        self.dir.setObjectName(u"dir")
        self.dir.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir.sizePolicy().hasHeightForWidth())
        self.dir.setSizePolicy(sizePolicy)
        self.dir.setMinimumSize(QSize(559, 90))
        self.dir.setMaximumSize(QSize(559, 45))
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.dir.setFont(font)
        self.dir.setLayoutDirection(Qt.LeftToRight)
        self.dir.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir)

        self.dir_2 = QPushButton(self.widget)
        self.dir_2.setObjectName(u"dir_2")
        self.dir_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dir_2.sizePolicy().hasHeightForWidth())
        self.dir_2.setSizePolicy(sizePolicy)
        self.dir_2.setMinimumSize(QSize(559, 90))
        self.dir_2.setMaximumSize(QSize(559, 45))
        self.dir_2.setFont(font)
        self.dir_2.setLayoutDirection(Qt.LeftToRight)
        self.dir_2.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir_2.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir_2)

        self.dir_3 = QPushButton(self.widget)
        self.dir_3.setObjectName(u"dir_3")
        self.dir_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dir_3.sizePolicy().hasHeightForWidth())
        self.dir_3.setSizePolicy(sizePolicy)
        self.dir_3.setMinimumSize(QSize(559, 90))
        self.dir_3.setMaximumSize(QSize(559, 45))
        self.dir_3.setFont(font)
        self.dir_3.setLayoutDirection(Qt.LeftToRight)
        self.dir_3.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir_3.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir_3)

        self.dir_4 = QPushButton(self.widget)
        self.dir_4.setObjectName(u"dir_4")
        self.dir_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dir_4.sizePolicy().hasHeightForWidth())
        self.dir_4.setSizePolicy(sizePolicy)
        self.dir_4.setMinimumSize(QSize(559, 90))
        self.dir_4.setMaximumSize(QSize(559, 45))
        self.dir_4.setFont(font)
        self.dir_4.setLayoutDirection(Qt.LeftToRight)
        self.dir_4.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir_4.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir_4)

        self.dir_5 = QPushButton(self.widget)
        self.dir_5.setObjectName(u"dir_5")
        self.dir_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dir_5.sizePolicy().hasHeightForWidth())
        self.dir_5.setSizePolicy(sizePolicy)
        self.dir_5.setMinimumSize(QSize(559, 90))
        self.dir_5.setMaximumSize(QSize(559, 45))
        self.dir_5.setFont(font)
        self.dir_5.setLayoutDirection(Qt.LeftToRight)
        self.dir_5.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir_5.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir_5)

        self.dir_6 = QPushButton(self.widget)
        self.dir_6.setObjectName(u"dir_6")
        self.dir_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dir_6.sizePolicy().hasHeightForWidth())
        self.dir_6.setSizePolicy(sizePolicy)
        self.dir_6.setMinimumSize(QSize(559, 90))
        self.dir_6.setMaximumSize(QSize(559, 45))
        self.dir_6.setFont(font)
        self.dir_6.setLayoutDirection(Qt.LeftToRight)
        self.dir_6.setStyleSheet(u"border: 2px solid rgb(0, 36, 109);\n"
"color: rgb(69, 246, 255);\n"
"\n"
"background-color: rgb(0, 13, 40);\n"
"border-color: rgb(0, 36, 109);\n"
"border-radius: 20px;")
        self.dir_6.setIconSize(QSize(42, 42))

        self.verticalLayout.addWidget(self.dir_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
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

        self.horizontalLayout.addWidget(self.settings)

        self.exit = QPushButton(self.widget)
        self.exit.setObjectName(u"exit")
        self.exit.setEnabled(True)
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

        self.horizontalLayout.addWidget(self.exit)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.dir.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.dir_2.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.dir_3.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.dir_4.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.dir_5.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.dir_6.setText(QCoreApplication.translate("MainWindow", u"ADD ITEM TO BASE", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

