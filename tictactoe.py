import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text=" ",
                    font=("Helvetica", 24),
                    width=6,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True

        for col in range(3):
            if all(row[col] == self.current_player for row in self.board):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
