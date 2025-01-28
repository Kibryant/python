from entities.task import Task


class TaskRepository:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path

    def save_tasks(self, tasks):
        """Saves the tasks to the file."""
        with open(self.file_path, "w") as file:
            for task in tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_tasks(self):
        """Loads tasks from the file."""
        tasks = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    description, completed = line.strip().split(",")
                    task = Task(description, completed == "True")
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks
