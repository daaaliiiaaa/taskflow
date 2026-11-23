# TaskFlow

A simple command line to-do app written in Python, refactored from functions into classes.

## Features
- Add, list, complete and delete tasks
- Tasks are saved to `tasks.json`, so they stay after you close the app

## Project structure
| File | What it does |
|------|--------------|
| `task.py` | `Task` dataclass: id, title, done, `mark_done()` |
| `manager.py` | `TaskManager`: add, complete, delete, list, find (never prints) |
| `storage.py` | `Storage`: `load()` and `save()` using JSON |
| `main.py` | The menu the user interacts with |

## How to run
Requires Python 3.10 or newer.

```bash
git clone https://github.com/<your-username>/taskflow.git
cd taskflow
python main.py
```

## Team
- Dalia Obeidat
- Member 2
