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
