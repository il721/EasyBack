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
