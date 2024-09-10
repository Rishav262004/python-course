# #Exception handling
# try:
#     a=int(input("Enter a number : "))
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
#     exit


# -------------------or------------

# try:
#     a = int(input("Enter a number : "))
#     print(a)
    
# except Exception as e :
#     print(f"An error occurred: {e}")

# ------------------------------or ------------------------

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

if(b==0):
    raise ZeroExceptionEroor("Cannot divide by zero")

else:
    print("The result is : ", a/b)  