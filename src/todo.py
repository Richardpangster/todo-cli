"""Core todo operations for todo-cli."""

from __future__ import annotations

from typing import List, Optional

from .storage import load_todos, next_id, save_todos


def add_todo(content: str) -> dict:
    """Add a new todo item.

    Args:
        content: The task description.

    Returns:
        The newly created todo dict.
    """
    todos = load_todos()
    item: dict = {
        "id": next_id(todos),
        "content": content,
        "done": False,
    }
    todos.append(item)
    save_todos(todos)
    return item


def list_todos() -> List[dict]:
    """Return all todos.

    Returns:
        List of all todo dicts.
    """
    return load_todos()


def mark_done(todo_id: int) -> Optional[dict]:
    """Mark a todo item as done.

    Args:
        todo_id: The ID of the todo to mark complete.

    Returns:
        The updated todo dict, or None if not found.
    """
    todos = load_todos()
    for item in todos:
        if item["id"] == todo_id:
            item["done"] = True
            save_todos(todos)
            return item
    return None


def delete_todo(todo_id: int) -> Optional[dict]:
    """Delete a todo item.

    Args:
        todo_id: The ID of the todo to delete.

    Returns:
        The deleted todo dict, or None if not found.
    """
    todos = load_todos()
    for i, item in enumerate(todos):
        if item["id"] == todo_id:
            removed = todos.pop(i)
            save_todos(todos)
            return removed
    return None
