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
        warn.assert_called_once()
        self.assertEqual(warn.call_args[0][2], "warn")
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

    def test_empty_name_warns_and_does_not_save(self):
        seldlg, _additem, ui = self._make_dialog()
        ui.input_file_name.setText("")
        with mock.patch.object(seldlg, "msg_one_button") as warn:
            ui.save_list_bt()
        warn.assert_called_once()
        self.assertEqual(warn.call_args[0][2], "warn")
        self.assertEqual(bl.list_names(MainBase.backup_lists_dir()), [])

    def test_save_blocked_when_settings_folder_unset(self):
        seldlg, _additem, ui = self._make_dialog()
        MainBase.path_settings_folder = ""   # simulate settings not loaded
        ui.input_file_name.setText("work_pc")
        with mock.patch.object(seldlg, "msg_one_button") as warn:
            ui.save_list_bt()
        warn.assert_called_once()
        self.assertEqual(warn.call_args[0][2], "warn")

    def test_save_does_not_mutate_working_set(self):
        seldlg, additem, ui = self._make_dialog()
        ui.input_file_name.setText("work_pc")
        with mock.patch.object(seldlg, "msg_one_button"):
            ui.save_list_bt()
        # Saving persists a copy; the in-memory working set is unchanged.
        self.assertEqual(additem.base.all_items, {"s_Word": ["C:/x"]})


class TestWorkingSet(unittest.TestCase):
    def test_add_item_targets_default_working_set(self):
        import d__01_add_item as additem
        additem.base.all_items.clear()
        ui = additem.AddItemDial01()
        dlg = QDialog()
        ui.setupUi(dlg)
        ui.input_name.setText("Word")
        ui.suffix = "s_"
        ui.list_of_file = ["C:/x"]
        with mock.patch.object(additem, "msg_one_button"):
            ui.add_item_01_bt()
        self.assertEqual(additem.base.all_items, {"s_Word": ("C:/x",)})

    def test_add_item_targets_given_dict(self):
        import d__01_add_item as additem
        target = {}
        ui = additem.AddItemDial01(target=target)
        dlg = QDialog()
        ui.setupUi(dlg)
        ui.input_name.setText("Photos")
        ui.suffix = "d_"
        ui.list_of_file = ["D:/p"]
        with mock.patch.object(additem, "msg_one_button"):
            ui.add_item_01_bt()
        self.assertEqual(target, {"d_Photos": ("D:/p",)})

    def test_clear_all_empties_working_set_when_confirmed(self):
        import d__01_add_item as additem
        additem.base.all_items.clear()
        additem.base.all_items["s_Word"] = ("C:/x",)
        ui = additem.AddItemDial01()
        dlg = QDialog()
        ui.setupUi(dlg)
        ui.list_of_file = ["C:/x"]
        with mock.patch.object(additem, "msg_two_button", return_value="yes"):
            ui.clear_all_bt()
        self.assertEqual(additem.base.all_items, {})
        self.assertEqual(ui.list_of_file, [])

    def test_clear_all_targets_given_dict_not_global(self):
        import d__01_add_item as additem
        additem.base.all_items.clear()
        additem.base.all_items["s_Global"] = ("G",)
        target = {"d_Local": ("L",)}
        ui = additem.AddItemDial01(target=target)
        dlg = QDialog()
        ui.setupUi(dlg)
        with mock.patch.object(additem, "msg_two_button", return_value="yes"):
            ui.clear_all_bt()
        self.assertEqual(target, {})                                    # edited list cleared
        self.assertEqual(additem.base.all_items, {"s_Global": ("G",)})  # global untouched


class TestBackupAll(unittest.TestCase):
    def test_empty_shows_message(self):
        import MainWindow
        MainBase.path_settings_folder = fresh_settings_dir()
        with mock.patch.object(MainWindow, "msg_one_button") as m:
            MainWindow.MainWindowDialog.backup_all_bt()
        m.assert_called()

    def test_aggregates_and_copies_from_all_lists(self):
        import MainWindow
        settings = fresh_settings_dir()
        MainBase.path_settings_folder = settings
        base_dir = MainBase.backup_lists_dir()
        # A real source file that a settings item points at.
        src = os.path.join(settings, "src.txt")
        with open(src, "w") as f:
            f.write("hi")
        bl.save_list(base_dir, "list_a", {"s_Alpha": [src]})
        bl.save_list(base_dir, "list_b", {"s_Beta": [src]})
        with mock.patch.object(MainWindow, "msg_one_button"):
            MainWindow.MainWindowDialog.backup_all_bt()
        # Existing copy logic writes each settings item to {settings}\<item>.
        self.assertTrue(os.path.isfile(os.path.join(settings, "Alpha")))
        self.assertTrue(os.path.isfile(os.path.join(settings, "Beta")))


class TestEditListManagement(unittest.TestCase):
    def _editor_with_two_lists(self):
        import d__02_edit_list_main as editmod
        MainBase.path_settings_folder = fresh_settings_dir()
        base_dir = MainBase.backup_lists_dir()
        bl.save_list(base_dir, "work_pc", {"s_Word": ["C:/x"]})
        bl.save_list(base_dir, "photos", {"d_Pics": ["D:/p"]})
        ui = editmod.EditListMain()
        dlg = QDialog()
        ui.setupUi(dlg)
        ui._dlg_ref = dlg   # keep the QDialog alive for the test's lifetime
        return editmod, base_dir, ui

    def test_lists_are_listed(self):
        _editmod, _base_dir, ui = self._editor_with_two_lists()
        self.assertEqual(ui.backup_lists.count(), 2)

    def test_delete_removes_file_and_refreshes(self):
        editmod, base_dir, ui = self._editor_with_two_lists()
        ui.backup_lists.setCurrentRow(0)  # "photos" (sorted) — index 0
        with mock.patch.object(editmod, "msg_two_button", return_value="yes"):
            ui.delete_bt_clicked()
        self.assertEqual(bl.list_names(base_dir), ["work_pc"])
        self.assertEqual(ui.backup_lists.count(), 1)

    def test_rename_changes_file_and_refreshes(self):
        editmod, base_dir, ui = self._editor_with_two_lists()
        ui.backup_lists.setCurrentRow(0)  # "photos"
        with mock.patch.object(editmod, "msg_one_button"):
            ui.do_rename("photos", "vacation")
        self.assertEqual(bl.list_names(base_dir), ["vacation", "work_pc"])

    def test_rename_collision_warns(self):
        editmod, base_dir, ui = self._editor_with_two_lists()
        with mock.patch.object(editmod, "msg_one_button") as warn:
            ui.do_rename("photos", "work_pc")
        warn.assert_called()
        self.assertEqual(bl.list_names(base_dir), ["photos", "work_pc"])


if __name__ == "__main__":
    unittest.main()
