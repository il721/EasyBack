"""The popup tags each row with its tool and backs up only the ticked models."""
import os
import tempfile
import json
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from ui_helpers import MovableDialog
from d__ai_settings import AiSettings
from main_base import MainBase
from llm_scan import ScanSections

_app = QApplication.instance() or QApplication(["test"])


def run():
    ok = True
    MainBase.path_settings_folder = tempfile.mkdtemp(prefix="aib_dlg_")

    dlg = MovableDialog()
    ui = AiSettings()
    ui.setupUi(dlg)

    # Feed a fake scan straight into the populate path (no real machine scan).
    s = ScanSections()
    s.ollama_models = ["llama3.2:3b"]
    s.cli_tools = [("claude", "C:/claude.exe")]
    s.cloud = [("anthropic", ["claude-opus"])]
    ui._populate_from_sections(s)

    if ui.found_list.count() != 2:
        print("  FAIL: row count", ui.found_list.count()); ok = False

    # Tick only the ollama model; each row must carry its tool id.
    for i in range(ui.found_list.count()):
        it = ui.found_list.item(i)
        it.setCheckState(Qt.Checked if it.text() == "llama3.2:3b" else Qt.Unchecked)
        if not it.data(Qt.UserRole):
            print("  FAIL: row missing tool id"); ok = False

    pairs = ui._checked_pairs()
    if pairs != [("llama3.2:3b", "ollama")]:
        print("  FAIL: checked pairs", pairs); ok = False

    # Backup writes into <settings>/AI and a manifest.
    ui._do_backup(modelfile=lambda n: "FROM x\n")
    ai = Path(MainBase.ai_dir())
    if not (ai / "ollama" / "models.txt").is_file():
        print("  FAIL: ollama backup not written"); ok = False
    man = json.loads((ai / "MANIFEST.json").read_text(encoding="utf-8"))
    if man["tools"] != ["ollama"]:
        print("  FAIL: manifest tools", man["tools"]); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
