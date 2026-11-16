"""Load and save tasks using a local JSON file."""

import json
import os

DATA_FILE = "tasks.json"

def load_tasks(manager):
    # Starting with an empty list is safe when the file does not exist yet.
    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        manager.tasks = data
        # Continue IDs from the largest existing ID.
        manager.next_id = max((task["id"] for task in data), default=0) + 1
    except (json.JSONDecodeError, OSError, KeyError, TypeError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")

def save_tasks(manager):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(manager.get_tasks(), file, indent=4)
