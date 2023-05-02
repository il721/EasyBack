from PySide6.QtWidgets import QMainWindow


class PySideMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # translit button
        self.ui.translit_button.setShortcut('Ctrl+t')
        self.ui.translit_button.clicked.connect(self.translit_input_text)
        # clear button
        self.ui.clear_button.setShortcut('Ctrl+d')
        self.ui.clear_button.clicked.connect(self.clear_all_windows)

    def translit_input_text(self) -> None:
        """
        Translit and copy to clipboard input text
        """
        text_in = self.ui.input_window.toPlainText()
        text_out = translit(text_in)
        pc.copy(text_out)
        self.ui.output_window.setText(text_out)

    def clear_all_windows(self) -> None:
        """
        Clear text in input/output window when press button clear
        """
        self.ui.input_window.clear()
        self.ui.output_window.clear()
