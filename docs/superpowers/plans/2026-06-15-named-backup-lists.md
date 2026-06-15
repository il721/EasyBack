# Named Backup Lists — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the single hardcoded `all` backup file with multiple named backup lists — name-on-save, full management (edit items / rename / delete) in the edit dialog, and "Back up all" aggregating every list.

**Architecture:** Approach B — a new stdlib-only leaf module `backup_lists.py` owns all list CRUD (save/load/list/rename/delete + name validation). The existing Qt dialogs stay thin and call into it. The in-memory working set is the module-level `MainBase` singleton `base` in `d__01_add_item.py`; it persists for the app run and is reset by "Clear All".

**Tech Stack:** Python 3.13, PySide6 (Qt), `winreg`/`json`/`pathlib`/`shutil` (stdlib). Tests use stdlib `unittest`, run headlessly via the project venv with `QT_QPA_PLATFORM=offscreen`.

---

## Conventions for every task

- **Interpreter:** always `./.venv/Scripts/python.exe` (from repo root). Do **not** use a bare `python`.
- **Run a whole test module:** `./.venv/Scripts/python.exe -m unittest <module> -v`
- **Run one test:** `./.venv/Scripts/python.exe -m unittest <module>.<Class>.<test> -v`
- **List filename == list name**, no extension (e.g. `backup_lists\work_pc`).
- Branch is already `feature/named-backup-lists`. Commit after each task with the trailer:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`

## File map

| File | Responsibility | Tasks |
|---|---|---|
| `backup_lists.py` *(new)* | Pure list CRUD + name validation. Stdlib only. | 1 |
| `test_backup_lists.py` *(new)* | Unit tests for `backup_lists.py`. | 1 |
| `main_base.py` | Add `backup_lists_dir()`; drop hardcoded-`all` save. | 2, 3 |
| `test_named_lists_gui.py` *(new)* | Headless tests for the dialog handlers. | 2–7 |
| `d__01_2__sel_buckup_file_name.py` | `D012SelFileNameDialog`: name → validate → overwrite → save. | 3 |
| `d__01_add_item.py` | `save_backup_list_bt` opens the name dialog; `clear_all_bt` resets working set; `AddItemDial01` gains a target dict; drop preload. | 3, 4 |
| `MainWindow.py` | `backup_all_bt` aggregates all lists. | 5 |
| `d__02_edit_list_main.py` | `EditListMain`: rename + delete list, refresh. | 6 |
| `d__02_1_edit_item.py` | `ListBackupItemEdit`: per-list item editor (delete/add/save). | 7 |

---

## Task 1: `backup_lists.py` storage seam + unit tests

**Files:**
- Create: `backup_lists.py`
- Test: `test_backup_lists.py`

- [ ] **Step 1: Write the failing tests**

Create `test_backup_lists.py`:

```python
"""Unit tests for backup_lists.py (pure file CRUD, stdlib only)."""
import json
import os
import tempfile
import unittest

import backup_lists as bl


class TestBackupLists(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="bl_test_")

    def test_valid_list_name_accepts_plain_names(self):
        self.assertTrue(bl.valid_list_name("work_pc"))
        self.assertTrue(bl.valid_list_name("My Photos 2026"))

    def test_valid_list_name_rejects_empty_and_reserved(self):
        self.assertFalse(bl.valid_list_name(""))
        self.assertFalse(bl.valid_list_name("   "))
        for bad in r'\ / : * ? " < > |'.split():
            self.assertFalse(bl.valid_list_name(f"a{bad}b"), bad)

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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/Scripts/python.exe -m unittest test_backup_lists -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'backup_lists'`.

- [ ] **Step 3: Implement `backup_lists.py`**

Create `backup_lists.py`:

```python
"""
Storage seam for named backup lists.

A "backup list" is a JSON file inside the backup_lists folder; the file name IS
the list name (no extension). Contents: {"<s_|d_>item_name": [paths, ...]}.

Pure file operations only — no Qt, no MainBase import — so this stays a leaf
module and is unit-testable in isolation.
"""
import json
import os
from pathlib import Path

# Characters Windows forbids in file names.
_INVALID_CHARS = set('\\/:*?"<>|')


def valid_list_name(name) -> bool:
    """True if `name` is non-empty (after strip) and has no reserved chars."""
    if not name or not str(name).strip():
        return False
    return not (_INVALID_CHARS & set(str(name)))


