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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(520, 150))
        Form.setMaximumSize(QSize(520, 150))
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 5, 5)
        self.progress_frame = QFrame(Form)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setMinimumSize(QSize(500, 100))
        self.progress_frame.setMaximumSize(QSize(500, 100))
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.progress_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progress_text = QLabel(self.progress_frame)
        self.progress_text.setObjectName(u"progress_text")

        self.verticalLayout_2.addWidget(self.progress_text)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progress_bar_line = QProgressBar(self.progress_frame)
        self.progress_bar_line.setObjectName(u"progress_bar_line")
        self.progress_bar_line.setMinimumSize(QSize(390, 50))
        self.progress_bar_line.setMaximumSize(QSize(390, 50))
        self.progress_bar_line.setValue(24)

        self.horizontalLayout.addWidget(self.progress_bar_line)

        self.pushButton = QPushButton(self.progress_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.progress_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.progress_text.setText(QCoreApplication.translate("Form", u"test", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

