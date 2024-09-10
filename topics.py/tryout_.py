import random

def guess_game():
    n = random.randint(1, 100)  # Random number between 1 and 100
    a = -1
    guess = 0
    
    print("Welcome to the Guessing Game!")
    
    while a != n:
        guess += 1
        a = int(input("Guess the number (between 1 and 100): "))
        
        if a > n:
            print("Your guess is too high.")
        elif a < n:
            print("Your guess is too low.")
        
    print(f"Congratulations! You guessed the correct number {n} in {guess} attempts.")
    
    return guess

def high_score_game():
    while True:
        print("Let's see if you can set a new high score!")
        
        # Play the guessing game
        attempts = guess_game()
        
        # Fetch the current high score (minimum number of attempts)
        try:
            with open("hiscore.txt", "r") as f:
                hiscore = f.read()
                if hiscore:
                    hiscore = int(hiscore)
                else:
                    hiscore = float('inf')  # Set to infinity if no previous score
        except FileNotFoundError:
            hiscore = float('inf')  # No file yet, set high score to infinity
        
        print(f"Your score (number of attempts) = {attempts}")
        
        # Update high score if the player has a better (lower) score
        if attempts < hiscore:
            print("Congratulations! You have set a new high score!")
            
            # Write the new high score to the file
            with open("hiscore.txt", "w") as f:
                f.write(str(attempts))
        else:
            print(f"The current high score is {hiscore} attempts.")
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! See you next time.")
            break

# Start the high score game loop
high_score_game()

