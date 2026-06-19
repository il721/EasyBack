"""AI Settings popup.

Opened from the main menu's 'AI Settings' button. Pressing 'Find LLM' scans the
machine for every available model (local runtimes + online providers, via
llm_scan.scan_sections) and lists them, one checkable row per model. Built in
the same frameless / SETTINGS_MAIN style as the other EasyBack popups, with the
'..main menu' button in the bottom row.

The scan walks the whole home folder for weight files, so it runs on a worker
thread (_ScanWorker) to keep the dialog responsive. Checked rows are preserved
across re-scans within the open dialog; persisting them to disk is a follow-up.
"""
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread,
                            Signal)
from PySide6.QtGui import QFont, QFontMetrics, QIcon
from PySide6.QtWidgets import (QFileDialog, QHBoxLayout, QLabel, QListWidget,
                               QListWidgetItem, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)
import dop_win_rc
from all_styles import SETTINGS_MAIN
from ui_helpers import msg_one_button
from main_base import MainBase
from ai_catalog import load_catalog
from ai_backup import backup_selected, export_ai, import_ai
from llm_scan import scan_sections, collect_models, model_tool_map, ollama_modelfile

# Selection-helper icons live on disk (not in the compiled Qt resource), so load
# them by absolute path relative to this module.
_ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "icons")


def _side_icon(name):
    return QIcon(os.path.join(_ICON_DIR, name))


class _ScanWorker(QThread):
    """Runs scan_sections() off the GUI thread.

    Emits done(sections) on success or failed(message) on error, so a
    slow home-folder walk never freezes the dialog.
    """
    done = Signal(object)
    failed = Signal(str)

    def run(self):
        try:
            self.done.emit(scan_sections())
        except Exception as exc:  # noqa: BLE001 - report any failure to the UI
            self.failed.emit(str(exc))


