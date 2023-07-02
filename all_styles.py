# from main_base import MainBase

SETTINGS_MAIN = """
            *{
                background-color: rgb(30, 30, 30);
                font: 16pt \"Lexend Light\";
                border: 1px solid;
                border-color: #2B79C2;
                color: rgb(230, 230, 230)}
            QLabel{
                font: 12pt \"Lexend Light\";
                color: #2B79C2;
                border: no}
            QLineEdit{
                background-color: rgb(30, 30, 30);}
            QLineEdit:disabled{
                background-color: rgb(50,50,50);}
            QFrame{
                border-color: #2B79C2;}
            QPushButton {
                border: 2px solid;
                color: rgb(230, 230, 230);
                border-color: rgb(110, 110, 110);
                border-radius: 15px;
                background-color: rgba(60,60, 60, 80);}
            QPushButton:disabled{
                background-color: rgb(100,100,100);}
            QPushButton:hover {
                color: #2B79C2;
                border: 3px solid;
                background-color: rgba(30, 30, 30, 180);
                border-color: rgb(150,150, 150);}
            QPushButton:pressed {
                color: rgb(30, 30, 30);
                border: 2px solid;
                background-color: #2B79C2;
                border-color: rgb(230, 230, 230);}
            QRadioButton{
                font: 14pt \"Lexend Light\";
                border: no}
            QToolButton{
                image: url(:/icon/icons/GREY/info_invert.svg);
                border: no}
            QToolButton:hover {
                image: url(:/icon/icons/GREY/info.svg);
                border: no}
            QToolButton:pressed{
                image: url(:/icon/icons/GREY/info_invert.svg);
                border: no}
            QTabBar::tab {
                background:  rgb(60,60, 60);
                font: 12pt \"Lexend Light\";
                color: rgb(150,150, 150);}
            QTabBar::tab:selected {
                background: #2B79C2;
                color: rgb(230, 230, 230)}
            QFrame:disabled{
                background-color: rgb(50,50,50);}
            QRadioButton:disabled{
                background-color: rgb(50,50,50);}
            QToolButton:disabled{
            background-color: rgb(50,50,50);}
            """

MSG_PUSH_BUTTON: str = """
            QPushButton { 
                border: 2px solid;
                color: rgb(230, 230, 230);
                border-color: rgb(110, 110, 110);
                border-radius: 15px;
                background-color: rgba(60,60, 60, 80);
                font: 300 16pt \"Lexend Light\";
                }
            QPushButton:hover {
                color: rgb(30, 30, 30);
                border: 3px solid;
                background-color: #2B79C2;
                border-color: rgb(150,150,150);
                }
            QPushButton:pressed {
                color: rgb(30, 30, 30);
                border: 2px solid;
                background-color: #2B79C2;
                border-color: rgb(230, 230, 230);
                }
                """


PROGRESS_BAR_LINE: str = """
            QWidget {
                background-color: #323232;
                font-size: 20px;
                color: #b1b1b1;
            }

            QPushButton {
                height: 45px;
                background-color: QLinearGradient(
                    x1: 0,
                    x2: 0,
                    y1: 0,
                    y2: 1,
                    stop: 0 #565656,
                    stop: 0.1 #525252,
                    stop: 0.5 #4e4e4e,
                    stop: 0.9 #4a4a4a,
                    stop: 1.0 #464646
                );
                border-width: 4.5px;
                border-color: #1e1e1e;
                border-style: solid;
                border-radius: 3px;
                padding: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }

            QPushButton:pressed {
                background-color: orange;
                color: white;

            }

            QPushButton:hover {
                border-color: orange;
                border-color: white;
            }

            QProgressBar {
                border-style: solid;
                border-color: grey;
                border-radius: 7px;
                border-width: 2px;
                text-align: center;
            }

            QProgressBar::chunk {
                width: 2px;
                background-color: #de7c09;
                margin: 3px;
            }

        """
PROGRESS_BAR: str = """
            
            QWidget {
                background-color: rgb(30, 30, 30);
            }
            QProgressBar {
                border-style: solid;
                border-color: rgb(150,150,150);
                border-radius: 7px;
                border-width: 2px;
                font: 20pt \"Lexend Light\";
                color: rgb(230, 230, 230);
                text-align: center;
            }

            QProgressBar::chunk {
                width: 2px;
                background-color: #2B79C2;
                margin: 3px;
            }
            QLabel {
                font: 16pt \"Lexend Light\";
                color: rgb(230, 230, 230);
                border: no;
            }
            QLineEdit {
                background-color: rgb(30, 30, 30);}
                QLineEdit:disabled{
                background-color: rgb(50,50,50);
            }
            QFrame {
                border-style: solid;
                border-radius: 7px;
                border-width: 2px;
                border-color: rgb(150, 150, 150);
            }
            QPushButton { 
                border: 2px solid;
                color: rgb(230, 230, 230);
                border-color: rgb(110, 110, 110);
                border-radius: 15px;
                background-color: rgba(60,60, 60, 80);
                font: 300 16pt \"Lexend Light\";
                }
            QPushButton:hover {
                color: rgb(30, 30, 30);
                border: 3px solid;
                background-color: #2B79C2;
                border-color: rgb(150,150,150);
                }
            QPushButton:pressed {
                color: rgb(30, 30, 30);
                border: 2px solid;
                background-color: #2B79C2;
                border-color: rgb(230, 230, 230);
                }
            QPushButton:disabled { 
                border: 2px solid;
                color: rgb(0, 0, 0);
                border-color: rgb(40, 40, 40);
                border-radius: 15px;
                background-color: rgba(60, 60, 60, 10);
                font: 300 16pt \"Lexend Light\";
                }
        """
