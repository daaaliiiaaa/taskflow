from dataclasses import dataclass


@dataclass
class Task:
    """One task in the list."""

    id: int
    title: str
    done: bool = False

    def mark_done(self) -> None:
        self.done = True

    def __str__(self) -> str:
        mark = "✓" if self.done else " "
        return f"[{mark}] {self.id}. {self.title}"
