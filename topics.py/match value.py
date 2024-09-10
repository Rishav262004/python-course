#Enter only positive integers.
n1 = int(input("Enter your 1st number : "))
n2 = int(input("Enter your 2nd number : ")) 
#n3 = int(input("Enter your 3rd number : ")) 
#input oprator such as +,-,*,/,% 
operator = input("Enter your operator : ")

match operator:
    case "+":
        print("Sum of two numbers is : " , n1+n2)
    case "-":
        print("Difference of two numbers is : " , n1-n2)
    case "*":
        print("Product of two numbers is : " , n1*n2)
    case _ :
        print("Divide is not done")