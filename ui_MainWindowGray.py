# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainWindowGray.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMaximumSize(QSize(600, 800))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 800))
        self.centralwidget.setMaximumSize(QSize(600, 800))
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 13, 561, 753))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_item = QPushButton(self.widget)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_item.sizePolicy().hasHeightForWidth())
        self.add_item.setSizePolicy(sizePolicy)
        self.add_item.setMinimumSize(QSize(559, 90))
        self.add_item.setMaximumSize(QSize(559, 45))
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.add_item.setFont(font)
        self.add_item.setLayoutDirection(Qt.LeftToRight)
        self.add_item.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons_grey/icons/GREY/gr_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon)
        self.add_item.setIconSize(QSize(70, 70))

        self.verticalLayout.addWidget(self.add_item)

        self.remove_item = QPushButton(self.widget)
        self.remove_item.setObjectName(u"remove_item")
        self.remove_item.setEnabled(True)
        sizePolicy.setHeightForWidth(self.remove_item.sizePolicy().hasHeightForWidth())
        self.remove_item.setSizePolicy(sizePolicy)
        self.remove_item.setMinimumSize(QSize(559, 90))
        self.remove_item.setMaximumSize(QSize(559, 45))
        self.remove_item.setFont(font)
        self.remove_item.setLayoutDirection(Qt.LeftToRight)
        self.remove_item.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons_grey/icons/GREY/gr_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_item.setIcon(icon1)
        self.remove_item.setIconSize(QSize(70, 70))

        self.verticalLayout.addWidget(self.remove_item)

        self.backup_all = QPushButton(self.widget)
        self.backup_all.setObjectName(u"backup_all")
        self.backup_all.setEnabled(True)
        sizePolicy.setHeightForWidth(self.backup_all.sizePolicy().hasHeightForWidth())
        self.backup_all.setSizePolicy(sizePolicy)
        self.backup_all.setMinimumSize(QSize(559, 90))
        self.backup_all.setMaximumSize(QSize(559, 45))
        self.backup_all.setFont(font)
        self.backup_all.setLayoutDirection(Qt.LeftToRight)
        self.backup_all.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons_grey/icons/GREY/gr_back_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backup_all.setIcon(icon2)
        self.backup_all.setIconSize(QSize(110, 110))

        self.verticalLayout.addWidget(self.backup_all)

        self.backup_selected = QPushButton(self.widget)
        self.backup_selected.setObjectName(u"backup_selected")
        self.backup_selected.setEnabled(True)
        sizePolicy.setHeightForWidth(self.backup_selected.sizePolicy().hasHeightForWidth())
        self.backup_selected.setSizePolicy(sizePolicy)
        self.backup_selected.setMinimumSize(QSize(559, 90))
        self.backup_selected.setMaximumSize(QSize(559, 45))
        self.backup_selected.setFont(font)
        self.backup_selected.setLayoutDirection(Qt.LeftToRight)
        self.backup_selected.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons_grey/icons/GREY/gr_back_sel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backup_selected.setIcon(icon3)
        self.backup_selected.setIconSize(QSize(110, 110))

        self.verticalLayout.addWidget(self.backup_selected)

        self.restore_all = QPushButton(self.widget)
        self.restore_all.setObjectName(u"restore_all")
        self.restore_all.setEnabled(True)
        sizePolicy.setHeightForWidth(self.restore_all.sizePolicy().hasHeightForWidth())
        self.restore_all.setSizePolicy(sizePolicy)
        self.restore_all.setMinimumSize(QSize(559, 90))
        self.restore_all.setMaximumSize(QSize(559, 45))
        self.restore_all.setFont(font)
        self.restore_all.setLayoutDirection(Qt.LeftToRight)
        self.restore_all.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons_grey/icons/GREY/gr_rest_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_all.setIcon(icon4)
        self.restore_all.setIconSize(QSize(110, 110))

        self.verticalLayout.addWidget(self.restore_all)

        self.restore_selected = QPushButton(self.widget)
        self.restore_selected.setObjectName(u"restore_selected")
        self.restore_selected.setEnabled(True)
        sizePolicy.setHeightForWidth(self.restore_selected.sizePolicy().hasHeightForWidth())
        self.restore_selected.setSizePolicy(sizePolicy)
        self.restore_selected.setMinimumSize(QSize(559, 90))
        self.restore_selected.setMaximumSize(QSize(559, 45))
        self.restore_selected.setFont(font)
        self.restore_selected.setLayoutDirection(Qt.LeftToRight)
        self.restore_selected.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons_grey/icons/GREY/gr_rest_sel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_selected.setIcon(icon5)
        self.restore_selected.setIconSize(QSize(110, 110))

        self.verticalLayout.addWidget(self.restore_selected)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QSize(270, 80))
        self.settings.setMaximumSize(QSize(270, 80))
        font1 = QFont()
        font1.setFamilies([u"Lexend Light"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.settings.setFont(font1)
        self.settings.setLayoutDirection(Qt.LeftToRight)
        self.settings.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons_grey/icons/GREY/gr_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.settings)

        self.exit = QPushButton(self.widget)
        self.exit.setObjectName(u"exit")
        self.exit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(270, 80))
        self.exit.setMaximumSize(QSize(270, 80))
        self.exit.setFont(font1)
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons_grey/icons/GREY/gr_exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit.setIcon(icon7)
        self.exit.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.exit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_item.setText(QCoreApplication.translate("MainWindow", u"                    Add Item To Base", None))
        self.remove_item.setText(QCoreApplication.translate("MainWindow", u"        Remove Item From Base", None))
        self.backup_all.setText(QCoreApplication.translate("MainWindow", u"                        Back Up All", None))
        self.backup_selected.setText(QCoreApplication.translate("MainWindow", u"              Back Up Selected", None))
        self.restore_all.setText(QCoreApplication.translate("MainWindow", u"                          Restore All", None))
        self.restore_selected.setText(QCoreApplication.translate("MainWindow", u"               Restore Selected", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"     Settings", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"       Exit", None))
    # retranslateUi

