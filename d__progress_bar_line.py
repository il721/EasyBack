import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon
from all_styles import PROGRESS_BAR_LINE


class ProgressBar(QProgressBar):
    def __init__(self,):
        super().__init__()
        self.setMaximum(100)
        self._active = False

    def updateBar(self, i):
        while True:
            time.sleep(0.001)
            value = self.value() + i
            self.setValue(value)

            if value >= 50:
                self.changeColor('green')

            if value >= self.maximum() or self._active:
                self.setValue(100)
                break
            elif value >= self.maximum() or not self._active:
                break

    def changeColor(self, color):
        css = """
            ::chunk {{
                background: {0};
            }}
        """.format(color)
        self.setStyleSheet(css)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 200
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('ProgressBar Template')
        self.setWindowIcon(QIcon('qt.ico'))
        self.setStyleSheet(PROGRESS_BAR_LINE)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.progressBar = ProgressBar()
        self.layout.addWidget(self.progressBar)
        for _ in range(20):
            time.sleep(0.01)
            self.progressBar.setValue(_)
            # self.progressBar.updateBar(_)

        # self.button = QPushButton('Update ProressBar', clicked=self.updateProgressBar)
        # self.layout.addWidget(self.button)
        # for i in range(40):
        #     self.progressBar.updateBar(i)
    # def updateProgressBar(self):
    #     i = 10
    #     self.progressBar.updateBar(i)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
