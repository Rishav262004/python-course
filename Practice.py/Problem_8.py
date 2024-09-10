# Percentage calculator
# Calculate the percentage of marks of a student and total should be >40% and individually marks should be >=33

marks1=int(input("Enter your marks1 : "))
marks2=int(input("Enter your marks2 : "))
marks3=int(input("Enter your marks3 : "))

total_percentage=((marks1+marks2+marks3)/300)*100

if total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("Your total percentage is :", total_percentage)
else:
    print("Your total percentage is less than 40 or marks are less than 33.")