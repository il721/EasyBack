"""export_ai zips the AI folder into one file; import_ai restores it."""
import tempfile
import zipfile
from pathlib import Path
from ai_backup import export_ai, import_ai


def run():
    ok = True
    ai = tempfile.mkdtemp(prefix="aib_exp_")
    (Path(ai) / "claude-code").mkdir(parents=True)
    (Path(ai) / "claude-code/settings.json").write_text("{}", encoding="utf-8")
    (Path(ai) / "MANIFEST.json").write_text('{"tools":["claude-code"]}', encoding="utf-8")

    out = Path(tempfile.mkdtemp(prefix="aib_out_")) / "ai-export.zip"
    export_ai(ai, out)
    if not out.is_file() or out.stat().st_size == 0:
        print("  FAIL: export file not created"); ok = False

    target = tempfile.mkdtemp(prefix="aib_imp_")
    imported = import_ai(out, target)
    if not (Path(target) / "claude-code/settings.json").is_file():
        print("  FAIL: settings.json not restored"); ok = False
    if not (Path(target) / "MANIFEST.json").is_file():
        print("  FAIL: manifest not restored"); ok = False
    if "MANIFEST.json" not in imported:
        print("  FAIL: import did not report manifest"); ok = False

    # Re-import over existing files makes a timestamped backup, does not throw.
    (Path(target) / "claude-code/settings.json").write_text("OLD", encoding="utf-8")
    import_ai(out, target)
    backups = list(Path(target).glob("import-backup-*"))
    if not backups:
        print("  FAIL: existing files not backed up on re-import"); ok = False

    # Zip-slip: a member escaping ai_dir is skipped (not written), no throw.
    evil = Path(tempfile.mkdtemp(prefix="aib_evil_")) / "evil.zip"
    with zipfile.ZipFile(evil, "w") as z:
        z.writestr("../escaped.txt", "PWNED")
        z.writestr("good.txt", "ok")
    sandbox = tempfile.mkdtemp(prefix="aib_slip_")
    import_ai(evil, sandbox)  # must not raise
    escaped = Path(sandbox).parent / "escaped.txt"
    if escaped.exists():
        print("  FAIL: zip-slip wrote outside ai_dir"); ok = False
        escaped.unlink()  # clean up the leak so reruns aren't poisoned
    if not (Path(sandbox) / "good.txt").is_file():
        print("  FAIL: safe member not extracted"); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
