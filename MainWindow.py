from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMainWindow
from ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.file_list = QListWidget(self)
        self.directory_list: list = []
        # self.directory_list = QListWidget(self)

        # self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.dir.clicked.connect(self.test2())
        self.ui.test.clicked.connect(self.test())
        # self.ui.files.clicked.connect(self.open_file_dialog())

        # clear button
        # self.ui.clear_button.setShortcut('Ctrl+d')
        # self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def test(self):
        print('buttun on')

    def test2(self):
        print('**********')

    def open_directory_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        filenames = dialog.selectedFiles()
        # dialog.exec()
        if filenames:
            self.directory_list.append(filenames)
        print(self.directory_list)

    # def open_file_dialog(self):
    #     dialog = QFileDialog(self)
    #     dialog.setDirectory(r'F:')
    #     dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
    #     # dialog.setNameFilter("Images (*.png *.jpg)")
    #     dialog.setViewMode(QFileDialog.ViewMode.List)
    #     if dialog.exec():
    #         filenames = dialog.selectedFiles()
    #         if filenames:
    #             self.file_list.addItems([str(Path(filename)) for filename in filenames])
    #     print(self.file_list)
