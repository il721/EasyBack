##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide6
## V: 1.0.0
##

import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow
from PySide6.QtGui import (QColor, )
# from PySide6.QtWidgets import *

# GUI FILE
from ui_splash_screen import Ui_SplashScreen
from ui_progress_bar_cirkle import UiProgressBarCircle

# GLOBALS
counter = 0
jumper = 10


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UiProgressBarCircle()
        self.ui.setupUi(self)

    ## DEF PROGRESS BAR VALUE
    # @staticmethod
    # def progress_bar_value(value, widget, color):
    #     # PROGRESSBAR STYLESHEET BASE
    #     style_sheet = """
    #     QFrame{border-radius: 110px;
    #      background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,
    #      stop:{STOP_1} rgba(255, 0, 127, 0),
    #      stop:{STOP_2} {COLOR});
    #     }
    #     """
    #
    #     # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
    #     # stop works of 1.000 to 0.000
    #     progress = (100 - value) / 100.0
    #
    #     # GET NEW VALUES
    #     stop_1 = str(progress - 0.001)
    #     stop_2 = str(progress)
    #
    #     # FIX MAX VALUE
    #     if value == 100:
    #         stop_1 = "1.000"
    #         stop_2 = "1.000"
    #
    #     # SET VALUES TO NEW STYLESHEET
    #     new_stylesheet = style_sheet.replace("{STOP_1}", stop_1).replace("{STOP_2}",
    #                                                                      stop_2).replace(
    #         "{COLOR}", color)
    #
    #     # APPLY STYLESHEET WITH NEW VALUES
    #     widget.setStyleSheet(new_stylesheet)


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progress_bar_value(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(5)

        ## SHOW ==> MAIN WINDOW
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        html_text = f'<p><span style=" font-size:68pt;">{str(jumper)}</span>' \
                    f'<span style=" font-size:58pt;; vertical-align:super;">%</span></p>'

        if value > jumper:
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(html_text)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100:
            value = 1.000
        self.progress_bar_value(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            print('STOP')

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    def progress_bar_value(self, value):

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        style_sheet = "QFrame{border-radius: 150px;" \
                      "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90," \
                      f"stop:{stop_1} rgba(255, 0, 127, 0)," \
                      f"stop:{stop_2} rgba(85, 170, 255, 255));" \
                      "}"

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(style_sheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
