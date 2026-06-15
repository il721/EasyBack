"""
Storage seam for named backup lists.

A "backup list" is a JSON file inside the backup_lists folder; the file name IS
the list name (no extension). Contents: {"<s_|d_>item_name": [paths, ...]}.

Pure file operations only — no Qt, no MainBase import — so this stays a leaf
module and is unit-testable in isolation.
"""
import json
import os
from pathlib import Path

# Characters Windows forbids in file names.
_INVALID_CHARS = set('\\/:*?"<>|')

# Names Windows reserves as devices; forbidden as bare file names.
_RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}


def valid_list_name(name) -> bool:
    """True if `name` is non-empty (after strip), is not a Windows reserved
    device name, and contains no reserved characters."""
    s = str(name).strip()
    if not s:
        return False
    if s.upper() in _RESERVED_NAMES:
        return False
    return not (_INVALID_CHARS & set(s))


def _path(base_dir, name) -> Path:
    return Path(base_dir) / name


def list_names(base_dir) -> list:
    """Sorted names of saved lists. Empty list if base_dir does not exist."""
    p = Path(base_dir)
    if not p.is_dir():
        return []
    return sorted(entry.name for entry in p.iterdir() if entry.is_file())


def list_exists(base_dir, name) -> bool:
    return _path(base_dir, name).is_file()


def save_list(base_dir, name, items: dict) -> None:
    """Write `items` as JSON (UTF-8) to base_dir/name, creating base_dir if needed."""
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    with open(_path(base_dir, name), "w", encoding="utf-8") as f:
        json.dump(items, f)


def load_list(base_dir, name) -> dict:
    """Read base_dir/name as JSON (UTF-8). Propagates FileNotFoundError/JSONDecodeError."""
    with open(_path(base_dir, name), "r", encoding="utf-8") as f:
        return json.load(f)


def rename_list(base_dir, old, new) -> None:
    """Rename base_dir/old to base_dir/new (overwrites new if it exists)."""
    os.replace(_path(base_dir, old), _path(base_dir, new))


def delete_list(base_dir, name) -> None:
    """Delete base_dir/name."""
    os.remove(_path(base_dir, name))
