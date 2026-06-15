"""Headless tests for the named-backup-list dialog handlers."""
import os
import tempfile
import unittest
from unittest import mock

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QDialog

import backup_lists as bl
from main_base import MainBase

_app = QApplication.instance() or QApplication(["test"])
# Never block on a modal dialog during tests.
QDialog.exec = lambda self: 0


def fresh_settings_dir():
    """A settings folder with no backup_lists subfolder yet."""
    return tempfile.mkdtemp(prefix="eb_gui_")


class TestBackupListsDir(unittest.TestCase):
    def test_backup_lists_dir(self):
        MainBase.path_settings_folder = "X:/stuff"
        self.assertEqual(MainBase.backup_lists_dir(), "X:/stuff\\backup_lists")


class TestSaveFlow(unittest.TestCase):
    def _make_dialog(self):
        import d__01_2__sel_buckup_file_name as seldlg
        import d__01_add_item as additem
        MainBase.path_settings_folder = fresh_settings_dir()
        additem.base.all_items.clear()
        additem.base.all_items["s_Word"] = ["C:/x"]
        dlg = QDialog()          # keep a ref so PySide6 doesn't GC the widgets
        ui = seldlg.D012SelFileNameDialog()
        ui.setupUi(dlg)
        ui._dlg_ref = dlg        # prevent GC of the QDialog and its children
        return seldlg, additem, ui

    def test_save_writes_named_file(self):
        seldlg, _additem, ui = self._make_dialog()
        ui.input_file_name.setText("work_pc")
        with mock.patch.object(seldlg, "msg_one_button"):
            ui.save_list_bt()
        base_dir = MainBase.backup_lists_dir()
        self.assertTrue(bl.list_exists(base_dir, "work_pc"))
        self.assertEqual(bl.load_list(base_dir, "work_pc"), {"s_Word": ["C:/x"]})

    def test_invalid_name_warns_and_does_not_save(self):
        seldlg, _additem, ui = self._make_dialog()
        ui.input_file_name.setText("bad/name")
        with mock.patch.object(seldlg, "msg_one_button") as warn:
            ui.save_list_bt()
        warn.assert_called()
        self.assertEqual(bl.list_names(MainBase.backup_lists_dir()), [])

    def test_overwrite_confirmed_replaces(self):
        seldlg, _additem, ui = self._make_dialog()
        bl.save_list(MainBase.backup_lists_dir(), "work_pc", {"s_Old": ["a"]})
        ui.input_file_name.setText("work_pc")
        with mock.patch.object(seldlg, "msg_two_button", return_value="yes"), \
             mock.patch.object(seldlg, "msg_one_button"):
            ui.save_list_bt()
        self.assertEqual(bl.load_list(MainBase.backup_lists_dir(), "work_pc"),
                         {"s_Word": ["C:/x"]})

    def test_overwrite_declined_keeps_old(self):
        seldlg, _additem, ui = self._make_dialog()
        bl.save_list(MainBase.backup_lists_dir(), "work_pc", {"s_Old": ["a"]})
        ui.input_file_name.setText("work_pc")
        with mock.patch.object(seldlg, "msg_two_button", return_value="no"), \
             mock.patch.object(seldlg, "msg_one_button"):
            ui.save_list_bt()
        self.assertEqual(bl.load_list(MainBase.backup_lists_dir(), "work_pc"),
                         {"s_Old": ["a"]})


if __name__ == "__main__":
    unittest.main()
