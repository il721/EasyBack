from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
import dop_win_rc


class D_01_1_ViewDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 250)
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
        self.info_2 = QLabel(Dialog)
        self.info_2.setObjectName(u"info_2")
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info_2)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        self.info.setFont(font)
        self.info.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_backup_list = QPushButton(Dialog)
        self.save_backup_list.setObjectName(u"save_backup_list")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_backup_list.sizePolicy().hasHeightForWidth())
        self.save_backup_list.setSizePolicy(sizePolicy)
        self.save_backup_list.setMinimumSize(QSize(180, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_backup_list.setIcon(icon)
        self.save_backup_list.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.save_backup_list)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Add Item to Backup List", None))
        self.info_2.setText(
            QCoreApplication.translate("Dialog", u"Enter New Buckup File Name:", None))
        self.input_name.setText("")
        self.input_name.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"Input name of backup file here", None))
        self.info.setText(
            QCoreApplication.translate("Dialog", u"To remove line from list below just select them",
                                       None))
        self.save_backup_list.setText(QCoreApplication.translate("Dialog", u"   Save List", None))
    # retranslateUi
