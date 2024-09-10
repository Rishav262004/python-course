def pow_ab(a,b):
    
    #base case
    if b==0:
        return 1
    #recursion
    ans = a* pow_ab(a,b-1)
    return ans

a =int(input("Enter your number : "))
b =int(input("Enter your power : "))

print(pow_ab(a,b))