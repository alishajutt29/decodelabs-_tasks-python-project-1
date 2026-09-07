# 📝 To-Do List — Python Programming (Project 1)

A command-line To-Do List manager built as **Project 1** of the DecodeLabs
Python Programming Industrial Training (Batch 2026).

This project focuses on **data management fundamentals** — storing multiple
items in a single variable using Python **lists**, before moving on to
databases later in the track.

## ✨ Features

- ➕ Add tasks
- 📋 View all tasks (with status: Pending / Done)
- ☑️ Mark a task as done
- 🗑️ Delete a task
- 💾 Persistent storage — tasks are saved to `tasks.json` so they survive
  program restarts (solves the "volatile memory" problem: RAM is wiped when
  a program closes, so data is written to disk).

## 🧠 Concepts Used

| Concept              | Where it's used                                   |
|----------------------|----------------------------------------------------|
| Lists                | Storing all tasks (`tasks = []`)                    |
| Dictionaries         | Each task is `{"id": .., "task": .., "done": ..}`   |
| `enumerate()`        | Numbering tasks when displaying them                |
| Functions            | `add_task()`, `view_tasks()`, `delete_task()`, etc. |
| File I/O + JSON      | `load_tasks()` / `save_tasks()` for persistence     |
| `if __name__ == "__main__":` | Entry point guard                          |

## 🚀 How to Run

```bash
python3 todo_list.py
```

You'll see a menu:

```
==============================
   📝 TO-DO LIST MANAGER
==============================
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
```

Just enter the number of the option you want.

## 📂 Project Structure

```
todo-list-python/
├── todo_list.py     # Main program
├── tasks.json        # Auto-generated on first run (ignored by git)
├── README.md
└── .gitignore
```

## 🏢 About

Built as part of the **DecodeLabs Industrial Training Kit — Python
Programming, Batch 2026**.

🌐 www.decodelabs.tech
