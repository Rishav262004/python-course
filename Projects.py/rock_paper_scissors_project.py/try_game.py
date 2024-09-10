import tkinter as tk
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x300")

        self.choices = {"r": "rock", "p": "paper", "s": "scissors"}
        self.scores = {"user": 0, "computer": 0, "ties": 0}

        self.create_widgets()

    def create_widgets(self):
        # Add labels to display choices and results
        self.user_label = tk.Label(self.root, text="Your Choice: ")
        self.user_label.pack()

        self.computer_label = tk.Label(self.root, text="Computer's Choice: ")
        self.computer_label.pack()

        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack()

        self.score_label = tk.Label(self.root, text="Scores - You: 0, Computer: 0, Ties: 0")
        self.score_label.pack()

        # Add buttons for rock, paper, and scissors
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("r"))
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("p"))
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("s"))
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

    def get_computer_choice(self):
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.scores["ties"] += 1
            return "It's a tie!"
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            self.scores["user"] += 1
            return "You win!"
        else:
            self.scores["computer"] += 1
            return "Computer wins!"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        self.user_label.config(text=f"Your Choice: {self.choices[user_choice]}")
        self.computer_label.config(text=f"Computer's Choice: {self.choices[computer_choice]}")
        self.result_label.config(text=f"Result: {result}")
        self.score_label.config(text=f"Scores - You: {self.scores['user']}, Computer: {self.scores['computer']}, Ties: {self.scores['ties']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
