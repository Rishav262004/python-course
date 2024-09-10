def factorial(n):
    if n==0:      #base case
        return 1  #base case for termination of function
    
    ans =n * factorial(n-1) #recursive case
    return ans

n=int(input("Enter your number : "))
print(factorial(n))