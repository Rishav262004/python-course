list1 = ["Apple","Bnanna", "Cherry","Mango"]
list2 = ["Yes","No","True","False"]

#append adds at the end of the list.
list1.append("Grapes")

#multiline comment ''' ... '''
'''insert adds at the specific index 
 and shifs the others on right side 
 and the previous elements do not change''' 
list1.insert(2,"Pear")

'''extend is used to add two lists especially 
 when they are of two differnet data types.'''
#or just use "+" operator to concatenate two list
list1.extend(list2)
#print(list1)

#remove() function removes the sepcific value passed
#list2.remove("Yes")

#pop() function removes at specified index value of if index is not mentioned then the last element is removed. 
list2.pop(2)
print(list2)