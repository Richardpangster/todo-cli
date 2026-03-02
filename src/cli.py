"""CLI entry point for todo-cli using argparse."""

from __future__ import annotations

import argparse
import sys

from .todo import add_todo, delete_todo, list_todos, mark_done


def cmd_add(args: argparse.Namespace) -> None:
    """Handle `todo add` command."""
    item = add_todo(args.content)
    print(f"✅ Added [{item['id']}]: {item['content']}")


def cmd_list(_args: argparse.Namespace) -> None:
    """Handle `todo list` command."""
    todos = list_todos()
    if not todos:
        print("📭 No todos yet. Add one with: todo add \"task content\"")
        return
    print(f"{'ID':<5} {'Status':<10} Task")
    print("-" * 50)
    for item in todos:
        status = "✔ done" if item["done"] else "○ todo"
        print(f"{item['id']:<5} {status:<10} {item['content']}")


def cmd_done(args: argparse.Namespace) -> None:
    """Handle `todo done` command."""
    item = mark_done(args.id)
    if item:
        print(f"🎉 Marked done [{item['id']}]: {item['content']}")
    else:
        print(f"❌ Todo with ID {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args: argparse.Namespace) -> None:
    """Handle `todo delete` command."""
    item = delete_todo(args.id)
    if item:
        print(f"🗑️  Deleted [{item['id']}]: {item['content']}")
    else:
        print(f"❌ Todo with ID {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command-line todo manager",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True

    # add
    add_parser = subparsers.add_parser("add", help="Add a new todo item")
    add_parser.add_argument("content", help="Task description")
    add_parser.set_defaults(func=cmd_add)

    # list
    list_parser = subparsers.add_parser("list", help="List all todos")
    list_parser.set_defaults(func=cmd_list)

    # done
    done_parser = subparsers.add_parser("done", help="Mark a todo as done")
    done_parser.add_argument("id", type=int, help="Todo ID")
    done_parser.set_defaults(func=cmd_done)

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete a todo item")
    delete_parser.add_argument("id", type=int, help="Todo ID")
    delete_parser.set_defaults(func=cmd_delete)

    return parser


def main() -> None:
    """Main CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
