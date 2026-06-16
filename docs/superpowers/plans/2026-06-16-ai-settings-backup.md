# AI Settings Backup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** From the AI Settings popup, back up the settings/skills/plugins of the checked AI models into a new `AI` folder inside the main settings folder, and export/import that folder as one transferable file.

**Architecture:** Detection stays in `llm_scan.py` (code); *what to back up per tool* lives in a data-driven `ai_catalog.json` (so new online models/tools are a data edit, not code). A pure leaf module `ai_backup.py` copies each selected tool's curated files into `{settings}\AI\<tool_id>\`, handles Ollama specially (variant A: save each model's Modelfile recipe + name, no weights), excludes secrets, writes a `MANIFEST.json`, and zips/unzips the folder for export/import. The popup maps each checked model to its owning tool and drives the backup.

**Tech Stack:** Python 3, PySide6 (Qt), stdlib only (`json`, `glob`, `fnmatch`, `shutil`, `zipfile`, `subprocess`). Tests are standalone scripts run with `.venv/Scripts/python.exe`, matching the existing `test_*.py` convention (no pytest).

**Settled decisions (from design discussion):**
- Group by tool: cloud providers = one unit; Ollama = one unit.
- Ollama = **variant A** — save Modelfile recipe + model name, re-pull weights on restore.
- **Exclude secrets** (`.credentials.json`, `keys.json`, API keys) — re-login/re-key on restore.
- **Full, data-driven catalog** (Claude Code, Ollama, LM Studio, GPT4All, Jan, aichat, llm, cloud providers, loose weights), extensible to future tools via JSON.
- All output under `{path_settings_folder}\AI\`.

---

## File Structure

- Create `ai_catalog.json` — data: per-tool `label`, `include`/`exclude` globs, `restore_note`, `special`.
- Create `ai_catalog.py` — pure loader: `load_catalog()`, `get_tool()`.
- Modify `llm_scan.py` — expose `scan_sections()`, add `model_tool_map()`, add `ollama_modelfile()`.
- Create `ai_backup.py` — pure leaf engine: path expansion, file selection, per-tool backup, Ollama/weights specials, manifest, export/import. No Qt, no MainBase.
- Modify `main_base.py` — add `MainBase.ai_dir()`.
- Modify `d__ai_settings.py` — tag each model row with its tool, add Backup / Export / Import buttons + handlers.
- Create tests: `test_ai_catalog.py`, `test_llm_tool_map.py`, `test_ai_backup.py`, `test_ai_export.py`, `test_ai_settings_dialog.py`.

Conventions to follow:
- `ai_backup.py` and `ai_catalog.py` are **leaf modules** (no Qt, no `MainBase`), like `backup_lists.py`. All filesystem/subprocess I/O is injected as callables so tests use fakes (same approach as `scan_local_llms`).
- Run any test with: `.venv/Scripts/python.exe <test_file>.py` (exit 0 = pass).

---

### Task 1: AI folder location on MainBase

**Files:**
- Modify: `main_base.py` (next to `backup_lists_dir`, ~`main_base.py:193-196`)
- Test: `test_ai_dir.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_dir.py`:
```python
"""MainBase.ai_dir() returns the AI folder inside the settings folder."""
from main_base import MainBase


def run():
    MainBase.path_settings_folder = r"C:\some\settings"
    got = MainBase.ai_dir()
    expected = r"C:\some\settings\AI"
    print("ai_dir ->", got)
    ok = got == expected
    print("RESULT:", "PASS" if ok else f"FAIL (expected {expected})")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_dir.py`
Expected: FAIL — `AttributeError: type object 'MainBase' has no attribute 'ai_dir'`.

- [ ] **Step 3: Add the classmethod**

In `main_base.py`, immediately after the `backup_lists_dir` classmethod (around line 196), add:
```python
    @classmethod
    def ai_dir(cls) -> str:
        """Folder that holds backed-up AI-model settings (one subfolder per tool)."""
        return f"{cls.path_settings_folder}\\AI"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_dir.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Commit**

```bash
git add main_base.py test_ai_dir.py
git commit -m "feat: MainBase.ai_dir() points at the AI settings folder"
```

---

### Task 2: Ship the data-driven tool catalog + loader

**Files:**
- Create: `ai_catalog.json`
- Create: `ai_catalog.py`
- Test: `test_ai_catalog.py`

- [ ] **Step 1: Write the catalog data file**

