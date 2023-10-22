import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [' ' for _ in range(9)]

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=('Arial', 20), height=4, width=8,
                                   command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def clicked(self, row, col):
        idx = 3 * row + col
        if self.board[idx] == ' ':
            self.board[idx] = self.current_player
            self.buttons[idx]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button['text'] = ' '
        self.current_player = 'X'


if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
