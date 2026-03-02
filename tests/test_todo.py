"""Tests for todo-cli core functionality."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

# We patch TODO_FILE so tests don't touch ~/.todo.json
import src.storage as storage_module
from src.todo import add_todo, delete_todo, list_todos, mark_done


@pytest.fixture(autouse=True)
def tmp_todo_file(tmp_path: Path):
    """Redirect TODO_FILE to a temp path for each test."""
    tmp_file = tmp_path / ".todo.json"
    with patch.object(storage_module, "TODO_FILE", tmp_file):
        yield tmp_file


class TestAddTodo:
    def test_add_single_todo(self):
        item = add_todo("Buy milk")
        assert item["id"] == 1
        assert item["content"] == "Buy milk"
        assert item["done"] is False

    def test_add_multiple_todos_increments_id(self):
        first = add_todo("Task A")
        second = add_todo("Task B")
        assert first["id"] == 1
        assert second["id"] == 2

    def test_add_persists_to_file(self, tmp_todo_file: Path):
        add_todo("Persist me")
        data = json.loads(tmp_todo_file.read_text())
        assert len(data) == 1
        assert data[0]["content"] == "Persist me"


class TestListTodos:
    def test_list_empty(self):
        todos = list_todos()
        assert todos == []

    def test_list_returns_all(self):
        add_todo("Alpha")
        add_todo("Beta")
        todos = list_todos()
        assert len(todos) == 2
        assert todos[0]["content"] == "Alpha"
        assert todos[1]["content"] == "Beta"


class TestMarkDone:
    def test_mark_existing_todo_done(self):
        add_todo("Finish report")
        result = mark_done(1)
        assert result is not None
        assert result["done"] is True

    def test_mark_nonexistent_todo_returns_none(self):
        result = mark_done(999)
        assert result is None

    def test_done_status_persisted(self, tmp_todo_file: Path):
        add_todo("Check email")
        mark_done(1)
        data = json.loads(tmp_todo_file.read_text())
        assert data[0]["done"] is True


class TestDeleteTodo:
    def test_delete_existing_todo(self):
        add_todo("Remove me")
        result = delete_todo(1)
        assert result is not None
        assert result["content"] == "Remove me"
        assert list_todos() == []

    def test_delete_nonexistent_todo_returns_none(self):
        result = delete_todo(42)
        assert result is None

    def test_delete_only_removes_target(self):
        add_todo("Keep me")
        add_todo("Delete me")
        delete_todo(2)
        remaining = list_todos()
        assert len(remaining) == 1
        assert remaining[0]["content"] == "Keep me"
