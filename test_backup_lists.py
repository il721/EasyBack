"""Unit tests for backup_lists.py (pure file CRUD, stdlib only)."""
import json
import os
import shutil
import tempfile
import unittest

import backup_lists as bl


class TestBackupLists(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="bl_test_")

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_valid_list_name_accepts_plain_names(self):
        self.assertTrue(bl.valid_list_name("work_pc"))
        self.assertTrue(bl.valid_list_name("My Photos 2026"))

    def test_valid_list_name_rejects_empty(self):
        self.assertFalse(bl.valid_list_name(""))
        self.assertFalse(bl.valid_list_name("   "))

    def test_valid_list_name_rejects_reserved_chars(self):
        for ch in '\\/:*?"<>|':
            self.assertFalse(bl.valid_list_name(f"a{ch}b"), ch)

    def test_valid_list_name_rejects_windows_device_names(self):
        for bad in ("CON", "nul", "Com1", "LPT9"):
            self.assertFalse(bl.valid_list_name(bad), bad)

    def test_list_names_missing_dir_returns_empty(self):
        missing = os.path.join(self.dir, "nope")
        self.assertEqual(bl.list_names(missing), [])

    def test_save_then_load_roundtrip(self):
        bl.save_list(self.dir, "work_pc", {"s_Word": ["C:/x"]})
        self.assertEqual(bl.load_list(self.dir, "work_pc"), {"s_Word": ["C:/x"]})

    def test_save_creates_dir_if_missing(self):
        sub = os.path.join(self.dir, "backup_lists")
        bl.save_list(sub, "a", {})
        self.assertTrue(os.path.isfile(os.path.join(sub, "a")))

    def test_save_roundtrip_unicode(self):
        bl.save_list(self.dir, "доку", {"s_Папка": ["D:/Фото"]})
        self.assertEqual(bl.load_list(self.dir, "доку"),
                         {"s_Папка": ["D:/Фото"]})

    def test_list_names_sorted(self):
        for n in ("banana", "apple", "cherry"):
            bl.save_list(self.dir, n, {})
        self.assertEqual(bl.list_names(self.dir), ["apple", "banana", "cherry"])

    def test_list_exists(self):
        self.assertFalse(bl.list_exists(self.dir, "x"))
        bl.save_list(self.dir, "x", {})
        self.assertTrue(bl.list_exists(self.dir, "x"))

    def test_save_overwrites(self):
        bl.save_list(self.dir, "x", {"a": [1]})
        bl.save_list(self.dir, "x", {"b": [2]})
        self.assertEqual(bl.load_list(self.dir, "x"), {"b": [2]})

    def test_rename_list(self):
        bl.save_list(self.dir, "old", {"a": [1]})
        bl.rename_list(self.dir, "old", "new")
        self.assertFalse(bl.list_exists(self.dir, "old"))
        self.assertEqual(bl.load_list(self.dir, "new"), {"a": [1]})

    def test_delete_list(self):
        bl.save_list(self.dir, "x", {})
        bl.delete_list(self.dir, "x")
        self.assertFalse(bl.list_exists(self.dir, "x"))

    def test_load_list_missing_raises(self):
        with self.assertRaises(FileNotFoundError):
            bl.load_list(self.dir, "nope")

    def test_load_list_corrupt_raises(self):
        with open(os.path.join(self.dir, "bad"), "w", encoding="utf-8") as f:
            f.write("{not json")
        with self.assertRaises(json.JSONDecodeError):
            bl.load_list(self.dir, "bad")


if __name__ == "__main__":
    unittest.main()
