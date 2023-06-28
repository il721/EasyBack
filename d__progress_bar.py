from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QFrame, QGraphicsDropShadowEffect, QLabel, QProgressBar, QSizePolicy,
                               QVBoxLayout)
from all_styles import PROGRESS_BAR


class UiProgressBar(object):
    def __init__(self, time: int, text: str):

        self.text = text
        self.time = time

    def setupUi(self, Form):
        self.value = 0
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(610, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(510, 110))
        Form.setMaximumSize(QSize(510, 110))
        Form.setStyleSheet(PROGRESS_BAR)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progress_frame = QFrame(Form)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setMinimumSize(QSize(500, 100))
        self.progress_frame.setMaximumSize(QSize(500, 100))
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.progress_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.progress_text = QLabel(self.progress_frame)
        self.progress_text.setObjectName(u"progress_text")
        self.progress_text.setStyleSheet("border: no;")

        self.verticalLayout_2.addWidget(self.progress_text)

        self.progress_bar_line = QProgressBar(self.progress_frame)
        self.progress_bar_line.setObjectName(u"progress_bar_line")
        self.progress_bar_line.setMinimumSize(QSize(0, 50))
        self.progress_bar_line.setMaximumSize(QSize(16777215, 50))
        self.progress_bar_line.setValue(24)

        self.verticalLayout_2.addWidget(self.progress_bar_line)

        self.verticalLayout.addWidget(self.progress_frame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        # ************************    MY CODE    ***************************************************
        self.shadow = QGraphicsDropShadowEffect()
        # self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(20)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.progress_frame.setGraphicsEffect(self.shadow)

        self.progress_text.setText(self.text)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(self.time)
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.progress_text.setText("")

    # retranslateUi

    # ************************    MY CODE    *******************************************************
    def progress(self):
        if self.value <= 100:
            self.progress_bar_line.setValue(self.value)
            self.value += 1
        else:
            self.timer.stop()
