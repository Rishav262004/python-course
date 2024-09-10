def fibonacci(n):
    if n==1:
        #base case
        return 0
    elif n==2:
        #base case
        return 1
    else:
        #recursive case
        return (fibonacci(n-1)+fibonacci(n-2))

n= int(input(":Enter your number : "))
#print(fibonacci(n))

#to print all the numbers inj the sequence
for i in range(1,n+1):
    print(fibonacci(i))