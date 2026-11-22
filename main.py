from manager import TaskManager
from storage import Storage

MENU = """
=== TaskFlow ===
1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Quit
"""


def ask_id() -> int | None:
    try:
        return int(input("Task id: "))
    except ValueError:
        print("Please enter a number.")
        return None


def main() -> None:
    storage = Storage()
    manager = TaskManager(storage.load())

    while True:
        print(MENU)
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                task = manager.add(input("Title: "))
                print(f"Added: {task}")
            except ValueError as e:
                print(e)
        elif choice == "2":
            tasks = manager.list()
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                print(task)
        elif choice in ("3", "4"):
            task_id = ask_id()
            if task_id is None:
                continue
            try:
                if choice == "3":
                    print(f"Completed: {manager.complete(task_id)}")
                else:
                    print(f"Deleted: {manager.delete(task_id)}")
            except KeyError as e:
                print(e.args[0])
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")
            continue

        storage.save(manager.list())


if __name__ == "__main__":
    main()