Create `ai_catalog.json`:
```json
{
  "claude-code": {
    "label": "Claude Code",
    "kind": "client",
    "include": [
      "~/.claude/settings.json",
      "~/.claude/CLAUDE.md",
      "~/.claude/skills/**",
      "~/.claude/agents/**",
      "~/.claude/rules/**",
      "~/.claude/commands/**",
      "~/.claude/plugins/installed_plugins.json",
      "~/.claude/plugins/known_marketplaces.json",
      "~/.claude/statusline_model.ps1",
      "~/.claude/widget_limits.json",
      "~/.claude/widget_pos.txt",
      "~/.claude/widget_opacity.txt",
      "~/.claude/widget_simple.txt"
    ],
    "exclude": [
      "**/.credentials.json",
      "**/plugins/cache/**",
      "**/plugins/repos/**"
    ],
    "restore_note": "Re-add marketplaces and /plugin install your plugins, then run `claude` to log in again."
  },
  "ollama": {
    "label": "Ollama",
    "kind": "runtime",
    "special": "ollama",
    "restore_note": "Run `ollama pull <name>` (or `ollama create` from the saved Modelfile) for each model."
  },
  "lmstudio": {
    "label": "LM Studio",
    "kind": "runtime",
    "include": ["~/.lmstudio/**"],
    "exclude": ["**/models/**", "**/.cache/**"],
    "restore_note": "Re-download models in LM Studio; presets/config are restored."
  },
  "gpt4all": {
    "label": "GPT4All",
    "kind": "runtime",
    "include": ["%LOCALAPPDATA%/nomic.ai/GPT4All/**"],
    "exclude": ["**/*.gguf", "**/*.bin"],
    "restore_note": "Re-download models in GPT4All; settings are restored."
  },
  "jan": {
    "label": "Jan",
    "kind": "runtime",
    "include": ["~/.jan/**"],
    "exclude": ["**/models/**"],
    "restore_note": "Re-download models in Jan; assistants/threads/settings are restored."
  },
  "aichat": {
    "label": "aichat",
    "kind": "client",
    "include": ["%APPDATA%/aichat/**", "~/.config/aichat/**"],
    "exclude": ["**/*.key", "**/secrets*"],
    "restore_note": "Set your provider API keys again; roles/sessions/config are restored."
  },
  "llm": {
    "label": "llm (datasette)",
    "kind": "client",
    "include": ["%APPDATA%/io.datasette.llm/**", "~/.config/io.datasette.llm/**"],
    "exclude": ["**/keys.json"],
    "restore_note": "Run `llm keys set <provider>` again; templates/plugins/logs are restored."
  },
  "anthropic-cloud": {
    "label": "Anthropic API",
    "kind": "cloud",
    "include": [],
    "restore_note": "Set ANTHROPIC_API_KEY on the new machine."
  },
  "openai-cloud": {
    "label": "OpenAI API",
    "kind": "cloud",
    "include": [],
    "restore_note": "Set OPENAI_API_KEY on the new machine."
  },
  "google-cloud": {
    "label": "Google AI API",
    "kind": "cloud",
    "include": [],
    "restore_note": "Set GEMINI_API_KEY / GOOGLE_API_KEY on the new machine."
  },
  "mistral-cloud": {
    "label": "Mistral API",
    "kind": "cloud",
    "include": [],
    "restore_note": "Set MISTRAL_API_KEY on the new machine."
  },
  "groq-cloud": {
    "label": "Groq API",
    "kind": "cloud",
    "include": [],
    "restore_note": "Set GROQ_API_KEY on the new machine."
  },
  "local-weights": {
    "label": "Local weight files",
    "kind": "weights",
    "special": "weights",
    "restore_note": "Re-download the listed .gguf/.safetensors files; only their paths are recorded."
  }
}
```

- [ ] **Step 2: Write the failing test**

Create `test_ai_catalog.py`:
```python
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
```

- [ ] **Step 3: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_catalog.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'ai_catalog'`.

- [ ] **Step 4: Write the loader**

Create `ai_catalog.py`:
```python
"""Loader for the data-driven AI tool catalog (ai_catalog.json).

Pure: no Qt, no MainBase. The catalog says WHAT to back up per tool (include /
exclude path globs + a restore note); detection of which tool a model belongs to
lives in llm_scan.model_tool_map. Add a new tool/online model by editing the
JSON — no code change.
"""
import json
from pathlib import Path

DEFAULT_CATALOG_PATH = Path(__file__).with_name("ai_catalog.json")