def _path(base_dir, name) -> Path:
    return Path(base_dir) / name


def list_names(base_dir) -> list:
    """Sorted names of saved lists. Empty list if base_dir does not exist."""
    p = Path(base_dir)
    if not p.is_dir():
        return []
    return sorted(entry.name for entry in p.iterdir() if entry.is_file())


def list_exists(base_dir, name) -> bool:
    return _path(base_dir, name).is_file()


def save_list(base_dir, name, items: dict) -> None:
    """Write `items` as JSON to base_dir/name, creating base_dir if needed."""
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    with open(_path(base_dir, name), "w") as f:
        json.dump(items, f)


def load_list(base_dir, name) -> dict:
    """Read base_dir/name as JSON. Propagates FileNotFoundError/JSONDecodeError."""
    with open(_path(base_dir, name), "r") as f:
        return json.load(f)


def rename_list(base_dir, old, new) -> None:
    os.replace(_path(base_dir, old), _path(base_dir, new))


def delete_list(base_dir, name) -> None:
    os.remove(_path(base_dir, name))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/Scripts/python.exe -m unittest test_backup_lists -v`
Expected: PASS (10 tests OK).

- [ ] **Step 5: Commit**

```bash
git add backup_lists.py test_backup_lists.py
git commit -m "Add backup_lists storage module with CRUD + name validation

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 2: `MainBase.backup_lists_dir()` + GUI test scaffold

**Files:**
- Modify: `main_base.py` (add classmethod near the other `@classmethod` helpers, e.g. after `check_folder_exist`)
- Create: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing test**

Create `test_named_lists_gui.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestBackupListsDir -v`
Expected: FAIL — `AttributeError: type object 'MainBase' has no attribute 'backup_lists_dir'`.

- [ ] **Step 3: Add the classmethod**

In `main_base.py`, add inside class `MainBase` (next to the other check helpers):

```python
    @classmethod
    def backup_lists_dir(cls) -> str:
        """Folder that holds the named backup-list files."""
        return f"{cls.path_settings_folder}\\backup_lists"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestBackupListsDir -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add main_base.py test_named_lists_gui.py
git commit -m "Add MainBase.backup_lists_dir() helper + GUI test scaffold

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 3: Save flow — name the list on save

**Files:**
- Modify: `d__01_2__sel_buckup_file_name.py` (imports at top; `setupUi` store dialog + hide button; rewrite `save_list_bt`)
- Modify: `d__01_add_item.py` (rewrite `save_backup_list_bt` at lines 346-363)
- Modify: `main_base.py` (delete the now-unused `save_base_to_disk`, lines 257-265)
- Test: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing tests**

Append to `test_named_lists_gui.py`:

```python
class TestSaveFlow(unittest.TestCase):
    def _make_dialog(self):
        import d__01_2__sel_buckup_file_name as seldlg
        import d__01_add_item as additem
        MainBase.path_settings_folder = fresh_settings_dir()
        additem.base.all_items.clear()
        additem.base.all_items["s_Word"] = ["C:/x"]
        ui = seldlg.D012SelFileNameDialog()
        ui.setupUi(QDialog())
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestSaveFlow -v`
Expected: FAIL — `save_list_bt` currently calls `b.base.save_base_to_disk()` (writes to `all`), and `msg_one_button`/`msg_two_button` are not attributes of the `seldlg` module yet, so the `mock.patch.object` calls raise `AttributeError`.

- [ ] **Step 3a: Update `d__01_2__sel_buckup_file_name.py` imports**

At the top of the file, after `import d__01_add_item as b` (line 6), add:

```python
import backup_lists
from main_base import MainBase
from ui_helpers import msg_one_button, msg_two_button
```

- [ ] **Step 3b: Store the dialog ref and hide the overwrite button**

In `setupUi`, **after** the `if not Dialog.objectName(): Dialog.setObjectName(u"Dialog")` block (i.e. on the line just before `Dialog.resize(600, 200)`, so it always runs), add:

```python
        self.dialog = Dialog
```

And in the buttons section (after `self.save_list.clicked.connect(self.save_list_bt)`), add:

```python
        self.owerwrite_exist.hide()  # name collisions handled by overwrite prompt
