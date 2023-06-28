from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtWidgets import (QLabel, QProgressBar, QVBoxLayout)
from all_styles import PROGRESS_BAR


class UiProgressBar(object):
    def __init__(self, time: int, text: str):

        self.text = text
        self.time = time

    def setupUi(self, Form):
        self.value = 0
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(492, 113)
        Form.setStyleSheet(PROGRESS_BAR)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progress_text = QLabel(Form)
        self.progress_text.setObjectName(u"progress_text")

        self.verticalLayout.addWidget(self.progress_text)

        self.progress_bar_line = QProgressBar(Form)
        self.progress_bar_line.setObjectName(u"progress_bar_line")
        self.progress_bar_line.setMinimumSize(QSize(0, 50))
        self.progress_bar_line.setMaximumSize(QSize(16777215, 50))
        self.progress_bar_line.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar_line)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        # ************************    MY CODE    ***************************************************
        self.progress_text.setText(self.text)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(self.time)
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

    # retranslateUi

    # ************************    MY CODE    *******************************************************
    def progress(self):
        if self.value <= 100:
            self.progress_bar_line.setValue(self.value)
            self.value += 1
        else:
            self.timer.stop()
