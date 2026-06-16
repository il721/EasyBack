"""backup_selected dispatches each ticked model to its tool and writes a manifest."""
import json
import tempfile
from pathlib import Path
from ai_catalog import load_catalog
from ai_backup import backup_selected


def run():
    ok = True
    cat = load_catalog()
    ai = tempfile.mkdtemp(prefix="aib_sel_")

    # Ticked models -> their tools (claude cloud + two ollama).
    pairs = [("claude-opus", "claude-code"),
             ("claude-sonnet", "claude-code"),
             ("llama3.2:3b", "ollama")]

    home = tempfile.mkdtemp(prefix="aib_selhome_")
    (Path(home) / ".claude").mkdir(parents=True)
    (Path(home) / ".claude/settings.json").write_text("{}", encoding="utf-8")

    result = backup_selected(
        ai, pairs, cat,
        env={}, home=home,
        modelfile=lambda n: "FROM x\n",
    )

    man = json.loads((Path(ai) / "MANIFEST.json").read_text(encoding="utf-8"))
    if set(man["tools"]) != {"claude-code", "ollama"}:
        print("  FAIL: manifest tools", man["tools"]); ok = False
    if man["models"].get("ollama") != ["llama3.2:3b"]:
        print("  FAIL: manifest ollama models", man.get("models")); ok = False
    if "secrets" not in man["note"].lower():
        print("  FAIL: manifest note should mention secrets excluded"); ok = False
    if not (Path(ai) / "ollama" / "models.txt").is_file():
        print("  FAIL: ollama not backed up"); ok = False
    if not (Path(ai) / "claude-code").is_dir():
        print("  FAIL: claude-code not backed up"); ok = False
    if "claude-code" not in result["restore_notes"]:
        print("  FAIL: restore_notes missing claude-code"); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
