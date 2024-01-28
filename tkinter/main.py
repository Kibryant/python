import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.label = ttk.Label(self.main_frame, text="Hello World!")
        self.label.pack(padx=20, pady=20)
        self.button = ttk.Button(self.main_frame, text="Click Me!", command=self.click)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def click(self):
        self.label.config(text="Button clicked!")


if __name__ == "__main__":
    App()