def load_catalog(path=DEFAULT_CATALOG_PATH) -> dict:
    """Return {tool_id: descriptor} parsed from the catalog JSON (UTF-8)."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_tool(catalog: dict, tool_id: str):
    """Descriptor for tool_id, or None if it is not in the catalog."""
    return catalog.get(tool_id)
```

- [ ] **Step 5: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_catalog.py`
Expected: `RESULT: PASS`

- [ ] **Step 6: Commit**

```bash
git add ai_catalog.json ai_catalog.py test_ai_catalog.py
git commit -m "feat: data-driven AI tool catalog + loader"
```

---

### Task 3: Map found models to their owning tool (+ Ollama Modelfile reader)

**Files:**
- Modify: `llm_scan.py` (refactor `scan_local_llms`; add `scan_sections`, `model_tool_map`, `ollama_modelfile`)
- Test: `test_llm_tool_map.py`

- [ ] **Step 1: Write the failing test**

Create `test_llm_tool_map.py`:
```python
"""model_tool_map groups found models under the tool that owns their settings."""
from llm_scan import ScanSections, model_tool_map, ollama_modelfile


def run():
    ok = True
    s = ScanSections()
    s.ollama_models = ["qwen3.5:4b", "llama3.2:3b"]
    s.runtimes = [("LM Studio", ["TheBloke/x"]), ("Jan", ["jan-model"])]
    s.weights = [("C:/w/foo.gguf", 1.2)]
    s.cli_tools = [("claude", "C:/claude.exe"), ("ollama", "C:/ollama.exe")]
    s.cloud = [("anthropic", ["claude-opus", "claude-sonnet"]),
               ("openai", ["gpt-4o"])]

    m = model_tool_map(s)
    expect = {
        "qwen3.5:4b": "ollama",
        "llama3.2:3b": "ollama",
        "TheBloke/x": "lmstudio",
        "jan-model": "jan",
        "foo": "local-weights",
        "claude-opus": "claude-code",   # claude CLI present -> Claude Code
        "claude-sonnet": "claude-code",
        "gpt-4o": "openai-cloud",
    }
    for k, v in expect.items():
        if m.get(k) != v:
            print(f"  FAIL {k}: got {m.get(k)!r}, want {v!r}"); ok = False

    # Without the claude CLI, anthropic falls back to the cloud tool.
    s2 = ScanSections()
    s2.cloud = [("anthropic", ["claude-opus"])]
    if model_tool_map(s2).get("claude-opus") != "anthropic-cloud":
        print("  FAIL: anthropic w/o claude CLI should be anthropic-cloud"); ok = False

    # ollama_modelfile shells out via injected run; returns the text or None.
    class P:
        returncode = 0
        stdout = "FROM x\nSYSTEM you are helpful\n"
    txt = ollama_modelfile("llama3.2:3b", run=lambda *a, **k: P(),
                           which=lambda n: "C:/ollama.exe")
    if "SYSTEM you are helpful" not in txt:
        print("  FAIL: ollama_modelfile text"); ok = False
    if ollama_modelfile("x", run=lambda *a, **k: P(), which=lambda n: None) is not None:
        print("  FAIL: no ollama CLI -> None"); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_llm_tool_map.py`
Expected: FAIL — `ImportError: cannot import name 'model_tool_map' from 'llm_scan'`.

- [ ] **Step 3: Refactor scan + add the new functions**

In `llm_scan.py`, replace the body of `scan_local_llms` so the I/O lives in a reusable `scan_sections`, and add the two new helpers. Replace this block:

```python
def scan_local_llms(*, env=None, which=shutil.which, run=subprocess.run, home=None):
    """Scan the machine for LLMs. Returns (report_text, model_names).

    All I/O is via injected callables so tests pass fakes. No individual probe
    failure may raise: each degrades to a 'none/unreachable' line.
    """
    env = os.environ if env is None else env
    home_fn = Path.home if home is None else home
    home_dir = Path(home_fn())
    sections = ScanSections()
```

with:

```python
def scan_sections(*, env=None, which=shutil.which, run=subprocess.run, home=None):
    """Scan the machine and return the raw ScanSections (all I/O injected)."""
    env = os.environ if env is None else env
    home_fn = Path.home if home is None else home
    home_dir = Path(home_fn())
    sections = ScanSections()
```

Then change the final line of that function from:

```python
    return build_report(sections), collect_models(sections)
```

to:

```python
    return sections


def scan_local_llms(*, env=None, which=shutil.which, run=subprocess.run, home=None):
    """Scan the machine for LLMs. Returns (report_text, model_names)."""
    sections = scan_sections(env=env, which=which, run=run, home=home)
    return build_report(sections), collect_models(sections)


_RUNTIME_TOOL = {
    "LM Studio": "lmstudio",
    "LM Studio (cache)": "lmstudio",
    "GPT4All": "gpt4all",
    "Jan": "jan",
}

_PROVIDER_CLOUD_TOOL = {
    "anthropic": "anthropic-cloud",
    "openai": "openai-cloud",
    "google": "google-cloud",
    "mistral": "mistral-cloud",
    "groq": "groq-cloud",
}


def model_tool_map(sections) -> dict:
    """Return {model_name: tool_id} mapping each found model to the tool that
    owns its settings. First-seen wins, mirroring collect_models()."""
    mapping = {}

    def put(name, tool):
        if name and name not in mapping:
            mapping[name] = tool

    for name in sections.ollama_models:
        put(name, "ollama")
    for rname, entries in sections.runtimes:
        for e in entries:
            put(e, _RUNTIME_TOOL.get(rname, "local-weights"))
    for path, _gb in sections.weights:
        put(Path(path).stem, "local-weights")

    has_claude_cli = any(name == "claude" for name, _ in sections.cli_tools)
    for provider, variants in sections.cloud:
        if provider == "anthropic" and has_claude_cli:
            tool = "claude-code"
        else:
            tool = _PROVIDER_CLOUD_TOOL.get(provider, f"{provider}-cloud")
        for v in variants:
            put(v, tool)
    return mapping


def ollama_modelfile(name, *, run=subprocess.run, which=shutil.which):
    """Return `ollama show --modelfile <name>` text, or None if ollama is absent
    or the call fails. This is a model's full recipe (FROM/TEMPLATE/PARAMETER/
    SYSTEM) — variant A backs this up instead of the weights."""
    if not which("ollama"):
        return None
    try:
        proc = run(["ollama", "show", "--modelfile", name],
                   capture_output=True, text=True, timeout=30)
        if proc.returncode == 0:
            return proc.stdout
    except Exception:  # noqa: BLE001 - any failure -> nothing to back up
        return None
    return None
```

- [ ] **Step 4: Run both the new and old scan tests to verify pass**

Run: `.venv/Scripts/python.exe test_llm_tool_map.py`
Expected: `RESULT: PASS`

Run (regression — the existing dialog/scan still works):
```
.venv/Scripts/python.exe -c "from llm_scan import scan_local_llms; r,m=scan_local_llms(env={}, which=lambda n: None, home=lambda: '.'); print('scan ok', type(m))"
```
Expected: prints `scan ok <class 'list'>` (no exception).

- [ ] **Step 5: Commit**

```bash
git add llm_scan.py test_llm_tool_map.py
git commit -m "feat: map found models to owning tool; read Ollama Modelfiles"
```

---

### Task 4: ai_backup — path expansion + file-based tool copy

**Files:**
- Create: `ai_backup.py`
- Test: `test_ai_backup.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_backup.py`:
```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_backup.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'ai_backup'`.

- [ ] **Step 3: Write the module (expansion + file copy)**

Create `ai_backup.py`:
```python
"""Engine that backs up AI-model settings into the AI folder, and exports /
imports that folder as one file.

