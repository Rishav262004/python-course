
# while loop
# list=["Rishav","is","a","good","boy"]

# i=0

# while(i<len(list)):

#     print(list[i])
#     i+=1

# ----------------------------------------------------------------- #

# for loop

# for i in range(4):
    # print(i, end=' ') # 0 1 2 3 :- that is it goes from 0 to n-1

# for i in range(0,100,20):
    # print(i, end=' ') # 0 20 40 60 80 :- that is it goes from 0 to 100 with a step of 20
    
# name="Rishav"

# for i in name:
#     print(i, end='-') #R-i-s-h-a-v-

# iterable for loops

# list=["Rishav","is","a","good","boy"]
# tuple=(1,3,5,2,4)

# for i in list:
#     print(i, end=' ') # Rishav is a good boy

# print("\n") : for the creation of new line

# for t in tuple:
#     print(t, end=' ') # 1 3 5 2 4
    
# ----------------------------------------------------------------- #

# for with else

# tuple=(1,3,5,2,4)
# for t in tuple:
#     print(t, end=' ')
# else:
#     print("\nNo element left in the tuple")

# ----------------------------------------------------------------- #

# break continue and pass statements

# for i in range(0,20,2):
#     if i==12:
#         break # exits the loop
#     print(i, end=' ')  # 0 2 4 6 8 10 
    
# for i in range(0,20,2):
#     if i==12:
#         continue # skips the iteration
#     print(i, end=' ') # 0 2 4 6 8 10 0 2 4 6 8 10 14 16 18 
    
# i=0

# for i in range(10):
#     pass # does nothing and just skips the iteration (null statement in python and instructs to do nothing)

# print(i) # 9 : it will print 9 as it is the last statement in the loop and it does not break or continue the loop
    
# ----------------------------------------------------------------- #

# num=int(input("Enter the numnber : "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}") # 5 x 1 = 5 5 x 2 = 10 5 x 3 = 15 5 x 4 = 20 5 x 5 = 25 5 x 6 = 30 5 x 7 = 35 5 x 8 = 40 5 x 9 = 45 5 x 10 = 50 
    
for i in range(10):
   pass 

print(i) # 9 

    