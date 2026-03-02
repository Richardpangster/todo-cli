"""Storage module for todo-cli: handles reading/writing ~/.todo.json."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import List

TODO_FILE = Path.home() / ".todo.json"


def load_todos() -> List[dict]:
    """Load todos from the JSON file.

    Returns:
        List of todo dicts, each with keys: id, content, done.
    """
    if not TODO_FILE.exists():
        return []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_todos(todos: List[dict]) -> None:
    """Save todos to the JSON file.

    Args:
        todos: List of todo dicts to persist.
    """
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def next_id(todos: List[dict]) -> int:
    """Return the next available todo ID.

    Args:
        todos: Existing todo list.

    Returns:
        Integer ID that is one greater than the current maximum.
    """
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1
