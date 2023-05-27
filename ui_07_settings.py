

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import dop_win_rc_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 479)
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
                             "QRadioButton{\n"
                             "font: 14pt \"Lexend Light\";\n"
                             "border: no\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sel_main_folder = QPushButton(Dialog)
        self.sel_main_folder.setObjectName(u"sel_main_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sel_main_folder.sizePolicy().hasHeightForWidth())
        self.sel_main_folder.setSizePolicy(sizePolicy)
        self.sel_main_folder.setMinimumSize(QSize(220, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sel_main_folder.setIcon(icon)
        self.sel_main_folder.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.sel_main_folder)

        self.checkbox = QFrame(Dialog)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setStyleSheet(u"border-color: #2B79C2;")
        self.verticalLayout_2 = QVBoxLayout(self.checkbox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_info_subfolders = QLabel(self.checkbox)
        self.label_info_subfolders.setObjectName(u"label_info_subfolders")
        self.label_info_subfolders.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_info_subfolders)

        self.default_folder_rad = QRadioButton(self.checkbox)
        self.default_folder_rad.setObjectName(u"default_folder_rad")
        self.default_folder_rad.setChecked(True)

        self.verticalLayout_2.addWidget(self.default_folder_rad)

        self.my_subfolders_rad = QRadioButton(self.checkbox)
        self.my_subfolders_rad.setObjectName(u"my_subfolders_rad")

        self.verticalLayout_2.addWidget(self.my_subfolders_rad)

        self.verticalLayout.addWidget(self.checkbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.info_main_folder = QLabel(Dialog)
        self.info_main_folder.setObjectName(u"info_main_folder")
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.info_main_folder.setFont(font)
        self.info_main_folder.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info_main_folder)

        self.input_name = QLineEdit(Dialog)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setMinimumSize(QSize(0, 40))
        self.input_name.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Lexend Light"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.input_name.setFont(font1)
        self.input_name.setStyleSheet(u"color: rgb(202, 202, 202);\n"
                                      "border-color: #2B79C2;\n"
                                      "")

        self.verticalLayout.addWidget(self.input_name)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        self.info.setFont(font)
        self.info.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_item = QPushButton(Dialog)
        self.add_item.setObjectName(u"add_item")
        sizePolicy.setHeightForWidth(self.add_item.sizePolicy().hasHeightForWidth())
        self.add_item.setSizePolicy(sizePolicy)
        self.add_item.setMinimumSize(QSize(220, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/GREY/gr_add_item.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon1)
        self.add_item.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.add_item)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QSize(220, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/gr_to_main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon2)
        self.ok.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sel_main_folder.setText(
            QCoreApplication.translate("Dialog", u"    Select Main Backup Folder", None))
        self.label_info_subfolders.setText(QCoreApplication.translate("Dialog",
                                                                      u"Select what backup subfolders you want to create:",
                                                                      None))
        # if QT_CONFIG(tooltip)
        self.default_folder_rad.setToolTip(QCoreApplication.translate("Dialog",
                                                                      u"Select this if you want to backup programm settings like MS Word, Adobe Photoshop etc.",
                                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.default_folder_rad.setText(QCoreApplication.translate("Dialog",
                                                                   u"Defaul \"SETTINGS\" and \"DATA\" in Main Backup Folder",
                                                                   None))
        # if QT_CONFIG(tooltip)
        self.my_subfolders_rad.setToolTip(QCoreApplication.translate("Dialog",
                                                                     u"Select this if you want to backup some personal data like MyWork, Foto, Doc`s etc.",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.my_subfolders_rad.setText(
            QCoreApplication.translate("Dialog", u"I want to select existing Folders", None))
        self.info_main_folder.setText(
            QCoreApplication.translate("Dialog", u"You files and settings are stored in:", None))
        self.input_name.setText("")
        self.input_name.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"Input name of backup item here", None))
        self.info.setText(
            QCoreApplication.translate("Dialog", u"To remove line from list below just select them",
                                       None))
        self.add_item.setText(QCoreApplication.translate("Dialog", u"    Add Item", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"   Main Menu", None))
    # retranslateUi
