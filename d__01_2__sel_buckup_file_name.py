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


class D012SelFileNameDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 200)
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_enter_name = QLabel(Dialog)
        self.info_enter_name.setObjectName(u"info_enter_name")
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.info_enter_name.setFont(font)
        self.info_enter_name.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info_enter_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_file_name = QLineEdit(Dialog)
        self.input_file_name.setObjectName(u"input_file_name")
        self.input_file_name.setMinimumSize(QSize(500, 40))
        self.input_file_name.setMaximumSize(QSize(500, 40))
        font1 = QFont()
        font1.setFamilies([u"Lexend Light"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.input_file_name.setFont(font1)
        self.input_file_name.setStyleSheet(u"color: rgb(202, 202, 202);\n"
                                           "border-color: #2B79C2;\n"
                                           "")

        self.horizontalLayout.addWidget(self.input_file_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.owerwrite_exist = QPushButton(Dialog)
        self.owerwrite_exist.setObjectName(u"owerwrite_exist")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owerwrite_exist.sizePolicy().hasHeightForWidth())
        self.owerwrite_exist.setSizePolicy(sizePolicy)
        self.owerwrite_exist.setMinimumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/load.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.owerwrite_exist.setIcon(icon)
        self.owerwrite_exist.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.owerwrite_exist)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.ok_01_2 = QPushButton(Dialog)
        self.ok_01_2.setObjectName(u"ok_01_2")
        sizePolicy.setHeightForWidth(self.ok_01_2.sizePolicy().hasHeightForWidth())
        self.ok_01_2.setSizePolicy(sizePolicy)
        self.ok_01_2.setMinimumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/GREY/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok_01_2.setIcon(icon1)
        self.ok_01_2.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.ok_01_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Add Item to Backup List", None))
        self.info_enter_name.setText(QCoreApplication.translate("Dialog",
                                                                u"Enter new buckup file name or select and owerwrite an exiting file:",
                                                                None))
        self.input_file_name.setText("")
        self.input_file_name.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"Input new name of backup file here", None))
        self.owerwrite_exist.setText("")
        self.ok_01_2.setText(QCoreApplication.translate("Dialog", u"  Ok", None))
    # retranslateUi
