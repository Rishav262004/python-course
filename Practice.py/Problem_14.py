# High score game #

import random
def high_score_game():
    print("You are playing the game...")
    score=random.randint(1,100)
    
    #Fetch the highscore
    
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    print(f"Your score =  {score}")
    if(score>hiscore):
        print("Congratulations! You have a new highscore!")
        
        #Write the new highscore
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    
    return score

high_score_game()