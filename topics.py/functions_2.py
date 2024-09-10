# Functions are the group of statements performing a specific task

# def avg():
#     a=int(input("Enter your first number : "))
#     b=int(input("Enter your second number : "))
#     c=int(input("Enter your third number : "))
    
#     average=(a+b+c)/3
#     print(average)

# avg()  #Calling a function

# --------------------------------------------------------------------- #

# def fun():  # Function definition
#     print("Hello from the function")
# fun()       # Function definition

# Function argument

# def nameit(name):
#     print("Hello", name)
# name=input("Enter your name: ")    
# nameit(name) # Hello Rishav

# Two arguments

# def add(a,b):
#     print(a+b)

# a=int(input("Enter your first number : "))
# b=int(input("Enter your second number : "))

# add(a,b) 

# default parametres

def nameit(name1, name2, ending="Thank you"):
    final_name = f"Hello {name1} {name2} {ending}"
    #print(final_name)
    return final_name

name1 = input("Enter your first name: ")
name2 = input("Enter your second name: ")

# Call the function and store the result in final_name
final_name = nameit(name1, name2)

# Print the final_name
print(f"The final name is: {final_name}")

