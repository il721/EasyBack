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
