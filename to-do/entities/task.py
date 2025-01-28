class Task:
    def __init__(self, description, completed=False):
        """Initializes a new task."""
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else " "
        return f"{status} {self.description}"
