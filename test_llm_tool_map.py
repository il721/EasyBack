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
