# todo-cli

A simple, lightweight command-line todo manager written in Python.  
Todos are stored in `~/.todo.json` — no database, no cloud, just a plain JSON file.

## Features

- ➕ Add todos
- 📋 List all todos with status
- ✅ Mark todos as done
- 🗑️ Delete todos
- 💾 Persistent JSON storage (`~/.todo.json`)

## Requirements

- Python 3.8+

## Installation

```bash
git clone https://github.com/Richardpangster/todo-cli.git
cd todo-cli
pip install -e .
```

## Usage

```bash
# Add a new todo
todo add "Buy groceries"
todo add "Write unit tests"

# List all todos
todo list
# ID    Status     Task
# --------------------------------------------------
# 1     ○ todo     Buy groceries
# 2     ○ todo     Write unit tests

# Mark a todo as done
todo done 1
# 🎉 Marked done [1]: Buy groceries

# Delete a todo
todo delete 2
# 🗑️  Deleted [2]: Write unit tests
```

## Project Structure

```
todo-cli/
├── src/
│   ├── __init__.py
│   ├── cli.py        # argparse CLI entry point
│   ├── todo.py       # core CRUD operations
│   ├── storage.py    # JSON persistence layer
│   └── main.py       # module runner shim
├── tests/
│   ├── __init__.py
│   └── test_todo.py  # pytest test suite
├── setup.py
├── requirements.txt
└── README.md
```

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Data Format

Todos are stored in `~/.todo.json` as a JSON array:

```json
[
  { "id": 1, "content": "Buy groceries", "done": true },
  { "id": 2, "content": "Write unit tests", "done": false }
]
```

## License

MIT