```

- [ ] **Step 3c: Rewrite `save_list_bt`**

Replace the whole `save_list_bt` method (lines 168-171) with:

```python
    def save_list_bt(self):
        name = self.input_file_name.text().strip()
        if not backup_lists.valid_list_name(name):
            msg_one_button("Invalid name",
                           "Please enter a valid list name "
                           "(no \\ / : * ? \" < > | characters).", "warn")
            return
        base_dir = MainBase.backup_lists_dir()
        if backup_lists.list_exists(base_dir, name):
            if msg_two_button("Overwrite?",
                              f"A backup list named '{name}' already exists.\n"
                              "Overwrite it?") != "yes":
                return
        backup_lists.save_list(base_dir, name, b.base.all_items)
        msg_one_button("Saved", f"Backup list '{name}' successfully saved", "info")
        self.dialog.accept()
```

- [ ] **Step 3d: Rewrite `save_backup_list_bt` in `d__01_add_item.py`**

Replace the whole `save_backup_list_bt` static method (lines 346-363) with:

```python
    @staticmethod
    def save_backup_list_bt():
        if not base.all_items:
            msg_one_button("Nothing to save",
                           "There is nothing to save. You haven't added any items.",
                           "info")
            return
        # Local import avoids a circular import: d__01_2 imports this module.
        from d__01_2__sel_buckup_file_name import D012SelFileNameDialog
        dialog = QDialog()
        ui = D012SelFileNameDialog()
        ui.setupUi(dialog)
        dialog.exec()
```

(`QDialog` is already imported at the top of `d__01_add_item.py`.)

- [ ] **Step 3e: Delete the unused `save_base_to_disk`**

In `main_base.py`, delete the `save_base_to_disk` method (lines 257-265). Its only callers were the two handlers rewritten above.

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestSaveFlow -v`
Expected: PASS (4 tests).
Also re-run the full GUI module to confirm nothing regressed:
`./.venv/Scripts/python.exe -m unittest test_named_lists_gui -v` → PASS.

- [ ] **Step 5: Commit**

```bash
git add d__01_2__sel_buckup_file_name.py d__01_add_item.py main_base.py test_named_lists_gui.py
git commit -m "Save backup lists under a user-supplied name

Save List now opens D012SelFileNameDialog, which validates the name,
confirms overwrite on collision, and writes via backup_lists.save_list.
Removes the hardcoded-'all' save path.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 4: Working set — target dict, Clear All reset, drop preload

**Files:**
- Modify: `d__01_add_item.py` — `AddItemDial01.__init__` (lines 14-19), `add_item_01_bt` (293-339), `clear_all_bt` (341-342)
- Test: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing tests**

Append to `test_named_lists_gui.py`:

```python
class TestWorkingSet(unittest.TestCase):
    def test_add_item_targets_default_working_set(self):
        import d__01_add_item as additem
        additem.base.all_items.clear()
        ui = additem.AddItemDial01()
        ui.setupUi(QDialog())
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
        ui.setupUi(QDialog())
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
        ui.setupUi(QDialog())
        ui.list_of_file = ["C:/x"]
        with mock.patch.object(additem, "msg_two_button", return_value="yes"):
            ui.clear_all_bt()
        self.assertEqual(additem.base.all_items, {})
        self.assertEqual(ui.list_of_file, [])
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestWorkingSet -v`
Expected: FAIL — `AddItemDial01.__init__` takes no `target` arg; `clear_all_bt` does not clear `base.all_items` and does not call `msg_two_button`.

- [ ] **Step 3a: Give `AddItemDial01` a target dict**

Replace `__init__` (lines 15-19) with:

```python
    def __init__(self, target=None):
        self.temp_dict: dict[str, tuple] = {}
        self.list_of_file: list[str] = []
        self.name_item: str = ""
        self.suffix: str = "s_"
        # The working set this dialog adds items into. Defaults to the shared
        # in-memory working set (the module-level singleton's all_items).
        self.target = target if target is not None else base.all_items
