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
import zipfile
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
    (root / "models.txt").write_text(
        "\n".join(model_names) + ("\n" if model_names else ""), encoding="utf-8")
    return written


def backup_local_weights(ai_dir, paths) -> None:
    """Record loose weight-file paths only (variant A — files are not copied)."""
    root = Path(ai_dir) / "local-weights"
    root.mkdir(parents=True, exist_ok=True)
    (root / "weights_paths.txt").write_text(
        "\n".join(paths) + ("\n" if paths else ""), encoding="utf-8")


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
    ai_dir_resolved = ai_dir.resolve()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    backup_root = ai_dir / f"import-backup-{stamp}"
    names = []
    with zipfile.ZipFile(in_file, "r") as z:
        for member in z.namelist():
            if member.endswith("/"):
                continue
            target = ai_dir / member
            # Guard against zip-slip: skip any member that resolves outside
            # ai_dir (e.g. "../evil" or an absolute path).
            try:
                target.resolve().relative_to(ai_dir_resolved)
            except ValueError:
                continue
            if backup_existing and target.is_file():
                bk = backup_root / member
                bk.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(target, bk)
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(member) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            names.append(member)
    return names
