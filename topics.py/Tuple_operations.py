#Enclosed within parenthesis()
#Tuples are immutable
#To take tuple of only one item we shall add a comma(',') after that

colours =("red",)
#Tuple with only one element
#If we do not add a comma it will recognise  it as a string.
#fruits =("Orange","Mango","Apple")

#Another way to create a tuple, list , dict or a set
#In this tuple is used as constructor

fruits = tuple(("Apple","Banana","Cherry","Mango"))
#Similarly a= list[]
#          a= set{} or dict{}
#In this way to crate a tuple with only one element
#colours = tuple(("red")) :- No need of comma

#Indexing
#Positive indexing
#print(fruits[1])

#Negative indexing
#print(fruits[-1])

#Range indexing
#First digit of range is inclusive i.e n
#Second digit of range is exclusive i.e n-1
#print(fruits[0:2])
#Range is from 0 to 1

#If we do not p rovide starting or any
#ending point then the wjole left out tuple is taken at that time

#To check an item in tuple
#if "Mango" in fruits:
 #   print("Mango is present")
 
 #To traverse
#for i in fruits:
#   print(i , end=" ")

#Unpacking a tuple
fruit1 , fruit2,  fruit3 , fruit4= fruits
print(fruit1 , fruit2 , fruit3 , fruit4)

#reverse a tuple
input_tuple =(1,2,3,4,5,6)
list =[]
for i in reversed(input_tuple):
    list.append(i)
output_tuple = tuple(list)

print(output_tuple, type(output_tuple))