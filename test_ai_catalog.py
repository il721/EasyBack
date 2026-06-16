"""ai_catalog loads the shipped JSON and looks tools up by id."""
from ai_catalog import load_catalog, get_tool


def run():
    cat = load_catalog()
    ok = True

    # Every tool has a label + restore_note; secrets never appear in include lists.
    for tool_id, d in cat.items():
        if "label" not in d or "restore_note" not in d:
            print(f"  FAIL {tool_id}: missing label/restore_note"); ok = False
        for inc in d.get("include", []):
            if "credential" in inc.lower() or inc.lower().endswith("keys.json"):
                print(f"  FAIL {tool_id}: include leaks a secret: {inc}"); ok = False

    claude = get_tool(cat, "claude-code")
    if claude is None or "~/.claude/skills/**" not in claude["include"]:
        print("  FAIL: claude-code missing skills in include"); ok = False
    if "**/.credentials.json" not in claude.get("exclude", []):
        print("  FAIL: claude-code does not exclude credentials"); ok = False
    if get_tool(cat, "ollama").get("special") != "ollama":
        print("  FAIL: ollama not marked special"); ok = False
    if get_tool(cat, "does-not-exist") is not None:
        print("  FAIL: missing tool should be None"); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
