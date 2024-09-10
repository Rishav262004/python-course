#input list using f function

n=int(input("Enter your number of elements : "))
list=[]

for i in range(n):
    num=int(input(f"Enter your number {i+1} : "))
    list.append(num)
    list.sort()
    
    print(list)
    
    
    