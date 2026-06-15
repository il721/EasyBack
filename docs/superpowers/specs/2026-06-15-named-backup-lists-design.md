# Named Backup Lists — Design

**Date:** 2026-06-15
**Status:** Approved (pending written-spec review)

## Overview

Today EasyBack saves every backup item into a single hardcoded file named `all`
inside `{path_settings_folder}\backup_lists`. The user wants **multiple, named
backup lists**:

1. In **Add Item**, build up some items, press **Save List**, and the program
   asks for a *name* and saves the current working set under that name.
2. **Edit Backup List** shows *all* saved lists and supports **full management**:
   edit the items inside a list, rename a whole list, and delete a whole list.
3. **Back up all** copies the items from *every* saved list.

The filename hardcoded to `all` currently appears in four files
(`MainWindow.py`, `main_base.py`, `d__01_add_item.py`, `d__02_edit_list_main.py`).
This design replaces that scattered convention with a single, testable storage
seam (Approach B).

The original author already scaffolded part of this: `D012SelFileNameDialog`
(`d__01_2__sel_buckup_file_name.py`) is a styled "enter list name" dialog whose
call is commented out in `save_backup_list_bt`. We complete and wire it up.

## Decisions (from brainstorming)

- **Edit scope:** Full management — add/remove items within a list, rename a
  list, delete a list.
- **Working-set model:** The in-memory working set (`base.all_items` on the
  module-level `MainBase` singleton in `d__01_add_item.py`) **persists** across
  opening/closing the Add Item dialog and across saves, for the duration of the
  app run. It is *not* auto-cleared on save.
- **Starting a fresh list:** The existing **Clear All** button resets the
  working set. It must be fixed to clear the underlying data
  (`base.all_items`, `self.list_of_file`), not only the visible widget.
- **Back up all:** Aggregates the items from *all* saved lists and copies them
  using the existing copy logic.
- **Architecture:** Approach B — a small, stdlib-only storage seam
  (`backup_lists.py`) holds all list CRUD; the Qt dialogs stay thin and call
  into it. This keeps the risky file operations (overwrite, rename, delete)
  unit-testable headlessly.

## Storage layout

- Each backup list is a JSON file: `{path_settings_folder}\backup_lists\<list_name>`.
- **Filename == list name**, no extension. This matches today's `all`
  convention and means the name the user types is exactly what appears in the
  Edit dialog (which lists raw filenames). Consequence: list names must be valid
  Windows filenames — see Validation.
- File contents (unchanged): a dict mapping `"<suffix>item_name"` to a list of
  paths, where the suffix is `s_` (settings) or `d_` (data). Example:
  `{"s_VSCode": ["C:/.../settings.json"], "d_Photos": ["D:/Photos"]}`.

## Component: `backup_lists.py` (new, leaf module)

Stdlib only (`json`, `os`, `pathlib`). Does **not** import `MainBase` or any Qt
module, so there is no import cycle and it is testable in isolation. All
functions take an explicit `base_dir` (the `backup_lists` folder path) so they
hold no global state.

```python
def list_names(base_dir) -> list[str]:
    """Sorted list of saved list names. Returns [] if base_dir is missing."""

def list_exists(base_dir, name) -> bool: ...

def save_list(base_dir, name, items: dict) -> None:
    """Create base_dir if needed, then json.dump items to base_dir/name."""

def load_list(base_dir, name) -> dict:
    """json.load base_dir/name. Raises FileNotFoundError / JSONDecodeError to caller."""

def rename_list(base_dir, old, new) -> None:
    """os.replace base_dir/old -> base_dir/new."""

def delete_list(base_dir, name) -> None:
    """os.remove base_dir/name."""

def valid_list_name(name) -> bool:
    """False for empty/whitespace names or names containing \\ / : * ? " < > |."""
```

`MainBase` gains one helper so callers don't rebuild the path string:

```python
@classmethod
def backup_lists_dir(cls) -> str:
    return f"{cls.path_settings_folder}\\backup_lists"
```

The hardcoded-`all` save logic in `MainBase.save_base_to_disk` is removed; all
saving is centralized in `backup_lists.save_list`. (If any caller still needs a
`MainBase` entry point, it becomes a one-line delegate to `save_list`.)

## Save flow (naming a list)

1. **`d__01_add_item.py: save_backup_list_bt`** — if the working set is empty,
   show an info message ("nothing to save") and return; otherwise open
   `D012SelFileNameDialog`.
2. **`d__01_2__sel_buckup_file_name.py: D012SelFileNameDialog.save_list_bt`**:
   - Read `input_file_name`.
   - `valid_list_name(name)` is False → warn, return.
   - `list_exists(base_dir, name)` → `msg_two_button` confirm overwrite;
     "no" → return.
   - `save_list(base_dir, name, b.base.all_items)`.
   - Success message; close the dialog.