```

- [ ] **Step 3b: Rewrite `add_item_01_bt` (drop preload-from-`all`, use `self.target`)**

Replace the whole `add_item_01_bt` method (lines 293-339) with:

```python
    def add_item_01_bt(self):
        """
        Validate fields and add one entry "<suffix>name": (files...) to the
        target working set. If the name already exists, confirm overwrite.
        """
        self.name_item = self.input_name.text()
        if not self.name_item or not self.list_of_file:
            msg_one_button("WARNING!", "Some fields are empty", 'warn')
            return

        self.name_item = f"{self.suffix}{self.input_name.text()}"
        if self.name_item in self.target:
            reply = msg_two_button("WARNING!",
                                   "This name already exists and will be "
                                   "overwritten if you press 'Yes'\n"
                                   " Press 'No' to cancel")
            if reply != 'yes':
                return
            self.target[self.name_item] = tuple(self.list_of_file)
            msg_one_button("Congradulations!",
                           f"Entry with name: '{self.name_item}'\n was changed",
                           'info')
        else:
            self.target[self.name_item] = tuple(self.list_of_file)
            msg_one_button("Congradulations!",
                           f"Entry with name {self.name_item} successfully "
                           "added to backup base'\n", 'info')

        base.list_saved = True
        self.list_files_and_folders.clear()
        self.list_of_file = []
        self.input_name.clear()
```

- [ ] **Step 3c: Rewrite `clear_all_bt`**

Replace `clear_all_bt` (lines 341-342) with:

```python
    def clear_all_bt(self):
        if not base.all_items and not self.list_of_file:
            self.list_files_and_folders.clear()
            return
        if msg_two_button("Clear All",
                          "Clear the current working list?\n"
                          "Unsaved items will be lost.") != 'yes':
            return
        base.all_items.clear()   # clear in place so target references stay valid
        self.list_of_file = []
        self.temp_dict = {}
        self.list_files_and_folders.clear()
        self.input_name.clear()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestWorkingSet -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add d__01_add_item.py test_named_lists_gui.py
git commit -m "Parameterize AddItemDial01 target; Clear All resets working set

AddItemDial01 now adds into a target dict (default: shared working set),
so it can edit a specific list's copy. Clear All wipes the working set in
place (with confirm). Drops the stale preload-from-'all' in add_item_01_bt.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 5: "Back up all" aggregates every list

**Files:**
- Modify: `MainWindow.py` — add `import backup_lists`; rewrite `backup_all_bt` (lines 66-92 in current file, the method that builds `path` and calls `load_base_from_disk`)
- Test: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing test**

Append to `test_named_lists_gui.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestBackupAll -v`
Expected: FAIL — `test_aggregates...` fails because `backup_all_bt` still reads a single `all` file (which does not exist) and shows the "no lists" message instead of copying; `Alpha`/`Beta` are never created.

- [ ] **Step 3a: Add the import**

In `MainWindow.py`, add near the other imports (after `from main_base import MainBase`):

```python
import backup_lists
```

- [ ] **Step 3b: Rewrite `backup_all_bt`**

Replace the body of `backup_all_bt` so the source becomes the union of all lists, keeping the existing copy logic. The method becomes:

```python
    @staticmethod
    def backup_all_bt():
        """
        Aggregate the items from every saved backup list and copy their files
        and folders into the main backup folder.
        """
        base_dir = MainBase.backup_lists_dir()
        names = backup_lists.list_names(base_dir)
        if not names:
            msg_one_button(NO_LISTS_TITLE, NO_LISTS_TEXT, 'info')
            return

        all_dict = {}
        for name in names:
            all_dict.update(backup_lists.load_list(base_dir, name))  # last wins

        data_dict = {}
        settings_dict = {k[2:]: v for k, v in all_dict.items() if k[0] == 's'}
        if len(settings_dict) != len(all_dict):
            data_dict = {k[2:]: v for k, v in all_dict.items() if k[0] == 'd'}

        for name_item, value_item in settings_dict.items():
            dst_path = Path(f"{MainBase.path_settings_folder}\\{name_item}")
            for _ in value_item:
                if Path.is_file(Path(_)):
                    shutil.copy2(_, dst_path)
                else:
                    shutil.copytree(_, dst_path, dirs_exist_ok=True)
```

(`Path` and `shutil` are already imported at the top of `MainWindow.py`. `NO_LISTS_TITLE`/`NO_LISTS_TEXT` already exist from the earlier bugfix.)

- [ ] **Step 4: Run test to verify it passes**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestBackupAll -v`
Expected: PASS (2 tests).

- [ ] **Step 5: Commit**

```bash
git add MainWindow.py test_named_lists_gui.py
git commit -m "Back up all: aggregate items from every saved list

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 6: Edit dialog — rename and delete a whole list

**Files:**
- Modify: `d__02_edit_list_main.py` — imports; `setupUi` (add buttons + wiring); `retranslateUi`; new `refresh`, `rename_bt_clicked`, `do_rename`, `delete_bt_clicked` methods; switch list population to `backup_lists.list_names`
- Test: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing tests**

Append to `test_named_lists_gui.py`:

```python
class TestEditListManagement(unittest.TestCase):
    def _editor_with_two_lists(self):
        import d__02_edit_list_main as editmod
        MainBase.path_settings_folder = fresh_settings_dir()
        base_dir = MainBase.backup_lists_dir()
        bl.save_list(base_dir, "work_pc", {"s_Word": ["C:/x"]})
        bl.save_list(base_dir, "photos", {"d_Pics": ["D:/p"]})
        ui = editmod.EditListMain()
        ui.setupUi(QDialog())
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestEditListManagement -v`
Expected: FAIL — `EditListMain` has no `delete_bt_clicked` / `do_rename` methods.

- [ ] **Step 3a: Update imports in `d__02_edit_list_main.py`**

The file already imports `os`, `MainBase`, and `msg_one_button, msg_two_button`. Add at the top with the other imports:

```python
import backup_lists
from PySide6.QtWidgets import QInputDialog
```

(`QPushButton`, `QSize` are already imported.)

- [ ] **Step 3b: Populate the list via `backup_lists.list_names`**

In `setupUi`, replace the line:

```python
        self.list_of_backup_lists = os.listdir(self.backup_list_path)
        self.backup_lists.addItems(self.list_of_backup_lists)
```

with:

```python
        self.refresh()
```

- [ ] **Step 3c: Add the Rename and Delete buttons**

In `setupUi`, immediately before `self.horizontalLayout.addWidget(self.ok)` (currently line 75), insert:

```python
        self.rename_bt = QPushButton(Dialog)
        self.rename_bt.setObjectName(u"rename_bt")
        self.rename_bt.setMinimumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.rename_bt)

        self.delete_bt = QPushButton(Dialog)
        self.delete_bt.setObjectName(u"delete_bt")
        self.delete_bt.setMinimumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.delete_bt)
```

- [ ] **Step 3d: Wire the buttons**

In the buttons section (after `self.backup_lists.clicked.connect(self.edit_item_bt)`), add:

```python
        self.rename_bt.clicked.connect(self.rename_bt_clicked)
        self.delete_bt.clicked.connect(self.delete_bt_clicked)
```

- [ ] **Step 3e: Label the buttons**

In `retranslateUi`, after the `self.ok.setText(...)` line, add:

```python
        self.rename_bt.setText(QCoreApplication.translate("Dialog", u"Rename", None))
        self.delete_bt.setText(QCoreApplication.translate("Dialog", u"Delete", None))
```

- [ ] **Step 3f: Add the methods**

Add these methods to `EditListMain` (e.g. after `edit_item_bt`):

