from main_base import MainBase

SETTINGS_MAIN = "*{" \
                "background-color: rgb(30, 30, 30);" \
                "font: 16pt \"Lexend Light\";" \
                "border: 1px solid;" \
                "border-color: #2B79C2;" \
                "color: rgb(230, 230, 230)}" \
                "QLabel{" \
                "font: 12pt \"Lexend Light\";" \
                "color: #2B79C2;" \
                "border: no}" \
                "QLineEdit{" \
                "background-color: rgb(30, 30, 30);}" \
                "QLineEdit:disabled{" \
                "background-color: rgb(50,50,50);}" \
                "QFrame{" \
                "border-color: #2B79C2;}" \
                "QPushButton {" \
                "border: 2px solid;" \
                "color: rgb(230, 230, 230);" \
                "border-color: rgb(110, 110, 110);" \
                "border-radius: 15px;" \
                "background-color: rgba(60,60, 60, 80);}" \
                "QPushButton:disabled{" \
                "background-color: rgb(100,100,100);}" \
                "QPushButton:hover {" \
                "color: #2B79C2;" \
                "border: 3px solid;" \
                "background-color: rgba(30, 30, 30, 180);" \
                "border-color: rgb(150,150, 150);}" \
                "QPushButton:pressed {" \
                "color: rgb(30, 30, 30);" \
                "border: 2px solid;" \
                "background-color: #2B79C2;" \
                "border-color: rgb(230, 230, 230);}" \
                "QRadioButton{" \
                "font: 14pt \"Lexend Light\";" \
                "border: no}" \
                "QToolButton{" \
                "image: url(:/icon/icons/GREY/info_invert.svg);" \
                "border: no}" \
                "QToolButton:hover {" \
                "image: url(:/icon/icons/GREY/info.svg);" \
                "border: no}" \
                "QToolButton:pressed{" \
                "image: url(:/icon/icons/GREY/info_invert.svg);" \
                "border: no}" \
                "QTabBar::tab {" \
                "background:  rgb(60,60, 60);" \
                "font: 12pt \"Lexend Light\";" \
                "color: rgb(150,150, 150);}" \
                "QTabBar::tab:selected {" \
                "background: #2B79C2;" \
                "color: rgb(230, 230, 230)}" \
                "QFrame:disabled{ background-color: rgb(50,50,50);}" \
                "QRadioButton:disabled{ background-color: rgb(50,50,50);}" \
                "QToolButton:disabled{ background-color: rgb(50,50,50);}"

MSG_PUSH_BUTTON: str = "QPushButton { border: 2px solid; " \
                       "color: rgb(230, 230, 230);" \
                       "border-color: rgb(110, 110, 110); " \
                       "border-radius: 15px; " \
                       "background-color: rgba(60,60, 60, 80);" \
                       "font: 300 16pt \"Lexend Light\";}" \
                       "QPushButton:hover {" \
                       "color: rgb(30, 30, 30);" \
                       "border: 3px solid; " \
                       "background-color: #2B79C2;" \
                       "border-color: rgb(150,150,150);}" \
                       "QPushButton:pressed { color: rgb(30, 30, 30);" \
                       "border: 2px solid;" \
                       "background-color: #2B79C2;" \
                       "border-color: rgb(230, 230, 230);}"

# TODO !!!DON`T REMEMBER CLEAR THIS!!!!
# TODO ??? And why don`t work????
MSG_MAIN: str = f'background-color: rgb(30, 30, 30);' \
                f'color: rgb(230, 230, 230);' \
                f'font: {MainBase.font_size_dialog}\"Lexend Light\";'