3. The dialog's separate **`owerwrite_exist` button is out of scope** and will be
   hidden — name collisions are handled by the confirm prompt above. (Flagged
   for review; building an existing-name picker was not requested.)
4. **`clear_all_bt`** now clears `base.all_items` and `self.list_of_file` in
   addition to the list widget, guarded by a `msg_two_button` confirm
   (it is now destructive of the working set).
5. Remove the stale **preload-from-`all`** block in `add_item_01_bt`
   (currently `d__01_add_item.py:309-312`): there is no global `all` file
   anymore, and the working set is the in-memory singleton. The duplicate-name
   check (`base.check_name`) continues to work against the in-memory working set.

## Edit flow (full management)

### `d__02_edit_list_main.py: EditListMain`

- Populate the list widget from `backup_lists.list_names(base_dir)` (instead of
  raw `os.listdir`).
- Add **Rename** and **Delete** buttons operating on the selected list:
  - **Delete** → `msg_two_button` confirm → `delete_list` → refresh widget.
  - **Rename** → a small name-input prompt that returns a string (a lightweight
    reuse of the styled `QLineEdit`, **not** `D012SelFileNameDialog`'s
    save-wired flow) → `valid_list_name` + collision check → `rename_list` →
    refresh widget.
- Clicking a list opens the per-list item editor (`ListBackupItemEdit`),
  passing the **list name** (so it can save back) in addition to the items dict.

### `d__02_1_edit_item.py: ListBackupItemEdit`

Becomes the per-list item editor (today: view-only, `item_bt` is a `print`
stub). It works on a loaded copy of the list:

- Show the list's item keys.
- Click an item → **delete** it (confirm) from the working copy.
- **Add item** button → open `AddItemDial01` targeting *this list's* working
  copy. `AddItemDial01` gains an **optional target-dict parameter** that
  defaults to the global working set (`base.all_items`); the editor passes its
  own copy. This avoids editing the global singleton by side effect.
- **Save** button → `backup_lists.save_list(base_dir, name, working_copy)`.

## Back up all

**`MainWindow.py: backup_all_bt`**:

1. `names = backup_lists.list_names(base_dir)`.
2. If empty → existing "No backup lists yet" message (from the earlier bugfix);
   return.
3. `merged = {}`; for each name: `merged.update(backup_lists.load_list(base_dir, name))`.
   Duplicate item keys across lists → last list wins (documented behavior).
4. Run the **existing** copy logic over `merged` (unchanged semantics — only the
   *source* changed from one `all` file to all lists).

Out of scope (pre-existing behavior, untouched): the current copy loop only
copies `s_` (settings) items and computes but does not copy `d_` (data) items;
and it copies into `{path_settings_folder}\<item_name>`. Redesigning copy
semantics is not part of this request.

## Error handling & validation

| Situation | Handling |
|---|---|
| Empty/whitespace list name | `valid_list_name` False → warn, no save |
| Reserved filename chars (`\ / : * ? " < > \|`) | `valid_list_name` False → warn |
| Save name already exists | `msg_two_button` confirm overwrite |
| Rename into an existing name | collision check → warn, no rename |
| Empty/corrupt list file | existing `JSONDecodeError` warn kept |
| `backup_lists` folder missing | `list_names` returns `[]`; call-site guard shows "No backup lists yet" |
| Rename/delete of a vanished file | guarded (check exists first) |

## Testing

Extends the headless pattern established in `test_missing_backup_lists.py`
(offscreen Qt, stubbed `msg_*`, patched `QDialog.exec`), run with
`.venv/Scripts/python.exe`.

- **`backup_lists.py` unit tests** (pure, temp dir, no Qt):
  save/load round-trip; `list_names` (incl. missing folder → `[]`);
  `list_exists`; `rename_list`; `delete_list`; overwrite; `valid_list_name`
  accepts good names and rejects empty / reserved-char names.
- **GUI handler tests** (headless):
  - `save_backup_list_bt` + `D012SelFileNameDialog`: save under a name; existing
    name → overwrite confirmed; invalid name → warned, not saved.
  - `backup_all_bt`: two saved lists aggregate into the copy step; empty → "no
    lists" message.
  - `EditListMain`: delete refreshes the widget; rename refreshes the widget.

## Files touched

- **New:** `backup_lists.py`
- **New:** tests (e.g. `test_backup_lists.py`, extend existing test file)
- **Modified:** `main_base.py` (`backup_lists_dir` helper; generalize
  `save_base_to_disk`), `d__01_add_item.py`, `d__01_2__sel_buckup_file_name.py`,
  `d__02_edit_list_main.py`, `d__02_1_edit_item.py`, `MainWindow.py`

## Out of scope

- Redesigning the "Back up all" file-copy semantics (data-item copying, copy
  destination) — preserved as-is.
- An existing-name picker for the save dialog (`owerwrite_exist` button) — hidden.
- Disk persistence of the in-memory working set across full app restarts (it
  persists only within a run, by the singleton).
- Migration of any existing single `all` file (none exists on the target setup).
