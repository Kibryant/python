import tkinter as tk
from tkinter import messagebox
from typing import List, Optional


class TicTacToe:
    root: tk.Tk
    current_player: str
    user_choice: str
    buttons: List[List[Optional[tk.Button]]]
    x_wins: int
    o_wins: int

    def __init__(self, root: tk.Tk):
        self.root: tk.Tk = root
        self.root.title("Tic Tac Toe")
        self.current_player: str = "X"
        self.user_choice: str = "X"
        self.x_wins: int = 0
        self.o_wins: int = 0

        self.buttons: List[List[Optional[tk.Button]]] = [
            [None for _ in range(3)] for _ in range(3)
        ]

        self.create_player_choice()

    def create_player_choice(self) -> None:
        """Creates a dialog for players to choose X or O."""
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(
            self.choice_frame, text="Choose your symbol:", font=("Helvetica", 14)
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            self.choice_frame,
            text="X",
            font=("Helvetica", 14),
            command=lambda: self.set_player_choice("X"),
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            self.choice_frame,
            text="O",
            font=("Helvetica", 14),
            command=lambda: self.set_player_choice("O"),
        ).grid(row=0, column=2, padx=5)

    def set_player_choice(self, choice: str) -> None:
        """Sets the player's choice and initializes the board."""
        self.user_choice = choice
        self.current_player = choice
        messagebox.showinfo("Selection Complete", f"You chose {choice}. Let's start!")

        self.choice_frame.destroy()
        self.create_board()

    def create_board(self) -> None:
        """Creates the 3x3 board with buttons."""
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("Helvetica", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c),
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Helvetica", 14),
            bg="red",
            fg="white",
            command=self.reset_game,
        )

        reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def on_click(self, row: int, col: int) -> None:
        """Handles button click events."""
        button = self.buttons[row][col]

        if button and button["text"] == " ":
            button["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")

                if self.current_player == "X":
                    self.x_wins += 1
                else:
                    self.o_wins += 1

                messagebox.showinfo("Score", f"X: {self.x_wins} | O: {self.o_wins}")

                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken!")

    def check_winner(self) -> bool:
        """Checks if the current player has won."""

        for row in range(3):
            if (
                self.buttons[row][0]["text"]
                == self.buttons[row][1]["text"]
                == self.buttons[row][2]["text"]
                != " "
            ):
                return True

        for col in range(3):
            if (
                self.buttons[0][col]["text"]
                == self.buttons[1][col]["text"]
                == self.buttons[2][col]["text"]
                != " "
            ):
                return True

        if (
            self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
            != " "
        ):
            return True

        if (
            self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
            != " "
        ):
            return True

        return False

    def is_draw(self) -> bool:
        """Checks if the game is a draw."""
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == " ":
                    return False
        return True

    def reset_board(self) -> None:
        """Resets the board for a new game."""

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]:
                    self.buttons[row][col]["text"] = " "
        self.current_player = self.user_choice

    def reset_game(self) -> None:
        """Resets the game, scores, and allows players to choose X or O again."""
        self.x_wins = 0
        self.o_wins = 0
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]:
                    self.buttons[row][col].destroy()  # Remove existing buttons
        self.create_player_choice()  # Recreate player choice screen


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
