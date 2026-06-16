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
    # Match each exclude glob against the full path. The second form ("*/" +
    # stripped pattern) lets a leading-anchored pattern such as "models/**" also
    # match deeper in the tree; the catalog's "**/..." patterns already match via
    # the direct form (fnmatch's * crosses "/"), so this is a belt-and-braces
    # fallback for bare patterns a future catalog entry might use.
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