Pure leaf module: no Qt, no MainBase. All filesystem / subprocess work is taken
as injected callables (mirrors backup_lists.py and llm_scan.scan_sections) so the
logic is unit-testable with fakes. Secrets are excluded by catalog rules; nothing
here ever copies a credential by design.

Layout produced under <ai_dir>:
    <ai_dir>/<tool_id>/...            curated files for a file-based tool
    <ai_dir>/ollama/models/<name>.modelfile   + models.txt   (variant A)
    <ai_dir>/local-weights/weights_paths.txt
    <ai_dir>/MANIFEST.json
"""
import fnmatch
import glob
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

_ENV_RE = re.compile(r"%([^%]+)%")


def expand(spec: str, *, env, home) -> str:
    """Expand %VAR% (from env) and a leading ~ (to home) in a path spec.

    Returns forward-slash form; glob/Path handle that on Windows.
    """
    s = spec.replace("\\", "/")
    s = _ENV_RE.sub(lambda m: str(env.get(m.group(1), "")).replace("\\", "/"), s)
    if s.startswith("~"):
        s = str(home).replace("\\", "/").rstrip("/") + s[1:]
    return s


def _excluded(path: str, exclude_globs) -> bool:
    p = path.replace("\\", "/")
    return any(fnmatch.fnmatch(p, pat) or fnmatch.fnmatch(p, "*/" + pat.lstrip("*/"))
               for pat in exclude_globs)


def _iter_files(include_globs, exclude_globs, *, env, home):
    """Yield absolute file paths matching include globs minus exclude globs."""
    seen = set()
    for spec in include_globs:
        pattern = expand(spec, env=env, home=home)
        for hit in glob.glob(pattern, recursive=True):
            if not os.path.isfile(hit):
                continue
            ap = os.path.abspath(hit)
            if ap in seen or _excluded(ap, exclude_globs):
                continue
            seen.add(ap)
            yield ap


def _rel_under_home(abs_path: str, home) -> str:
    """Path relative to home if it lives under home, else a flattened drive form."""
    home_abs = os.path.abspath(str(home))
    ap = os.path.abspath(abs_path)
    try:
        return os.path.relpath(ap, home_abs)
    except ValueError:           # different drive
        return ap.replace(":", "").replace("\\", "/").lstrip("/")


def backup_tool(ai_dir, tool_id, descriptor, *, env, home, copy=shutil.copy2) -> list:
    """Copy a file-based tool's curated files into <ai_dir>/<tool_id>/.

    Returns the list of relative destination paths written. Tools with no
    `include` (e.g. cloud providers) write nothing and return []."""
    include = descriptor.get("include", [])
    exclude = descriptor.get("exclude", [])
    dest_root = Path(ai_dir) / tool_id
    written = []
    for src in _iter_files(include, exclude, env=env, home=home):
        rel = _rel_under_home(src, home)
        dst = dest_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        copy(src, dst)
        written.append(rel.replace("\\", "/"))
    return written
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_backup.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Commit**

```bash
git add ai_backup.py test_ai_backup.py
git commit -m "feat: ai_backup file-based tool copy with secret-excluding globs"
```

---

### Task 5: ai_backup — Ollama (variant A) + local-weights specials

**Files:**
- Modify: `ai_backup.py`
- Test: `test_ai_backup_ollama.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_backup_ollama.py`:
```python
"""Ollama backup saves each model's Modelfile recipe + a names list (variant A)."""
import tempfile
from pathlib import Path
from ai_backup import backup_ollama, backup_local_weights


def run():
    ok = True
    ai = tempfile.mkdtemp(prefix="aib_oll_")

    recipes = {"llama3.2:3b": "FROM x\nSYSTEM hi\n", "qwen3.5:4b": "FROM y\n"}
    written = backup_ollama(ai, ["llama3.2:3b", "qwen3.5:4b"],
                            modelfile=lambda n: recipes.get(n))

    base = Path(ai) / "ollama" / "models"
    # ":" is illegal in Windows filenames -> sanitised to "_".
    if not (base / "llama3.2_3b.modelfile").is_file():
        print("  FAIL: modelfile not written"); ok = False
    if "SYSTEM hi" not in (base / "llama3.2_3b.modelfile").read_text(encoding="utf-8"):
        print("  FAIL: modelfile content"); ok = False
    names = (Path(ai) / "ollama" / "models.txt").read_text(encoding="utf-8")
    if "llama3.2:3b" not in names or "qwen3.5:4b" not in names:
        print("  FAIL: models.txt missing names"); ok = False
    if len(written) != 2:
        print("  FAIL: written count"); ok = False

    # A model whose recipe can't be read is still listed (re-pull by name).
    w2 = backup_ollama(ai, ["ghost:1b"], modelfile=lambda n: None)
    if "ghost:1b" not in (Path(ai) / "ollama" / "models.txt").read_text(encoding="utf-8"):
        print("  FAIL: name-only model not listed"); ok = False

    # local-weights records paths only (variant A — no copy).
    backup_local_weights(ai, ["C:/w/a.gguf", "C:/w/b.safetensors"])
    wp = (Path(ai) / "local-weights" / "weights_paths.txt").read_text(encoding="utf-8")
    if "a.gguf" not in wp or "b.safetensors" not in wp:
        print("  FAIL: weights_paths.txt"); ok = False

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_backup_ollama.py`
Expected: FAIL — `ImportError: cannot import name 'backup_ollama' from 'ai_backup'`.

- [ ] **Step 3: Add the specials to `ai_backup.py`**

Append to `ai_backup.py`:
```python
_FNAME_BAD = re.compile(r'[\\/:*?"<>|]')


def _safe_filename(name: str) -> str:
    """Make a model name safe as a Windows filename (e.g. 'llama3.2:3b')."""
    return _FNAME_BAD.sub("_", name)


def backup_ollama(ai_dir, model_names, *, modelfile) -> list:
    """Variant A: save each model's Modelfile recipe + a names list.

    `modelfile` is a callable name -> recipe_text|None (see
    llm_scan.ollama_modelfile). Models with no readable recipe are still listed
    in models.txt so they can be re-pulled by name. Returns recipe files written.
    """
    root = Path(ai_dir) / "ollama"
    models_dir = root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for name in model_names:
        text = modelfile(name)
        if text:
            f = models_dir / f"{_safe_filename(name)}.modelfile"
            f.write_text(text, encoding="utf-8")
            written.append(name)
    (root / "models.txt").write_text("\n".join(model_names) + "\n", encoding="utf-8")
    return written