class AiSettings(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        self.dialog = Dialog
        self._worker = None
        self._tool_map = {}          # model name -> tool id (from last scan)
        self._catalog = load_catalog()

        Dialog.resize(820, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(820, 600))
        Dialog.setMaximumSize(QSize(900, 800))
        Dialog.setStyleSheet(SETTINGS_MAIN)

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.info.setFont(font)
        self.info.setStyleSheet(u"")
        self.verticalLayout.addWidget(self.info)

        # The list and the vertical select/deselect column mirror the bottom
        # button row's geometry: the list is exactly as wide as the
        # FindLLM+Backup+Export+Import block (so its right edge meets Import's),
        # then a 10px gap, then a 210px column aligned under 'Main Menu'. Both
        # rows total 750px and are centred by matching expanding spacers.
        self.listRow = QHBoxLayout()
        self.listRow.setObjectName(u"listRow")
        self.listRow.setSpacing(10)
        self.listRow.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.found_list = QListWidget(Dialog)
        self.found_list.setObjectName(u"found_list")
        self.found_list.setMinimumSize(QSize(530, 380))
        self.found_list.setMaximumWidth(530)
        self.found_list.setStyleSheet(u"background-color: rgb(50, 50,50);\n"
                                      "color: rgb(230, 230, 230);\n"
                                      "font: 300 16pt \"Lexend Light\";")
        self.listRow.addWidget(self.found_list)

        self.selectColumn = QVBoxLayout()
        self.selectColumn.setObjectName(u"selectColumn")
        self.selectColumn.setSpacing(10)
        self.sel_all_bt = self._make_side_button(Dialog, u"sel_all_bt", "Sel_ALL.svg")
        self.dsel_all_bt = self._make_side_button(Dialog, u"dsel_all_bt", "Dsel_ALL.svg")
        self.sel_local_bt = self._make_side_button(Dialog, u"sel_local_bt", "Sel_local.svg")
        self.dsel_local_bt = self._make_side_button(Dialog, u"dsel_local_bt", "Dsel_local.svg")
        self.sel_global_bt = self._make_side_button(Dialog, u"sel_global_bt", "Sel_global.svg")
        self.dsel_global_bt = self._make_side_button(Dialog, u"dsel_global_bt", "Dsel_global.svg")
        for bt in (self.sel_all_bt, self.dsel_all_bt, self.sel_local_bt,
                   self.dsel_local_bt, self.sel_global_bt, self.dsel_global_bt):
            self.selectColumn.addWidget(bt)
        self.selectColumn.addStretch(1)
        self.listRow.addLayout(self.selectColumn)

        self.listRow.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.listRow)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSpacing(10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.find_llm = QPushButton(Dialog)
        self.find_llm.setObjectName(u"find_llm")
        self.find_llm.setMinimumSize(QSize(140, 60))
        self.find_llm.setMaximumSize(QSize(140, 60))
        self.horizontalLayout.addWidget(self.find_llm)

        self.backup_bt = QPushButton(Dialog)
        self.backup_bt.setObjectName(u"backup_bt")
        self.backup_bt.setMinimumSize(QSize(120, 60))
        self.backup_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.backup_bt)

        self.export_bt = QPushButton(Dialog)
        self.export_bt.setObjectName(u"export_bt")
        self.export_bt.setMinimumSize(QSize(120, 60))
        self.export_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.export_bt)

        self.import_bt = QPushButton(Dialog)
        self.import_bt.setObjectName(u"import_bt")
        self.import_bt.setMinimumSize(QSize(120, 60))
        self.import_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.import_bt)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QSize(210, 60))
        self.ok.setMaximumSize(QSize(210, 60))
        icon = QIcon()
        icon.addFile(u":/icon/icons/GREY/main_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ok.setIcon(icon)
        self.ok.setIconSize(QSize(50, 50))
        self.horizontalLayout.addWidget(self.ok)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        # ************************  MY CODE (buttons)  *********************************************
        self.find_llm.clicked.connect(self.find_llm_bt)
        self.backup_bt.clicked.connect(self.backup_bt_clicked)
        self.export_bt.clicked.connect(self.export_bt_clicked)
        self.import_bt.clicked.connect(self.import_bt_clicked)
        self.ok.clicked.connect(Dialog.reject)
        self.sel_all_bt.clicked.connect(self.select_all_clicked)
        self.dsel_all_bt.clicked.connect(self.deselect_all_clicked)
        self.sel_local_bt.clicked.connect(self.select_local_clicked)
        self.dsel_local_bt.clicked.connect(self.deselect_local_clicked)
        self.sel_global_bt.clicked.connect(self.select_global_clicked)
        self.dsel_global_bt.clicked.connect(self.deselect_global_clicked)
        # ------------------------------------------------------------------------------------------

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"AI Settings", None))
        self.info.setText(QCoreApplication.translate(
            "Dialog",
            u"Press 'Find LLM' to list the AI models available on this "
            u"computer (local and online). Tick the ones you want to use.",
            None))
        self.find_llm.setText(QCoreApplication.translate("Dialog", u"Find LLM", None))
        self.backup_bt.setText(QCoreApplication.translate("Dialog", u"Backup", None))
        self.export_bt.setText(QCoreApplication.translate("Dialog", u"Export", None))
        self.import_bt.setText(QCoreApplication.translate("Dialog", u"Import", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"Main Menu", None))
        self.sel_all_bt.setText(QCoreApplication.translate("Dialog", u"Select All", None))
        self.dsel_all_bt.setText(QCoreApplication.translate("Dialog", u"Deselect All", None))
        self.sel_local_bt.setText(QCoreApplication.translate("Dialog", u"Select Local", None))
        self.dsel_local_bt.setText(QCoreApplication.translate("Dialog", u"Deselect Local", None))
        self.sel_global_bt.setText(QCoreApplication.translate("Dialog", u"Select Global", None))
        self.dsel_global_bt.setText(QCoreApplication.translate("Dialog", u"Deselect Global", None))
        self._align_side_texts_right()

    def _align_side_texts_right(self):
        """Right-align each side button's label while its icon stays on the left.

        Qt draws a button's icon+text as one left-aligned block, so the label is
        prefixed with however many spaces fill the gap to the right padding,
        measured with the button's own font. pad_left/pad_right must match the
        padding set on the side buttons in _make_side_button.
        """
        pad_left, pad_right, border, icon_gap = 10, 2, 2, 4
        for btn in (self.sel_all_bt, self.dsel_all_bt, self.sel_local_bt,
                    self.dsel_local_bt, self.sel_global_bt, self.dsel_global_bt):
            text = btn.text().strip()
            fm = QFontMetrics(btn.font())
            space_w = fm.horizontalAdvance(" ") or 1
            target_right = btn.maximumWidth() - border - pad_right
            text_start = border + pad_left + btn.iconSize().width() + icon_gap
            gap = target_right - text_start - fm.horizontalAdvance(text)
            # floor (not round) so the label never overshoots the right border,
            # even for short labels that need many filler spaces.
            btn.setText(" " * max(0, int(gap / space_w)) + text)

    # ************************    MY CODE    ***************************************************
    def _make_side_button(self, Dialog, name, icon_file):
        """A fixed-width row button (icon left, label right) for the select column."""
        bt = QPushButton(Dialog)
        bt.setObjectName(name)
        bt.setMinimumSize(QSize(210, 55))
        bt.setMaximumSize(QSize(210, 55))
        # Match the rendered font so _align_side_texts_right measures correctly.
        font = QFont()
        font.setFamilies([u"Lexend Light"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        bt.setFont(font)
        bt.setIcon(_side_icon(icon_file))
        bt.setIconSize(QSize(24, 48))
        # Icon pinned left; the label is pushed to the right edge by
        # _align_side_texts_right (same approach as the main menu buttons).
        bt.setStyleSheet(u"text-align: left; padding-left: 10px; padding-right: 2px;")
        return bt

    @staticmethod
    def _is_global(item):
        """A row is 'global' (online) when its tool is a cloud provider; every
        local runtime / weight file is 'local'."""
        tool = item.data(Qt.UserRole) or ""
        return tool.endswith("-cloud") or tool == "claude-code"

    def _set_check_state(self, predicate, state):
        """Set every row matching predicate to the given check state."""
        for row in range(self.found_list.count()):
            item = self.found_list.item(row)
            if predicate(item):
                item.setCheckState(state)

    def select_all_clicked(self):
        self._set_check_state(lambda i: True, Qt.Checked)

    def deselect_all_clicked(self):
        self._set_check_state(lambda i: True, Qt.Unchecked)

    def select_local_clicked(self):
        self._set_check_state(lambda i: not self._is_global(i), Qt.Checked)

    def deselect_local_clicked(self):
        self._set_check_state(lambda i: not self._is_global(i), Qt.Unchecked)

    def select_global_clicked(self):
        self._set_check_state(self._is_global, Qt.Checked)

    def deselect_global_clicked(self):
        self._set_check_state(self._is_global, Qt.Unchecked)

    def find_llm_bt(self):
        """Scan the machine for LLMs on a worker thread and fill the list."""
        if self._worker is not None:        # a scan is already running
            return
        self.find_llm.setEnabled(False)
        self.info.setText("Scanning for AI models…")
        self._worker = _ScanWorker()
        self._worker.done.connect(self._on_scan_done)
        self._worker.failed.connect(self._on_scan_failed)
        self._worker.finished.connect(self._on_scan_finished)
        self._worker.start()

    def _on_scan_done(self, sections):
        self._populate_from_sections(sections)

    def _populate_from_sections(self, sections):
        """Fill the list from a ScanSections and remember each model's tool."""
        self._tool_map = model_tool_map(sections)
        models = collect_models(sections)
        self._fill_models(models)
        self.info.setText(
            f"Found {len(models)} model(s). Tick the ones to back up, then press Backup.")

    def _on_scan_failed(self, message):
        self.info.setText(f"Scan failed: {message}")

    def _on_scan_finished(self):
        self.find_llm.setEnabled(True)
        self._worker = None

    def _fill_models(self, names):
        """Show each model name as a checkable row, keeping prior ticks; each row
        carries its tool id (Qt.UserRole) so backup knows where it belongs."""
        checked = self._checked_names()
        self.found_list.clear()
        for name in names:
            item = QListWidgetItem(name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked if name in checked else Qt.Unchecked)
            item.setData(Qt.UserRole, self._tool_map.get(name, "local-weights"))
            self.found_list.addItem(item)

    def _checked_names(self):
        """Model names whose row is currently ticked."""
        names = set()
        for row in range(self.found_list.count()):
            item = self.found_list.item(row)
            if item.checkState() == Qt.Checked:
                names.add(item.text())
        return names

    def _checked_pairs(self):
        """(model_name, tool_id) for every ticked row."""
        pairs = []
        for row in range(self.found_list.count()):
            item = self.found_list.item(row)
            if item.checkState() == Qt.Checked:
                pairs.append((item.text(), item.data(Qt.UserRole)))
        return pairs

    def _do_backup(self, modelfile=ollama_modelfile):
        """Back up the ticked models into the AI folder. Returns the result dict."""
        pairs = self._checked_pairs()
        return backup_selected(MainBase.ai_dir(), pairs, self._catalog,
                               env=os.environ, home=os.path.expanduser("~"),
                               modelfile=modelfile)

    def backup_bt_clicked(self):
        if not self._checked_pairs():
            msg_one_button("Nothing selected",
                           "Tick at least one model first.", "info")
            return
        result = self._do_backup()
        tools = ", ".join(result["tools"])
        msg_one_button("Backup done",
                       f"Saved settings for: {tools}\ninto {MainBase.ai_dir()}", "info")

    def export_bt_clicked(self):
        out, _ = QFileDialog.getSaveFileName(
            None, "Export AI settings", "ai-settings-export.zip", "Zip (*.zip)")
        if not out:
            return
        export_ai(MainBase.ai_dir(), out)
        msg_one_button("Exported", f"AI settings exported to\n{out}", "info")

    def import_bt_clicked(self):
        path, _ = QFileDialog.getOpenFileName(
            None, "Import AI settings", "", "Zip (*.zip)")
        if not path:
            return
        import_ai(path, MainBase.ai_dir())
        msg_one_button("Imported",
                       "AI settings imported into\n"
                       f"{MainBase.ai_dir()}\n\n"
                       "Remember: secrets were not included - re-login / re-key, "
                       "and re-pull Ollama models / re-install Claude plugins.", "info")
