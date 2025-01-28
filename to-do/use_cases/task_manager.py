from entities.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()

    def get_all_tasks(self):
        return self.tasks