def backup_local_weights(ai_dir, paths) -> None:
    """Record loose weight-file paths only (variant A — files are not copied)."""
    root = Path(ai_dir) / "local-weights"
    root.mkdir(parents=True, exist_ok=True)
    (root / "weights_paths.txt").write_text("\n".join(paths) + "\n", encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_backup_ollama.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Commit**

```bash
git add ai_backup.py test_ai_backup_ollama.py
git commit -m "feat: Ollama variant-A backup (Modelfiles + names) and local-weights paths"
```

---

### Task 6: ai_backup — orchestrator + manifest

**Files:**
- Modify: `ai_backup.py`
- Test: `test_ai_backup_selected.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_backup_selected.py`:
```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_backup_selected.py`
Expected: FAIL — `ImportError: cannot import name 'backup_selected' from 'ai_backup'`.

- [ ] **Step 3: Add the orchestrator to `ai_backup.py`**

Append to `ai_backup.py`:
```python
def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def backup_selected(ai_dir, model_tool_pairs, catalog, *, env, home,
                    modelfile, now=_now_iso) -> dict:
    """Back up every tool referenced by the ticked (model, tool_id) pairs.

    Groups pairs by tool, runs the right backup per tool kind (file-based copy,
    Ollama variant A, or local-weights), then writes MANIFEST.json. Returns
    {"tools": [...], "models": {tool: [...]}, "restore_notes": {tool: str}}.
    """
    Path(ai_dir).mkdir(parents=True, exist_ok=True)

    by_tool = {}
    for model, tool_id in model_tool_pairs:
        by_tool.setdefault(tool_id, []).append(model)

    restore_notes = {}
    for tool_id, models in by_tool.items():
        descriptor = catalog.get(tool_id, {})
        special = descriptor.get("special")
        if special == "ollama":
            backup_ollama(ai_dir, models, modelfile=modelfile)
        elif special == "weights":
            backup_local_weights(ai_dir, models)
        else:
            backup_tool(ai_dir, tool_id, descriptor, env=env, home=home)
        if descriptor.get("restore_note"):
            restore_notes[tool_id] = descriptor["restore_note"]

    manifest = {
        "exportedAt": now(),
        "tools": sorted(by_tool),
        "models": {t: sorted(set(ms)) for t, ms in by_tool.items()},
        "restore_notes": restore_notes,
        "note": ("Portable AI settings. Secrets (API keys, credentials) were "
                 "intentionally excluded; re-login / re-key on the target machine."),
    }
    with open(Path(ai_dir) / "MANIFEST.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return {"tools": manifest["tools"], "models": manifest["models"],
            "restore_notes": restore_notes}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_backup_selected.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Commit**

```bash
git add ai_backup.py test_ai_backup_selected.py
git commit -m "feat: backup_selected orchestrator writes per-tool backups + manifest"
```

---

### Task 7: ai_backup — export to one file + import

**Files:**
- Modify: `ai_backup.py`
- Test: `test_ai_export.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_export.py`:
```python
"""export_ai zips the AI folder into one file; import_ai restores it."""
import tempfile
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

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_export.py`
Expected: FAIL — `ImportError: cannot import name 'export_ai' from 'ai_backup'`.

- [ ] **Step 3: Add export/import to `ai_backup.py`**

Add `import zipfile` to the imports at the top of `ai_backup.py`, then append:
```python
def export_ai(ai_dir, out_file) -> str:
    """Zip the whole AI folder into a single file at out_file. Returns out_file."""
    ai_dir = Path(ai_dir)
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        out_file.unlink()
    with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as z:
        for f in ai_dir.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(ai_dir).as_posix())
    return str(out_file)


def import_ai(in_file, ai_dir, *, backup_existing=True) -> list:
    """Extract an exported AI zip into ai_dir, backing up any file it overwrites
    into a timestamped import-backup-* folder. Returns the archive member names."""
    ai_dir = Path(ai_dir)
    ai_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = ai_dir / f"import-backup-{stamp}"
    names = []
    with zipfile.ZipFile(in_file, "r") as z:
        for member in z.namelist():
            if member.endswith("/"):
                continue
            target = ai_dir / member
            if backup_existing and target.is_file():
                bk = backup_root / member
                bk.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(target, bk)
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(member) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            names.append(member)
    return names
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_export.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Commit**

```bash
git add ai_backup.py test_ai_export.py
git commit -m "feat: export AI folder to one zip + import with overwrite backup"
```

---

### Task 8: Wire backup / export / import into the AI Settings popup

**Files:**
- Modify: `d__ai_settings.py`
- Test: `test_ai_settings_dialog.py`

- [ ] **Step 1: Write the failing test**

Create `test_ai_settings_dialog.py`:
```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python.exe test_ai_settings_dialog.py`
Expected: FAIL — `AttributeError: 'AiSettings' object has no attribute '_populate_from_sections'`.

- [ ] **Step 3: Update `d__ai_settings.py`**

3a. Replace the imports block at the top with:
```python
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread,
                            Signal)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QFileDialog, QHBoxLayout, QLabel, QListWidget,
                               QListWidgetItem, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)
import dop_win_rc
from all_styles import SETTINGS_MAIN
from ui_helpers import msg_one_button
from main_base import MainBase
from ai_catalog import load_catalog
from ai_backup import backup_selected, export_ai, import_ai
from llm_scan import scan_sections, collect_models, model_tool_map, ollama_modelfile
```

