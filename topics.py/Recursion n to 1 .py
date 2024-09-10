#def n_to_1(n):
    
    #base case
#    if n==0:
#      return
 #  print(n) #first rask is performed then the recursive function is called

    
    #recursive case
  #  n_to_1(n-1)
    
#n_to_1(5)

#1_to_n
        
#def n1_to_n (n):   
    #if n==0:
     #   return
    #n1_to_n(n-1) #first recursive function is called then the task of print is performed
    #print(n)

#n1_to_n(5)

# sum from 1 to n using recursion
def sumr(n):
    
    if n==1:
        return 1
    ans = n + sumr(n-1)
    return ans

n=int(input("Enter your number :"))
print(sumr(n))