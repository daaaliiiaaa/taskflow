import json
from dataclasses import asdict
from pathlib import Path

from task import Task


class Storage:
    """Saves and loads tasks as JSON."""

    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        return [Task(**item) for item in data]

    def save(self, tasks: list[Task]) -> None:
        data = [asdict(t) for t in tasks]
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")