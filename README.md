# ado-ai

A lightweight demo repository containing a Python CLI to-do list skeleton.

## Project Overview

This project includes:
- An `argparse`-based command-line app with `add` and `list` commands.
- JSON-backed task storage for simple local persistence.
- A starter layout for extending into a fuller application.

## Structure

- `src/todo.py`: CLI entry point and command handlers.
- `data/tasks.json`: Local JSON file used to store tasks.
- `requirements.txt`: Dependency placeholder file.

## Usage

Run from the repository root:

```bash
python3 src/todo.py add "Buy milk"
python3 src/todo.py list
```
