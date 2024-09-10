#def add(x,y): #defining a function
    #sum=x+y
    #return sum  #returning the end result
   
#positional argument
#print(add(5,7)) #calling  a function

#keyword argument (named arguments)
#print(add(x=3 , y=5))

#Default arguments
#print(add(3)) the value of y is taken 0 by default
# If value is assigned while defining a function then that value is considered as default value
#def add(x,y=3) : if while calling  a function i do not specify the values then the default values of x and y is taken as 0 and 3 respectively.

# Arbitary arguments ( variable-length arguments *args and **kwargs)
#here *args is taken as tuple in function

#def add(*args):
 #   sum=0
  #  for i in args:
   #     sum+=i
    #return sum
#print(add(1,2,3,4)) : out : 10 ; #calling a function 

# **kwargs : key-value pair arguments or keyword arguments.
# here **kwargs are taken as dictionary
 
#def student_info(**kwargs):
 #   for x,y in kwargs.items():
  #      print(x,"is",y)

#student_info(name ="Rishav", age =20 , city="navsari")
#student_info(name= "Hiamnshu",age=20,city="navsari")

#function should be defined before calling it

#creating a function to sum numbers upto n given by user

def sum(n):
    add =0
    for i in range(1,n+1):
        add+=i
    return add

#Always take input outside the defined function not under it
n=int(input("Enter yoour number"))
inputn = sum(n)
print(inputn)
