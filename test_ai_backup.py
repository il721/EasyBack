"""ai_backup copies a file-based tool's curated files, honouring excludes."""
import os
import tempfile
from pathlib import Path
from ai_backup import expand, backup_tool


def _touch(p, text="x"):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(text, encoding="utf-8")


def run():
    ok = True

    # expand(): %VAR% and leading ~
    if expand("%APPDATA%/aichat", env={"APPDATA": "C:/AD"}, home="C:/Home") != "C:/AD/aichat":
        print("  FAIL expand env"); ok = False
    if expand("~/.claude/settings.json", env={}, home="C:/Home") != "C:/Home/.claude/settings.json":
        print("  FAIL expand home"); ok = False

    home = tempfile.mkdtemp(prefix="aib_home_")
    ai = tempfile.mkdtemp(prefix="aib_ai_")
    _touch(f"{home}/.claude/settings.json", "{}")
    _touch(f"{home}/.claude/skills/foo/SKILL.md", "skill")
    _touch(f"{home}/.claude/.credentials.json", "SECRET")        # must be excluded
    _touch(f"{home}/.claude/plugins/cache/x.bin", "cache")        # must be excluded

    descriptor = {
        "include": ["~/.claude/settings.json", "~/.claude/skills/**"],
        "exclude": ["**/.credentials.json", "**/plugins/cache/**"],
    }
    copied = backup_tool(ai, "claude-code", descriptor, env={}, home=home)

    dest = Path(ai) / "claude-code"
    if not (dest / ".claude/settings.json").is_file():
        print("  FAIL: settings.json not copied"); ok = False
    if not (dest / ".claude/skills/foo/SKILL.md").is_file():
        print("  FAIL: skill not copied"); ok = False
    if (dest / ".claude/.credentials.json").exists():
        print("  FAIL: credentials were copied (must be excluded)"); ok = False
    if any("credential" in c.lower() for c in copied):
        print("  FAIL: credentials in copied list"); ok = False

    print(f"  copied {len(copied)} files")
    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
