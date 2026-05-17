"""Simple to-do CLI skeleton using argparse and JSON storage."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"


def ensure_data_file(path: Path) -> None:
    """Create the data file with an empty task list if it does not exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("[]\n", encoding="utf-8")


def load_tasks(path: Path) -> list[dict[str, Any]]:
    """Load tasks from JSON storage."""
    ensure_data_file(path)
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def save_tasks(path: Path, tasks: list[dict[str, Any]]) -> None:
    """Persist tasks to JSON storage."""
    path.write_text(json.dumps(tasks, indent=2) + "\n", encoding="utf-8")


def add_task(path: Path, text: str) -> None:
    """Add a new task entry."""
    tasks = load_tasks(path)
    tasks.append({"id": len(tasks) + 1, "task": text, "done": False})
    save_tasks(path, tasks)
    print(f"Added task #{len(tasks)}: {text}")


def list_tasks(path: Path) -> None:
    """Print all tasks."""
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        status = "x" if task.get("done") else " "
        print(f"[{status}] {task.get('id')}: {task.get('task')}")


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser and subcommands."""
    parser = argparse.ArgumentParser(description="To-do list CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new to-do task")
    add_parser.add_argument("task", help="Task description")

    subparsers.add_parser("list", help="List all to-do tasks")

    return parser


def main() -> None:
    """Entry point for the CLI app."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(DATA_FILE, args.task)
    elif args.command == "list":
        list_tasks(DATA_FILE)


if __name__ == "__main__":
    main()
