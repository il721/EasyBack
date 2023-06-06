from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, )
from PySide6.QtGui import (QIcon, )
from PySide6.QtWidgets import (QComboBox, QDialog, QFileDialog, QFrame, QHBoxLayout, QLabel,
                               QLineEdit,
                               QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QTabWidget, QToolButton,
                               QVBoxLayout, QWidget, )
import dop_win_rc
from main_base import MainBase
import MainWindow as mw
import all_styles


class settings_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(620, 602)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(620, 600))
        Dialog.setMaximumSize(QSize(620, 602))
        Dialog.setStyleSheet(u"*{\n"
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
                             "border-color: #2B79C2;}\n"
                             "QPushButton {\n"
                             "border: 2px solid;\n"
                             "color: rgb(230, 230, 230);\n"
                             "border-color: rgb(110, 110, 110);\n"
                             "border-radius: 15px;\n"
                             "background-color: rgba(60,60, 60, 80);}\n"
                             "QPushButton:disabled{\n"
                             "background-color: rgb(100,100,100);}\n"
                             "QPushButton:hover {\n"
                             "color: #2B79C2;\n"
                             "border: 3px solid;\n"
                             "background-color: rgba(30, 30, 30, 180);\n"
                             "border-color: rgb(150,150, 150);}\n"
                             "QPushButton:pressed {\n"
                             "color: rgb(30, 30, 30);\n"
                             "border: 2px solid;\n"
                             "background-color: #2B79C2;\n"
                             "border-color: rgb(230, 230, 230);}\n"
                             "QRadioButton{\n"
                             "font: 14pt \"Lexend Light\";\n"
                             "border: no}\n"
                             "QToolButton{\n"
                             ""
                             "image: url(:/icon/icons/GREY/info_invert.svg);\n"
                             "border: no}\n"
                             "QToolButton:hover {\n"
                             "image: url(:/icon/icons/GREY/info.svg);\n"
                             "border: no}\n"
                             "QToolButton:pressed{\n"
                             "image: url(:/icon/icons/GREY/info_invert.svg);\n"
                             "border: no}\n"
                             "QTabBar::tab {\n"
                             "background:  rgb(60,60, 60);\n"
                             "font: 12pt \"Lexend Light\";\n"
                             "color: rgb(150,150, 150);}\n"
                             "QTabBar::tab:selected {\n"
                             "background: #2B79C2;\n"
                             "color: rgb(230, 230, 230)}\n"
                             "QFrame:disabled{\n"
                             "background-color: rgb(50,50,50);}"
                             "QRadioButton:disabled{\n background-color: rgb(50,50,50);}"
                             "QToolButton:disabled{\n background-color: rgb(50,50,50);}")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(600, 480))
        self.tabWidget.setMaximumSize(QSize(16777215, 480))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_main = QWidget()
        self.tab_main.setObjectName(u"tab_main")
        self.verticalLayout = QVBoxLayout(self.tab_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox = QFrame(self.tab_main)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setMinimumSize(QSize(0, 125))
        self.checkbox.setStyleSheet(u"")
        self.label_info_subfolders = QLabel(self.checkbox)
        self.label_info_subfolders.setObjectName(u"label_info_subfolders")
        self.label_info_subfolders.setGeometry(QRect(10, 10, 541, 16))
        self.label_info_subfolders.setStyleSheet(u"")
        self.default_folder_rad = QRadioButton(self.checkbox)
        self.default_folder_rad.setObjectName(u"default_folder_rad")
        self.default_folder_rad.setGeometry(QRect(11, 36, 385, 24))
        self.default_folder_rad.setStyleSheet(u"")
        self.default_folder_rad.setChecked(True)
        self.default_info = QToolButton(self.checkbox)
        self.default_info.setObjectName(u"default_info")
        self.default_info.setGeometry(QRect(450, 40, 25, 25))
        self.default_info.setStyleSheet(u"")
        self.default_info.setIconSize(QSize(10, 10))
        self.select_folders_rad = QRadioButton(self.checkbox)
        self.select_folders_rad.setObjectName(u"select_folders_rad")
        self.select_folders_rad.setGeometry(QRect(11, 80, 386, 24))
        self.select_folders_rad.setStyleSheet(u"")
        self.select_folders_rad.setChecked(False)
        self.select_info = QToolButton(self.checkbox)
        self.select_info.setObjectName(u"select_info")
        self.select_info.setGeometry(QRect(450, 80, 25, 25))
        self.select_info.setStyleSheet(u"")
        self.select_info.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.checkbox)

        self.main_folder = QLabel(self.tab_main)
        self.main_folder.setObjectName(u"main_folder")
        self.main_folder.setMinimumSize(QSize(0, 30))
        self.main_folder.setMaximumSize(QSize(16777215, 30))
        self.main_folder.setStyleSheet(u"color: rgb(100, 100, 100);\n"
                                       "border: 1px solid;\n"
                                       "border-color: #2B79C2;")

        self.verticalLayout.addWidget(self.main_folder)

        self.sel_main_folder = QPushButton(self.tab_main)
        self.sel_main_folder.setObjectName(u"sel_main_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sel_main_folder.sizePolicy().hasHeightForWidth())
        self.sel_main_folder.setSizePolicy(sizePolicy1)
        self.sel_main_folder.setMinimumSize(QSize(220, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sel_main_folder.setIcon(icon)
        self.sel_main_folder.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.sel_main_folder)

        self.verticalSpacer_2 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.select_frame = QFrame(self.tab_main)
        self.select_frame.setObjectName(u"select_frame")
        self.select_frame.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select_frame.sizePolicy().hasHeightForWidth())
        self.select_frame.setSizePolicy(sizePolicy2)
        self.select_frame.setMinimumSize(QSize(0, 160))
        self.select_frame.setMaximumSize(QSize(16777215, 160))
        self.select_frame.setStyleSheet(u"")
        self.select_frame.setFrameShape(QFrame.StyledPanel)
        self.select_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.select_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sett_text = QLabel(self.select_frame)
        self.sett_text.setObjectName(u"sett_text")
        self.sett_text.setMinimumSize(QSize(85, 30))
        self.sett_text.setMaximumSize(QSize(16777215, 30))
        self.sett_text.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.sett_text)

        self.sett_folder = QLineEdit(self.select_frame)
        self.sett_folder.setObjectName(u"sett_folder")
        self.sett_folder.setMinimumSize(QSize(465, 0))
        self.sett_folder.setMaximumSize(QSize(460, 16777215))

        self.horizontalLayout_2.addWidget(self.sett_folder)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.data_text = QLabel(self.select_frame)
        self.data_text.setObjectName(u"data_text")
        self.data_text.setMinimumSize(QSize(85, 30))
        self.data_text.setMaximumSize(QSize(16777215, 30))
        self.data_text.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.data_text)

        self.data_folder_2 = QLineEdit(self.select_frame)
        self.data_folder_2.setObjectName(u"data_folder_2")
        self.data_folder_2.setMinimumSize(QSize(465, 0))
        self.data_folder_2.setMaximumSize(QSize(460, 16777215))

        self.horizontalLayout_3.addWidget(self.data_folder_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.settings_folder = QPushButton(self.select_frame)
        self.settings_folder.setObjectName(u"settings_folder")
        sizePolicy.setHeightForWidth(self.settings_folder.sizePolicy().hasHeightForWidth())
        self.settings_folder.setSizePolicy(sizePolicy)
        self.settings_folder.setMinimumSize(QSize(0, 50))
        self.settings_folder.setMaximumSize(QSize(280, 50))

        self.horizontalLayout_4.addWidget(self.settings_folder)

        self.data_folder = QPushButton(self.select_frame)
        self.data_folder.setObjectName(u"data_folder")
        sizePolicy.setHeightForWidth(self.data_folder.sizePolicy().hasHeightForWidth())
        self.data_folder.setSizePolicy(sizePolicy)
        self.data_folder.setMinimumSize(QSize(280, 50))
        self.data_folder.setMaximumSize(QSize(280, 50))

        self.horizontalLayout_4.addWidget(self.data_folder)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout.addWidget(self.select_frame)

        self.tabWidget.addTab(self.tab_main, "")
        self.tab_appearance = QWidget()
        self.tab_appearance.setObjectName(u"tab_appearance")
        self.tab_appearance.setStyleSheet(u"")
        self.comboBox = QComboBox(self.tab_appearance)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 80, 121, 41))
        self.tabWidget.addTab(self.tab_appearance, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_settings = QPushButton(Dialog)
        self.save_settings.setObjectName(u"save_settings")
        sizePolicy1.setHeightForWidth(self.save_settings.sizePolicy().hasHeightForWidth())
        self.save_settings.setSizePolicy(sizePolicy1)
        self.save_settings.setMinimumSize(QSize(220, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/GREY/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_settings.setIcon(icon1)
        self.save_settings.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.save_settings)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_settings = QPushButton(Dialog)
        self.main_settings.setEnabled(MainBase.settings_exist)
        self.main_settings.setObjectName(u"main_settings")
        sizePolicy1.setHeightForWidth(self.main_settings.sizePolicy().hasHeightForWidth())
        self.main_settings.setSizePolicy(sizePolicy1)
        self.main_settings.setMinimumSize(QSize(220, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.main_settings.setIcon(icon2)
        self.main_settings.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.main_settings)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

        # ************************    MY CODE    ***************************************************
        if MainBase.settings_exist:
            main_folder_path = MainBase.path_of_main_folder
            settings_folder_path = MainBase.path_of_settings_folder
            data_folder_path = MainBase.path_of_data_folder
            self.main_folder.setText(main_folder_path)
            self.sett_folder.setText(settings_folder_path)
            self.data_folder_2.setText(data_folder_path)
        # ************************  MY CODE (buttons)  *********************************************
        self.sel_main_folder.clicked.connect(self.select_main_folder_bt)
        self.default_info.clicked.connect(self.default_info_bt)
        self.select_info.clicked.connect(self.select_info_bt)
        self.save_settings.clicked.connect(self.save_settings_bt)
        self.main_settings.clicked.connect(Dialog.reject)

        self.default_folder_rad.clicked.connect(self.data_radio_bt)
        self.select_folders_rad.clicked.connect(self.select_radio_bt)
        # ------------------------------------------------------------------------------------------

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_info_subfolders.setText(QCoreApplication.translate("Dialog",
                                                                      u"Select what backup subfolders you want to create:",
                                                                      None))
        # if QT_CONFIG(tooltip)
        self.default_folder_rad.setToolTip(QCoreApplication.translate("Dialog",
                                                                      u"\"SETTINGS\" and \"DATA\" was create automaticly in Main Folder",
                                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.default_folder_rad.setText(
            QCoreApplication.translate("Dialog", u"Default (Select only Main Backup Folder)", None))
        # if QT_CONFIG(tooltip)
        self.select_folders_rad.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.select_folders_rad.setText(
            QCoreApplication.translate("Dialog", u"I want to select existing Folders manualy",
                                       None))
        self.main_folder.setText(
            QCoreApplication.translate("Dialog", u"Please select main backup folder...", None))
        self.sel_main_folder.setText(
            QCoreApplication.translate("Dialog", u"    Select Main Backup Folder", None))
        self.sett_text.setText(QCoreApplication.translate("Dialog", u"SETTINGS:", None))
        self.data_text.setText(QCoreApplication.translate("Dialog", u"DATA:", None))
        self.settings_folder.setText(
            QCoreApplication.translate("Dialog", u"Select \"SETTINGS\" Folder", None))
        self.data_folder.setText(
            QCoreApplication.translate("Dialog", u"Select \"DATA\" Folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main),
                                  QCoreApplication.translate("Dialog", u"Main", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Large", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Medium", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Small", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_appearance),
                                  QCoreApplication.translate("Dialog", u"Appearance", None))
        self.save_settings.setText(QCoreApplication.translate("Dialog", u"   Save Settings", None))
        self.main_settings.setText(QCoreApplication.translate("Dialog", u"  Main Menu", None))

    # ************************    MY CODE    *******************************************************
    @staticmethod
    def default_info_bt():
        title = 'Info'
        main = 'Folders "SETTINGS" and "DATA" will be created automatically in the Main Folder. ' \
               'Program settings (settings.ini) and all backup lists are stored in the "SETTING"' \
               ' folder.'
        mw.msg_one_button(title, main, 'info')

    @staticmethod
    def select_info_bt():
        title = 'Info'
        main = 'You have to choose the folders "SETTINGS" and "DATA" yourself.' \
               ' The "SETTINGS" folder must be specified, ' \
               'it will store the program settings and buckup lists. "DATA" - as needed.'
        mw.msg_one_button(title, main, 'info')

    def save_settings_bt(self):
        MainBase.save_settings()

        # if the main folder is not set, the dialog will not close
        if MainBase.settings_exist:
            self.main_settings.setEnabled(True)

    def select_main_folder_bt(self):
        dialog = QFileDialog()
        dialog.setDirectory(r'F:')
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = "".join(dialog.selectedFiles())
            if filenames == MainBase.path_of_main_folder:
                return
            else:
                MainBase.flag_change_settings = True
                MainBase.path_of_main_folder = filenames
                MainBase.path_of_settings_folder = f"{filenames}/SETTINGS"
                MainBase.path_of_data_folder = f"{filenames}/DATA"
                self.main_folder.setText(filenames)
                self.sett_folder.setText(MainBase.path_of_settings_folder)
                self.data_folder_2.setText(MainBase.path_of_data_folder)

    def super_warnings(self) -> str:
        """
        dialog for double confirmation of backup folder transfer

        :return: str 'yes' or 'no'
        """

    def data_radio_bt(self):
        self.select_frame.setEnabled(False)
        self.main_folder.setEnabled(True)
        self.sel_main_folder.setEnabled(True)

    def select_radio_bt(self):
        self.select_frame.setEnabled(True)
        self.main_folder.setEnabled(False)
        self.sel_main_folder.setEnabled(False)
