#  rock - paper - scissors game

'''
1 for rock
-1 paper
0 for scissors
    
'''
#  import random
    
# user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")
    
# if user_choice not in ["r", "p", "s"]:
    
#     print("Invalid choice. Please enter r for rock, p for paper, or s for scissors.")
#     print("")
  
# computer_choice = random.choice([-1,0,1])
# userDict={"r":1,"p":-1,"s":0}
# reverseDict={1:"rock",-1:"paper",0:"scissors"}
    
# user =userDict[user_choice]
    
# print(f"You chose {reverseDict[user]} \n Computer chose {reverseDict[computer_choice]}")
    
# if user == computer_choice:
#         print("It's a tie!")
# else:
#     if(computer_choice==1 and user==-1):
#             print("You win!")
#     elif(computer_choice==1 and user==0):
#             print("Computer wins!")
#     elif(computer_choice==-1 and user==1):
#             print("Computer wins!")
#     elif(computer_choice==-1 and user==0):
#             print("You win!")
#     elif(computer_choice==0 and user==1):
#             print("You win!")
#     elif(computer_choice==0 and user==-1):
#             print("Computer wins!")
#     else:
#             print("Error: Invalid condition")
            
            
#  rock - paper - scissors game using function

'''
1 for rock
-1 paper
0 for scissors
    
'''

'''
import random
def play_game():
    
    user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")
    print("")

    if user_choice not in ["r", "p", "s"]:
    
     print("Invalid choice. Please enter r for rock, p for paper, or s for scissors.")
    
  
    computer_choice = random.choice([-1,0,1])
    userDict={"r":1,"p":-1,"s":0}
    reverseDict={1:"rock",-1:"paper",0:"scissors"}
    user = userDict[user_choice]
    
    print(f"You chose {reverseDict[user]} \nComputer chose {reverseDict[computer_choice]}")
    
    if user == computer_choice:
           print("It's a tie!")
    else:
        if(computer_choice==1 and user==-1):
            print("You win!")
        elif(computer_choice==1 and user==0):
            print("Computer wins!")
        elif(computer_choice==-1 and user==1):
            print("Computer wins!")
        elif(computer_choice==-1 and user==0):    
            print("You win!")
        elif(computer_choice==0 and user==1):
            print("You win!")
        elif(computer_choice==0 and user==-1):
            print("Computer wins!")
        else:
            print("Error: Invalid condition")
            

play_game()
'''

# ------------------------------------ Refactored code with functions -------------------------------------------


# import random

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (r for rock, p for paper, s for scissors, q to quit): ").lower()
#         if user_choice in ["r", "p", "s", "q"]:
#             return user_choice
#         print("Invalid choice. Please enter r for rock, p for paper, s for scissors, or q to quit.")

# def get_computer_choice():
#     return random.choice(["r", "p", "s"])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "r" and computer_choice == "s") or \
#          (user_choice == "p" and computer_choice == "r") or \
#          (user_choice == "s" and computer_choice == "p"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     choices = {"r": "rock", "p": "paper", "s": "scissors"}
    
#     while True:
#         user_choice = get_user_choice()
        
#         if user_choice == "q":
#             print("Thanks for playing!")
#             break

#         computer_choice = get_computer_choice()

#         print(f"\nYou chose {choices[user_choice]}")
#         print(f"Computer chose {choices[computer_choice]}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)
#         print("\nLet's play again!\n")

# if __name__ == "__main__":
#     play_game()



# ---------------------------------- Refactored code with class : -----------------------------------------------

# import random

# class RockPaperScissors:
#     def __init__(self):
#         self.choices = {"r": "rock", "p": "paper", "s": "scissors"}
#         self.scores = {"user": 0, "computer": 0, "ties": 0}

#     def get_user_choice(self):
#         while True:
#             user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
#             if user_choice in self.choices:
#                 return user_choice
#             print("Invalid choice. Please enter r for rock, p for paper, or s for scissors.")

#     def get_computer_choice(self):
#         return random.choice(list(self.choices.keys()))

#     def determine_winner(self, user_choice, computer_choice):
#         if user_choice == computer_choice:
#             self.scores["ties"] += 1
#             return "It's a tie!"
#         elif (user_choice == "r" and computer_choice == "s") or \
#              (user_choice == "p" and computer_choice == "r") or \
#              (user_choice == "s" and computer_choice == "p"):
#             self.scores["user"] += 1
#             return "You win!"
#         else:
#             self.scores["computer"] += 1
#             return "Computer wins!"

#     def play_game(self):
#         user_choice = self.get_user_choice()
#         computer_choice = self.get_computer_choice()
#         print(f"\nYou chose {self.choices[user_choice]}\nComputer chose {self.choices[computer_choice]}")
#         result = self.determine_winner(user_choice, computer_choice)
#         print(result)
#         print(f"\nScores:\nYou: {self.scores['user']}\nComputer: {self.scores['computer']}\nTies: {self.scores['ties']}\n")

# if __name__ == "__main__":
    # game = RockPaperScissors()
    # while True:
    #     game.play_game()
    #     play_again = input("Do you want to play again? (y/n): ").lower()
    #     if play_again != 'y':
    #         break


# ------------------------------

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors, q to quit): ").lower()
        if user_choice in ["r", "p", "s", "q"]:
            return user_choice
        print("Invalid choice. Please enter r for rock, p for paper, s for scissors, or q to quit.")

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = {"r": "rock", "p": "paper", "s": "scissors"}
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == "q":
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose {choices[user_choice]}")
        print(f"Computer chose {choices[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("\nLet's play again!\n")

if __name__ == "__main__":
    play_game()
