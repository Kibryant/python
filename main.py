import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.main_frame = ttk.Frame(self.root)

        self.root.mainloop()

    def click(self):
        self.label.config(text="Button clicked!")

if __name__ == "__main__":
    App()