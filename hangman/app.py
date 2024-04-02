import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["python", "java", "javascript", "ruby", "data", "science", "hangman", "youtune", "zig", "computer", "typescript"]
lives = 6

def draw_hangman(lives: int, canvas: tk.Canvas):
    if lives == 5:
        canvas.create_line(50, 50, 150, 50)
    elif lives == 4:
        canvas.create_line(100, 50, 100, 100)
    elif lives == 3:
        canvas.create_line(90, 100, 110, 120)
    elif lives == 2:
        canvas.create_line(100, 120, 100, 170)
    elif lives == 1:
        canvas.create_line(100, 120, 130, 150)
    elif lives == 0:
        canvas.create_line(100, 120, 70, 150)


def main():
    chosen_word = random.choice(WORDS)
    guessed_word = ["_"] * len(chosen_word)

    window = tk.Tk()
    window.title("Hangman")
    window.geometry("400x400")

    label = tk.Label(window, text="Guess the word: ", font=("Helvetica", 16))
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    lives_label = tk.Label(window, text=f"Lives: {lives}", font=("Helvetica", 16))
    lives_label.pack()

    canvas = tk.Canvas(window, width=200, height=200)
    canvas.pack()

    def check():
        global lives

        guess = entry.get()

        entry.delete(0, "end")

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    guessed_word[i] = guess

            label.config(text=" ".join(guessed_word))

            if "".join(guessed_word) == chosen_word:
                messagebox.showinfo("You won!", "Congratulations!")
            
        else:
            lives -= 1
            lives_label.config(text=f"Lives remaining: {lives}")
            draw_hangman(lives=lives, canvas=canvas)

            if lives == 0:
                messagebox.showinfo("You lost", f"the word was {chosen_word}")

    button = tk.Button(window, text="Check", command=lambda: check())
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()