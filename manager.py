from task import Task


class TaskManager:
    """Holds the tasks and the rules for changing them. It never prints."""

    def __init__(self, tasks: list[Task] | None = None):
        self.tasks: list[Task] = tasks or []

    def _next_id(self) -> int:
        return max((t.id for t in self.tasks), default=0) + 1

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty")
        task = Task(self._next_id(), title)
        self.tasks.append(task)
        return task

    def find(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete(self, task_id: int) -> Task:
        task = self.find(task_id)
        if task is None:
            raise KeyError(f"No task with id {task_id}")
        task.mark_done()
        return task

    def delete(self, task_id: int) -> Task:
        task = self.find(task_id)
        if task is None:
            raise KeyError(f"No task with id {task_id}")
        self.tasks.remove(task)
        return task

    def list(self) -> list[Task]:
        return list(self.tasks)