3b. Change `_ScanWorker.run` to return the sections object instead of `(report, models)`:
```python
    def run(self):
        try:
            self.done.emit(scan_sections())
        except Exception as exc:  # noqa: BLE001 - report any failure to the UI
            self.failed.emit(str(exc))
```

3c. In `setupUi`, after `self._worker = None`, add:
```python
        self._tool_map = {}          # model name -> tool id (from last scan)
        self._catalog = load_catalog()
```

3d. Add the three action buttons. Insert this block right after the `self.find_llm` button is added to `self.horizontalLayout` (after `self.horizontalLayout.addWidget(self.find_llm)`), before the `self.ok` button is created:
```python
        self.backup_bt = QPushButton(Dialog)
        self.backup_bt.setObjectName(u"backup_bt")
        self.backup_bt.setMinimumSize(QSize(120, 60))
        self.backup_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.backup_bt)

        self.export_bt = QPushButton(Dialog)
        self.export_bt.setObjectName(u"export_bt")
        self.export_bt.setMinimumSize(QSize(120, 60))
        self.export_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.export_bt)

        self.import_bt = QPushButton(Dialog)
        self.import_bt.setObjectName(u"import_bt")
        self.import_bt.setMinimumSize(QSize(120, 60))
        self.import_bt.setMaximumSize(QSize(120, 60))
        self.horizontalLayout.addWidget(self.import_bt)
```

3e. Widen the dialog so the extra buttons fit. Change:
```python
        Dialog.resize(520, 600)
```
to:
```python
        Dialog.resize(820, 600)
```
and change:
```python
        Dialog.setMinimumSize(QSize(520, 600))
        Dialog.setMaximumSize(QSize(520, 800))
```
to:
```python
        Dialog.setMinimumSize(QSize(820, 600))
        Dialog.setMaximumSize(QSize(900, 800))
```

3f. In `setupUi`, in the `MY CODE (buttons)` block, after `self.find_llm.clicked.connect(self.find_llm_bt)` add:
```python
        self.backup_bt.clicked.connect(self.backup_bt_clicked)
        self.export_bt.clicked.connect(self.export_bt_clicked)
        self.import_bt.clicked.connect(self.import_bt_clicked)
```

3g. In `retranslateUi`, after the `self.find_llm.setText(...)` line add:
```python
        self.backup_bt.setText(QCoreApplication.translate("Dialog", u"Backup", None))
        self.export_bt.setText(QCoreApplication.translate("Dialog", u"Export", None))
        self.import_bt.setText(QCoreApplication.translate("Dialog", u"Import", None))
```

3h. Replace `_on_scan_done` with a sections-based version and add the new helpers. Replace:
```python
    def _on_scan_done(self, result):
        _report, models = result
        self._fill_models(models)
        self.info.setText(f"Found {len(models)} model(s). Tick the ones you want to use.")
```
with:
```python
    def _on_scan_done(self, sections):
        self._populate_from_sections(sections)

    def _populate_from_sections(self, sections):
        """Fill the list from a ScanSections and remember each model's tool."""
        self._tool_map = model_tool_map(sections)
        models = collect_models(sections)
        self._fill_models(models)
        self.info.setText(
            f"Found {len(models)} model(s). Tick the ones to back up, then press Backup.")
```

3i. Update `_fill_models` to tag each row with its tool id (store on the item). Replace its body with:
```python
    def _fill_models(self, names):
        """Show each model name as a checkable row, keeping prior ticks; each row
        carries its tool id (Qt.UserRole) so backup knows where it belongs."""
        checked = self._checked_names()
        self.found_list.clear()
        for name in names:
            item = QListWidgetItem(name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked if name in checked else Qt.Unchecked)
            item.setData(Qt.UserRole, self._tool_map.get(name, "local-weights"))
            self.found_list.addItem(item)
```

