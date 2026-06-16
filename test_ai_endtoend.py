"""End-to-end: scan map -> backup -> export -> import round trip, real catalog."""
import os
import tempfile
import json
from pathlib import Path

from ai_catalog import load_catalog, get_tool
from ai_backup import backup_selected, export_ai, import_ai


def run():
    ok = True
    cat = load_catalog()

    # Every tool referenced by llm_scan's provider/runtime mapping must exist.
    required = ["claude-code", "ollama", "lmstudio", "gpt4all", "jan", "aichat",
                "llm", "anthropic-cloud", "openai-cloud", "google-cloud",
                "mistral-cloud", "groq-cloud", "local-weights"]
    for t in required:
        if get_tool(cat, t) is None:
            print(f"  FAIL: catalog missing {t}"); ok = False

    home = tempfile.mkdtemp(prefix="e2e_home_")
    (Path(home) / ".claude/skills/s").mkdir(parents=True)
    (Path(home) / ".claude/settings.json").write_text("{}", encoding="utf-8")
    (Path(home) / ".claude/skills/s/SKILL.md").write_text("x", encoding="utf-8")
    (Path(home) / ".claude/.credentials.json").write_text("SECRET", encoding="utf-8")

    ai = tempfile.mkdtemp(prefix="e2e_ai_")
    pairs = [("claude-opus", "claude-code"), ("llama3.2:3b", "ollama"),
             ("gpt-4o", "openai-cloud")]
    backup_selected(ai, pairs, cat, env=os.environ, home=home,
                    modelfile=lambda n: "FROM x\n")

    # Secret must never be in the backup.
    leaked = list(Path(ai).rglob(".credentials.json"))
    if leaked:
        print("  FAIL: secret leaked into backup:", leaked); ok = False

    out = Path(tempfile.mkdtemp(prefix="e2e_out_")) / "ai.zip"
    export_ai(ai, out)
    target = tempfile.mkdtemp(prefix="e2e_imp_")
    import_ai(out, target)

    if not (Path(target) / "claude-code/.claude/settings.json").is_file():
        print("  FAIL: round-trip lost settings.json"); ok = False
    man = json.loads((Path(target) / "MANIFEST.json").read_text(encoding="utf-8"))
    if set(man["tools"]) != {"claude-code", "ollama", "openai-cloud"}:
        print("  FAIL: round-trip manifest tools", man["tools"]); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
