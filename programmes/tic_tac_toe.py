import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):  # Corrected constructor
        self.root = root
        self.root.title("🎮 Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('Helvetica', 24), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="Restart", font=('Helvetica', 14),
                                      command=self.reset_game, bg='lightblue')
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def on_click(self, index):
        if self.buttons[index]['text'] == "" and not self.check_winner():
            self.buttons[index]['text'] = self.current_player
            self.board[index] = self.current_player

            if self.check_winner():
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
            elif all(cell != "" for cell in self.board):
                messagebox.showinfo("Game Over", "🤝 It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combos:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                for i in combo:
                    self.buttons[i].config(bg='lightgreen')
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg='SystemButtonFace')
        self.current_player = "X"

# Corrected main function
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
