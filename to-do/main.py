import tkinter as tk
from tkinter import messagebox
from use_cases.task_manager import TaskManager
from interface.task_repository import TaskRepository


class ToDoApp:
    def __init__(self, root):
        """Initializes the To-Do List application."""
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")

        self.task_manager = TaskManager()
        self.task_repository = TaskRepository()
        self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the To-Do List application."""
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(
            self.root, text="Adicionar Tarefa", command=self.add_task
        )
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(
            self.root, text="Remover Tarefa", command=self.remove_task
        )
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(
            self.root, text="Marcar como Concluída", command=self.mark_task_as_completed
        )
        self.complete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.update_task_listbox()

        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def add_task(self):
        """Adds a task to the listbox."""
        description = self.task_entry.get()
        if description:
            self.task_manager.add_task(description)
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

    def remove_task(self):
        """Removes a task from the listbox."""
        try:
            index = self.task_listbox.curselection()[0]
            self.task_manager.remove_task(index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione uma tarefa para remover."
            )

    def mark_task_as_completed(self):
        """Marks a task as completed in the listbox."""
        try:
            index = self.task_listbox.curselection()[0]
            self.task_manager.mark_task_as_completed(index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione uma tarefa para marcar como concluída."
            )

    def update_task_listbox(self):
        """Updates the listbox with the tasks."""
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_all_tasks():
            self.task_listbox.insert(tk.END, str(task))

    def load_tasks(self):
        """Loads tasks from the file."""
        tasks = self.task_repository.load_tasks()
        for task in tasks:
            self.task_manager.add_task(task.description)
            if task.completed:
                self.task_manager.mark_task_as_completed(
                    len(self.task_manager.get_all_tasks()) - 1
                )

    def save_and_exit(self):
        """Saves the tasks to the file and exits the application."""
        self.task_repository.save_tasks(self.task_manager.get_all_tasks())
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