```python
    def refresh(self):
        """Reload the list widget from disk."""
        base_dir = MainBase.backup_lists_dir()
        self.list_of_backup_lists = backup_lists.list_names(base_dir)
        self.backup_lists.clear()
        self.backup_lists.addItems(self.list_of_backup_lists)

    def _selected_name(self):
        row = self.backup_lists.currentRow()
        if row < 0:
            return None
        return self.list_of_backup_lists[row]

    def delete_bt_clicked(self):
        name = self._selected_name()
        if name is None:
            return
        if msg_two_button("Delete list",
                          f"Delete the backup list '{name}'?") != 'yes':
            return
        base_dir = MainBase.backup_lists_dir()
        if backup_lists.list_exists(base_dir, name):
            backup_lists.delete_list(base_dir, name)
        self.refresh()

    def rename_bt_clicked(self):
        name = self._selected_name()
        if name is None:
            return
        new_name, ok = QInputDialog.getText(None, "Rename list",
                                            f"New name for '{name}':")
        if ok:
            self.do_rename(name, new_name)

    def do_rename(self, old_name, new_name):
        new_name = (new_name or "").strip()
        base_dir = MainBase.backup_lists_dir()
        if not backup_lists.valid_list_name(new_name):
            msg_one_button("Invalid name",
                           "Please enter a valid list name "
                           "(no \\ / : * ? \" < > | characters).", "warn")
            return
        if backup_lists.list_exists(base_dir, new_name):
            msg_one_button("Name taken",
                           f"A backup list named '{new_name}' already exists.",
                           "warn")
            return
        backup_lists.rename_list(base_dir, old_name, new_name)
        self.refresh()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestEditListManagement -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add d__02_edit_list_main.py test_named_lists_gui.py
git commit -m "Edit dialog: rename and delete whole backup lists

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 7: Per-list item editor — view, delete, add, save items

**Files:**
- Modify: `d__02_edit_list_main.py` — `edit_item_bt` (lines 105-120): load via `backup_lists`, pass the list name
- Modify: `d__02_1_edit_item.py` — imports; `setupUi(self, Dialog, items, name)` (store working copy + name, add buttons, refresh); add `del_item_bt`, `add_item_bt`, `save_bt`, `_refresh_items`; remove the `item_bt` print stub wiring
- Test: `test_named_lists_gui.py`

- [ ] **Step 1: Write the failing tests**

Append to `test_named_lists_gui.py`:

```python
class TestItemEditor(unittest.TestCase):
    def _open_editor(self, items):
        import d__02_1_edit_item as itemmod
        MainBase.path_settings_folder = fresh_settings_dir()
        bl.save_list(MainBase.backup_lists_dir(), "work_pc", items)
        ui = itemmod.ListBackupItemEdit()
        ui.setupUi(QDialog(), dict(items), "work_pc")
        return itemmod, ui

    def test_shows_items(self):
        _itemmod, ui = self._open_editor({"s_Word": ["C:/x"], "d_Pics": ["D:/p"]})
        self.assertEqual(ui.backup_items.count(), 2)

    def test_delete_item_then_save_persists(self):
        itemmod, ui = self._open_editor({"s_Word": ["C:/x"], "d_Pics": ["D:/p"]})
        ui.backup_items.setCurrentRow(0)
        with mock.patch.object(itemmod, "msg_two_button", return_value="yes"):
            ui.del_item_bt()
        with mock.patch.object(itemmod, "msg_one_button"):
            ui.save_bt()
        saved = bl.load_list(MainBase.backup_lists_dir(), "work_pc")
        self.assertEqual(len(saved), 1)

    def test_save_writes_working_copy(self):
        itemmod, ui = self._open_editor({"s_Word": ["C:/x"]})
        ui.items["d_New"] = ["D:/n"]   # simulate an added item
        with mock.patch.object(itemmod, "msg_one_button"):
            ui.save_bt()
        saved = bl.load_list(MainBase.backup_lists_dir(), "work_pc")
        self.assertIn("d_New", saved)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestItemEditor -v`
Expected: FAIL — `setupUi` currently takes `(self, Dialog, ttt)` (no `name`), and there are no `items`, `del_item_bt`, or `save_bt` members.

- [ ] **Step 3a: Update `d__02_1_edit_item.py` imports**

After `import dop_win_rc` (line 5), add:

```python
from PySide6.QtWidgets import QPushButton
from main_base import MainBase
from ui_helpers import msg_one_button, msg_two_button
import backup_lists
```

(The file already imports `QSize` and the other widgets it needs.)

- [ ] **Step 3b: Change `setupUi` signature and store state**

Change the signature on line 9 from:

```python
    def setupUi(self, Dialog, ttt):
```

to:

```python
    def setupUi(self, Dialog, items, name):
```

Then, **after** the `if not Dialog.objectName(): Dialog.setObjectName(u"Dialog")` block (on the line just before `Dialog.resize(400, 800)`, so it always runs), add:

```python
        self.dialog = Dialog
        self.items = items          # working copy of this list's items
        self.name = name            # list (file) name to save back to
        self.base_dir = MainBase.backup_lists_dir()
```

- [ ] **Step 3c: Add Delete / Add / Save buttons**

In `setupUi`, immediately before `self.horizontalLayout.addWidget(self.ok)` (currently line 104), insert:

```python
        self.del_item = QPushButton(Dialog)
        self.del_item.setObjectName(u"del_item")
        self.del_item.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.del_item)

        self.add_item = QPushButton(Dialog)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.add_item)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(110, 60))
        self.horizontalLayout.addWidget(self.save)
