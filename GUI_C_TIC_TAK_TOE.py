
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"  # You start
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text=" ", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":  # Only allow X to play manually
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O"  # Switch to computer

                # After player makes a move, let computer play
                self.computer_move()

    def computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        
        if empty_cells:
            # Randomly select an empty spot for the computer to play
            row, col = random.choice(empty_cells)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "X"  # Switch back to player

    def check_winner(self):
        for i in range(3):
            # Check rows and columns
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def is_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToe().run()
