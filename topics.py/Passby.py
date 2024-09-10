#Pass by value :

# for immutable objects such as strings, integers, tuples etc.
# when passed to function a copy of object is created and assigned to a local variable in a function

#def add(x,y):
 #   sum = x+y
  #  return sum
#a=2 #no change in the variable a and b while calling the function because it is locally assigned and are the copy of the real objects or parameters x and y
#b=3 #any change made to them inside function do not affect the original variable outside function.
#print(add(a,b))

#def add(x):
 #   x=x+1
  #  print("Inisde function : ",x) #6 #inside function
    
#x=5
#add(x) #calling  a function 

#print("outside frunction :", x)  #5 #outside function


#Pass by reference :
#for mutable objects like lists, dictionary
#refrence to actual object is passed to function
#changes inside a function will affect the original object

def modifylist(lst):
    lst.append(4)
    print("Inside function : ", lst) # 1,2,3,4

lst =[1,2,3]
modifylist(lst)
print("Outside function: " , lst) # 1,2,3,4