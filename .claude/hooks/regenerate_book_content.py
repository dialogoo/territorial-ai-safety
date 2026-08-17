"""PostToolUse hook: keep src/generated/ in step with the pipeline.

Reads the hook payload on stdin. If the edited file was the indicator registry or
anything in analysis/pipeline/, rerun analysis/pipeline/render_book.py so the
book's computed tables can never go stale — the staleness check CI enforces.

Silent on a no-match; prints a systemMessage when it regenerates or fails.
"""

import json
import os
import subprocess
import sys
from pathlib import Path


def project_dir() -> Path:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[2]


def interpreter(root: Path) -> str:
    """Prefer the project venv — the system interpreter may lack pandas."""
    for candidate in (root / ".venv" / "Scripts" / "python.exe", root / ".venv" / "bin" / "python"):
        if candidate.exists():
            return str(candidate)
    return sys.executable


def touched(payload: dict) -> str:
    tool_input = payload.get("tool_input") or {}
    tool_response = payload.get("tool_response") or {}
    path = tool_input.get("file_path") or tool_response.get("filePath") or ""
    return path.replace("\\", "/")


def is_pipeline_file(path: str) -> bool:
    if path.endswith("analysis/registry/indicators.yml"):
        return True
    return "analysis/pipeline/" in path and path.endswith(".py")


def say(message: str) -> None:
    print(json.dumps({"systemMessage": message}))


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return

    path = touched(payload)
    if not is_pipeline_file(path):
        return

    root = project_dir()
    result = subprocess.run(
        [interpreter(root), str(root / "analysis" / "pipeline" / "render_book.py")],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        say("Regenerated src/generated/ — commit it with this change.")
    else:
        tail = (result.stderr or result.stdout).strip().splitlines()
        say("render_book.py failed: " + (tail[-1] if tail else "unknown error"))


if __name__ == "__main__":
    main()
