def factorial(n):
    fact=1
    if n==0:
        fact=1
    else:
        for i in range(1,n+1):
            fact*=i
    
    return fact

n=int(input("Enter your number : "))

output = factorial(n)
print(output)