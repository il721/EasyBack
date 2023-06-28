from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, )
from PySide6.QtWidgets import (QProgressBar)
from all_styles import PROGRESS_BAR


class UiProgressBar(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(492, 113)
        Form.setStyleSheet(PROGRESS_BAR)
        self.progress_bar_line = QProgressBar(Form)
        self.progress_bar_line.setObjectName(u"progress_bar_line")
        self.progress_bar_line.setGeometry(QRect(20, 50, 451, 50))
        self.progress_bar_line.setMinimumSize(QSize(0, 50))
        self.progress_bar_line.setMaximumSize(QSize(16777215, 50))
        self.progress_bar_line.setValue(24)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        # ************************    MY CODE    ***************************************************

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi
