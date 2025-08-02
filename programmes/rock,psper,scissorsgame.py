import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to decide winner
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer choice: {computer_choice}\n{result}")

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), pady=20)
result_label.pack()

# Run the GUI loop
root.mainloop()