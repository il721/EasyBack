"""
One-off reproduction / regression test.

Bug: clicking "Edit backup list" or "Back up all" before any backup list has
been saved crashes with FileNotFoundError, because the `backup_lists` folder and
its per-list files are only created lazily on the first save (backup_lists.save_list).

Two scenarios are checked, both headless (GUI message box + modal exec stubbed):

  EMPTY  settings folder has NO backup_lists -> handler must NOT crash and must
         show the "no backup lists yet" message.
  POPULATED  backup_lists/all exists -> handler must proceed WITHOUT showing that
         message (guards against a false warning / regression of normal flow).

Run: .venv/Scripts/python.exe test_missing_backup_lists.py
"""
import os
import json
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")  # no real windows

from PySide6.QtWidgets import QApplication, QDialog

import MainWindow
from main_base import MainBase

_app = QApplication.instance() or QApplication(["test"])
QDialog.exec = lambda self: 0  # don't block on modal dialogs in the populated case

HANDLERS = (("edit_list_bt", MainWindow.MainWindowDialog.edit_list_bt),
            ("backup_all_bt", MainWindow.MainWindowDialog.backup_all_bt))


def _install_msg_stub():
    calls = []
    MainWindow.msg_one_button = lambda *a, **k: calls.append((a, k))
    return calls


def empty_case():
    tmp = tempfile.mkdtemp(prefix="easyback_test_empty_")
    MainBase.path_settings_folder = tmp
    calls = _install_msg_stub()
    results = {}
    for name, fn in HANDLERS:
        before = len(calls)
        try:
            fn()
            results[name] = ("OK (message shown)" if len(calls) > before
                             else "FAIL (no crash but no message shown)")
        except Exception as e:
            results[name] = f"FAIL CRASH: {type(e).__name__}: {e}"
    return results


def populated_case():
    tmp = tempfile.mkdtemp(prefix="easyback_test_pop_")
    os.mkdir(os.path.join(tmp, "backup_lists"))
    with open(os.path.join(tmp, "backup_lists", "all"), "w") as f:
        json.dump({}, f)  # empty base -> backup_all does no copying
    MainBase.path_settings_folder = tmp
    calls = _install_msg_stub()
    results = {}
    for name, fn in HANDLERS:
        before = len(calls)
        try:
            fn()
            results[name] = ("OK (proceeded, no warning)" if len(calls) == before
                             else "FAIL (warned even though list exists)")
        except Exception as e:
            results[name] = f"FAIL CRASH: {type(e).__name__}: {e}"
    return results


def run():
    ok = True
    for label, results in (("EMPTY (no backup_lists folder)", empty_case()),
                           ("POPULATED (backup_lists/all exists)", populated_case())):
        print(f"=== {label} ===")
        for name, res in results.items():
            print(f"  {name:15} -> {res}")
            if not res.startswith("OK"):
                ok = False
    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
