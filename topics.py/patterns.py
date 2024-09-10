'''
for n =3
      *
     ***
    *****
'''

# num=int(input("Enter the number : "))

# for i in range(1, num+1):
#     print(" " * (num-i) + "*" * (2*i-1))
    
    #Output :- Enter the number : 5
                #       *
                #      ***
                #     *****
                #    *******
                #   *********
                
# -------------------------------------------------------------------- #

'''
for n =3
      *
     **
    ***
'''
                
# num=int(input("Enter the number : "))

# for i in range(1, num+1):
#     print(" " * (num-i) + "*" * (i))
    
    #Output :- Enter the number : 5
                   #      *
                   #     **
                   #    ***
                   #   ****
                   #  *****
            
# --------------------------------------------------------------------------------   #

'''
for n =3
    *
    **
    ***
'''

# num=int(input("Enter the number : "))

# for i in range(1, num+1):
#    print("*" * (i))
    
    #Output :- Enter the number : 5
                    # *
                    # **
                    # ***
                    # ****
                    # *****
                    
# ------------------------------------------------------------------------------------- #

'''
for n = 5
    *****
    *   *
    *   *
    *   *
    *****
'''

# num=int(input("Enter the number : "))

# for i in range(1, num+1):
#     if i == 1 or i == num:
#         print("*" * num,end="")
#     else:
#         print("*",end="")
#         print(" "*(num-2),end="")
#         print("*",end="")
#     print("")
    
    #Output :- Enter the number : 5
    # *****
    # *   *
    # *   *
    # *   *
    # *****

# ------------------------------------------------------------------------------- #


'''
for n = 5

    *****
    ****
    ***
    **
    *
    
'''

# def pattern():
    
#     num=int(input("Enter the number : "))
#     for i in range(num,0,-1):
#       print("*" * i,end="")
#       print("")

# pattern()
    
#     # Output :- Enter the number : 5
#     # *****
#     # ****
#     # ***
#     # **
#     # *
    
# ------------------------------------------------------------------------------- #

'''
for n = 5 [Using recurssion]

    *****
    ****
    ***
    **
    *
    
'''
# def pattern(n):

#     if n == 0:
#          return
#     else:
        
#         print("*"*n, end="")
#         print("")
#         pattern(n-1)
        
# n=int(input("Enter your number : "))
        
# pattern(n)

#---------------------------------------------------------------------------------------#

