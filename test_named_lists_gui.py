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


if __name__ == "__main__":
    unittest.main()