3j. Add the backup/export/import handlers at the end of the class:
```python
    def _checked_pairs(self):
        """(model_name, tool_id) for every ticked row."""
        pairs = []
        for row in range(self.found_list.count()):
            item = self.found_list.item(row)
            if item.checkState() == Qt.Checked:
                pairs.append((item.text(), item.data(Qt.UserRole)))
        return pairs

    def _do_backup(self, modelfile=ollama_modelfile):
        """Back up the ticked models into the AI folder. Returns the result dict."""
        pairs = self._checked_pairs()
        return backup_selected(MainBase.ai_dir(), pairs, self._catalog,
                               env=os.environ, home=os.path.expanduser("~"),
                               modelfile=modelfile)

    def backup_bt_clicked(self):
        if not self._checked_pairs():
            msg_one_button("Nothing selected",
                           "Tick at least one model first.", "info")
            return
        result = self._do_backup()
        tools = ", ".join(result["tools"])
        msg_one_button("Backup done",
                       f"Saved settings for: {tools}\ninto {MainBase.ai_dir()}", "info")

    def export_bt_clicked(self):
        out, _ = QFileDialog.getSaveFileName(
            None, "Export AI settings", "ai-settings-export.zip", "Zip (*.zip)")
        if not out:
            return
        export_ai(MainBase.ai_dir(), out)
        msg_one_button("Exported", f"AI settings exported to\n{out}", "info")

    def import_bt_clicked(self):
        path, _ = QFileDialog.getOpenFileName(
            None, "Import AI settings", "", "Zip (*.zip)")
        if not path:
            return
        import_ai(path, MainBase.ai_dir())
        msg_one_button("Imported",
                       "AI settings imported into\n"
                       f"{MainBase.ai_dir()}\n\n"
                       "Remember: secrets were not included — re-login / re-key, "
                       "and re-pull Ollama models / re-install Claude plugins.", "info")
```

Note: the `os` import is already present at the top of the file via the new imports block? It is not — add `import os` as the first line of `d__ai_settings.py`.

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python.exe test_ai_settings_dialog.py`
Expected: `RESULT: PASS`

- [ ] **Step 5: Byte-compile the touched modules**

Run: `.venv/Scripts/python.exe -m py_compile d__ai_settings.py ai_backup.py ai_catalog.py llm_scan.py main_base.py`
Expected: no output (exit 0).

- [ ] **Step 6: Commit**

```bash
git add d__ai_settings.py test_ai_settings_dialog.py
git commit -m "feat: AI Settings popup backs up, exports and imports selected models"
```

---

### Task 9: Full-catalog validation + end-to-end smoke

**Files:**
- Test: `test_ai_endtoend.py`

- [ ] **Step 1: Write the test**

Create `test_ai_endtoend.py`:
```python
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
```

- [ ] **Step 2: Run the test**

Run: `.venv/Scripts/python.exe test_ai_endtoend.py`
Expected: `RESULT: PASS` (fix any catalog gap it reports).

- [ ] **Step 3: Run the whole AI test suite**

Run each and confirm `RESULT: PASS`:
```
.venv/Scripts/python.exe test_ai_dir.py
.venv/Scripts/python.exe test_ai_catalog.py
.venv/Scripts/python.exe test_llm_tool_map.py
.venv/Scripts/python.exe test_ai_backup.py
.venv/Scripts/python.exe test_ai_backup_ollama.py
.venv/Scripts/python.exe test_ai_backup_selected.py
.venv/Scripts/python.exe test_ai_export.py
.venv/Scripts/python.exe test_ai_settings_dialog.py
.venv/Scripts/python.exe test_ai_endtoend.py
```

- [ ] **Step 4: Commit**

```bash
git add test_ai_endtoend.py
git commit -m "test: end-to-end AI backup/export/import round trip + catalog validation"
```

---

## Self-Review Notes (coverage)

- **AI folder inside settings folder** → Task 1 (`MainBase.ai_dir()`); used by the dialog in Task 8 and exercised in Tasks 8–9.
- **Group by tool (cloud = one unit, Ollama = one unit)** → `model_tool_map` (Task 3) + `backup_selected` grouping (Task 6).
- **Ollama variant A (Modelfiles + names, no weights)** → `ollama_modelfile` (Task 3) + `backup_ollama` (Task 5).
- **Exclude secrets** → catalog `exclude` rules (Task 2) enforced by `_excluded`/`backup_tool` (Task 4); asserted in Tasks 2, 4, 9.
- **Full, data-driven catalog** → `ai_catalog.json` + loader (Task 2); validated in Task 9.
- **Backup selected models** → Task 8 (`backup_bt_clicked` / `_do_backup`).
- **Export to one file / import on another machine** → `export_ai`/`import_ai` (Task 7); wired in Task 8; round-trip in Task 9.
- **Future online models (e.g. Kimi/ChatGPT)** → add to `CLOUD_CATALOG`/`_PROVIDER_CLOUD_TOOL` in `llm_scan.py` (one line) and, if a new client, one `ai_catalog.json` entry — no engine change.

**Manual QA after Task 8/9** (not automatable headless): launch EasyBack, open AI Settings, Find LLM, tick `llama3.2:3b` + a `claude-*`, press Backup, confirm `…\AI\ollama\models.txt`, `…\AI\ollama\models\llama3.2_3b.modelfile`, and `…\AI\claude-code\.claude\skills\…` exist and no `.credentials.json` is present; then Export to a zip and Import on a second machine.
