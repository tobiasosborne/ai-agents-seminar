"""
Two tools for the primitive agent: read_file and write_file.

Both are restricted to paths within the workspace/ directory.
"""

import os

WORKSPACE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspace")


def _safe_path(path):
    """Resolve path and ensure it stays within WORKSPACE."""
    resolved = os.path.realpath(os.path.join(WORKSPACE, path))
    if not resolved.startswith(os.path.realpath(WORKSPACE)):
        raise ValueError(f"Path escapes workspace: {path}")
    return resolved


def read_file(path):
    """Read and return file contents, or an error string."""
    try:
        full = _safe_path(path)
        with open(full) as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: file not found: {path}"
    except ValueError as e:
        return f"Error: {e}"


def write_file(path, content):
    """Write content to path (creating directories if needed). Returns 'ok' or error."""
    try:
        full = _safe_path(path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w") as f:
            f.write(content)
        return "ok"
    except ValueError as e:
        return f"Error: {e}"
