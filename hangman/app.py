import tkinter as tk
from tkinter import messagebox
from typing import List
import random

WORDS = ["python", "java", "javascript", "ruby", "data", "science", "hangman", "youtube", "zig", "computer", "typescript"]

class HangmanGame:
    def __init__(self, word_list: List[str]):
        self.word_list = word_list
        self.lives = 6
        self.chosen_word = random.choice(word_list)
        self.guessed_word = ["_"] * len(self.chosen_word)

    def guess(self, letter: str) -> bool:
        if letter in self.chosen_word:
            for i, char in enumerate(self.chosen_word):
                if char == letter:
                    self.guessed_word[i] = letter
            return True
        else:
            self.lives -= 1
            return False

    def is_game_over(self) -> bool:
        return self.lives <= 0 or "".join(self.guessed_word) == self.chosen_word

    def get_hidden_word(self) -> str:
        return " ".join(self.guessed_word)

class HangmanGUI:
    def __init__(self, game: HangmanGame):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.window.geometry("400x400")

        self.label = tk.Label(self.window, text="Guess the word: ", font=("Helvetica", 16))
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.lives_label = tk.Label(self.window, text=f"Lives: {self.game.lives}", font=("Helvetica", 16))
        self.lives_label.pack()

        self.canvas = tk.Canvas(self.window, width=200, height=200)
        self.canvas.pack()

        self.button = tk.Button(self.window, text="Check", command=self.check)
        self.button.pack()

    def draw_hangman(self):
        if self.game.lives == 5:
            self.canvas.create_line(50, 50, 150, 50)
        elif self.game.lives == 4:
            self.canvas.create_line(100, 50, 100, 100)
        elif self.game.lives == 3:
            self.canvas.create_line(90, 100, 110, 120)
        elif self.game.lives == 2:
            self.canvas.create_line(100, 120, 100, 170)
        elif self.game.lives == 1:
            self.canvas.create_line(100, 120, 130, 150)
        elif self.game.lives == 0:
            self.canvas.create_line(100, 120, 70, 150)

    def check(self):
        if self.game.is_game_over():
            self.handle_game_over()
        else:
            guess = self.entry.get().strip().lower()
            self.entry.delete(0, "end")

            if len(guess) != 1 or not guess.isalpha():
                messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            else:
                if self.game.guess(guess):
                    self.label.config(text=self.game.get_hidden_word())
                    if self.game.is_game_over():
                        self.handle_game_over()
                else:
                    self.lives_label.config(text=f"Lives remaining: {self.game.lives}")
                    self.draw_hangman()
                    if self.game.is_game_over():
                        self.handle_game_over()

    def handle_game_over(self):
        if self.game.lives <= 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {self.game.chosen_word}.")
        else:
            messagebox.showinfo("Game Over", "Congratulations! You won!")
        self.window.destroy()

    def start(self):
        self.label.config(text=self.game.get_hidden_word())
        self.window.mainloop()

def main():
    game = HangmanGame(WORDS)
    gui = HangmanGUI(game)
    gui.start()

if __name__ == "__main__":
    main()