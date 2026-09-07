"""
DecodeLabs - Python Programming Internship
Project 1: The To-Do List
--------------------------------------------------
Goal   : Build a program where users can add tasks to a list and view them.
Skill  : Lists (append & loops), enumerate(), functions, JSON persistence.
Author : Junior Python Developer Track
"""

import json
import os

DATA_FILE = "tasks.json"


# ------------------------------------------------------------------
# STORAGE LAYER (Persistence: RAM -> Disk, so data isn't lost on exit)
# ------------------------------------------------------------------
def load_tasks():
    """Load tasks from disk into memory. Returns a list of dicts."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Persist the in-memory list to disk as JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# ------------------------------------------------------------------
# CORE LOGIC LAYER (Model)
# ------------------------------------------------------------------
def add_task(tasks, task_name):
    """Append a new task dict to the list. Each task = {id, task, done}."""
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": new_id, "task": task_name, "done": False})
    print(f'✅ Task added: "{task_name}"')


def view_tasks(tasks):
    """Print all tasks using enumerate() for clean numbering."""
    if not tasks:
        print("📭 No tasks yet. Add one first!")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "❌ Pending"
        print(f'{index}. {task["task"]}  [{status}]')
    print("------------------------\n")


def mark_done(tasks, position):
    """Mark a task as done using its displayed position (1-based)."""
    if 1 <= position <= len(tasks):
        tasks[position - 1]["done"] = True
        print(f'☑️  Marked "{tasks[position - 1]["task"]}" as done.')
    else:
        print("⚠️  Invalid task number.")


def delete_task(tasks, position):
    """Remove a task using its displayed position (1-based)."""
    if 1 <= position <= len(tasks):
        removed = tasks.pop(position - 1)
        print(f'🗑️  Removed: "{removed["task"]}"')
    else:
        print("⚠️  Invalid task number.")


# ------------------------------------------------------------------
# VIEW LAYER (User Interface / Menu)
# ------------------------------------------------------------------
def show_menu():
    print("=" * 30)
    print("   📝 TO-DO LIST MANAGER")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def get_int_input(prompt):
    """Safely get an integer from the user."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("⚠️  Please enter a valid number.")


# ------------------------------------------------------------------
# MAIN PROGRAM LOOP (Controller)
# ------------------------------------------------------------------
def main():
    tasks = load_tasks()  # load previous session's tasks (persistence)

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task_name = input("Enter the task: ").strip()
            if task_name:
                add_task(tasks, task_name)
                save_tasks(tasks)
            else:
                print("⚠️  Task cannot be empty.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                pos = get_int_input("Enter task number to mark done: ")
                mark_done(tasks, pos)
                save_tasks(tasks)

        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                pos = get_int_input("Enter task number to delete: ")
                delete_task(tasks, pos)
                save_tasks(tasks)

        elif choice == "5":
            print("👋 Goodbye! Your tasks are saved.")
            break

        else:
            print("⚠️  Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
