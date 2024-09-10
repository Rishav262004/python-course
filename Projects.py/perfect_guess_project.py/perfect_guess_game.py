from random import randint
n= randint(1,100)

a=-1
guess=0
while(a!=n):
    guess+=1
    a=int(input("Guess the number : "))
    
    if(a>n):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
        
    if(a==n):
        print("Congratulations! You guessed the correct number.")
        
print(f"You have gussed the correct number {n} in {guess} attempt")