```

- [ ] **Step 3d: Replace the button-wiring + item population block**

Replace the current MY CODE (buttons) block (lines 116-122):

```python
        self.backup_items.clicked.connect(self.item_bt)

        self.backup_items.addItems(list(ttt))
        self.ok.clicked.connect(Dialog.reject)
```

with:

```python
        self.ok.clicked.connect(Dialog.reject)
        self.del_item.clicked.connect(self.del_item_bt)
        self.add_item.clicked.connect(self.add_item_bt)
        self.save.clicked.connect(self.save_bt)
        self._refresh_items()
```

- [ ] **Step 3e: Label the new buttons**

In `retranslateUi`, after `self.ok.setText(...)`, add:

```python
        self.del_item.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.add_item.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))
```

- [ ] **Step 3f: Replace the `item_bt` stub with the real handlers**

Replace the `item_bt` method (lines 133-134):

```python
    def item_bt(self):
        print("tttt")
```

with:

```python
    def _refresh_items(self):
        self.backup_items.clear()
        self.backup_items.addItems(list(self.items))

    def del_item_bt(self):
        row = self.backup_items.currentRow()
        if row < 0:
            return
        key = self.backup_items.currentItem().text()
        if msg_two_button("Delete item",
                          f"Remove '{key}' from this list?") != 'yes':
            return
        self.items.pop(key, None)
        self._refresh_items()

    def add_item_bt(self):
        # Local import avoids a load-time import cycle with d__01_add_item.
        from d__01_add_item import AddItemDial01
        from PySide6.QtWidgets import QDialog
        dialog = QDialog()
        ui = AddItemDial01(target=self.items)   # add into THIS list's copy
        ui.setupUi(dialog)
        dialog.exec()
        self._refresh_items()

    def save_bt(self):
        backup_lists.save_list(self.base_dir, self.name, self.items)
        msg_one_button("Saved", f"Backup list '{self.name}' saved", "info")
        self.dialog.accept()
```

- [ ] **Step 3g: Update `edit_item_bt` in `d__02_edit_list_main.py`**

Replace `edit_item_bt` (lines 105-120) with:

```python
    def edit_item_bt(self):
        """When a list is clicked, open the per-list item editor."""
        name = self._selected_name()
        if name is None:
            return
        base_dir = MainBase.backup_lists_dir()
        try:
            items = backup_lists.load_list(base_dir, name)
        except json.decoder.JSONDecodeError:
            msg_one_button("Warning!", "Backup lists file is empty!", "warn")
            return
        dialog = QDialog()
        ui = ListBackupItemEdit()
        ui.setupUi(dialog, items, name)
        dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        dialog.exec()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/Scripts/python.exe -m unittest test_named_lists_gui.TestItemEditor -v`
Expected: PASS (3 tests).
Then run the **entire** suite to confirm nothing regressed:
`./.venv/Scripts/python.exe -m unittest test_backup_lists test_named_lists_gui test_missing_backup_lists -v`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add d__02_1_edit_item.py d__02_edit_list_main.py test_named_lists_gui.py
git commit -m "Per-list item editor: view, delete, add, and save items

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Final verification

- [ ] Run the full suite: `./.venv/Scripts/python.exe -m unittest test_backup_lists test_named_lists_gui test_missing_backup_lists -v` → all PASS.
- [ ] Manual smoke test (real GUI): `./.venv/Scripts/python.exe main.py`
  - Add Item → add a couple of items → Save List → enter a name → confirm it saves.
  - Add Item → Clear All → confirm the working set empties.
  - Edit Backup List → the named list(s) appear → open one (view/delete/add/save), rename one, delete one.
  - Back up all → files from all lists are copied into the settings folder.

## Spec ↔ plan coverage

- Storage layout / `backup_lists.py` seam → Task 1; `backup_lists_dir` → Task 2.
- Name-on-save + validation + overwrite + hide overwrite button + drop hardcoded `all` → Task 3.
- Persistent working set + target dict + Clear All reset + drop preload → Task 4.
- Back up all aggregates every list → Task 5.
- Full management: rename + delete list → Task 6; item add/remove/save → Task 7.
- Error handling (invalid name, collision, empty/corrupt file, missing folder) → Tasks 3, 6, 7 (+ existing bugfix guard).
- Testing strategy (pure unit + headless GUI) → every task.
