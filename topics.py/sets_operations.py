# We cannot update elements in a set but can have elements of different data types
# We can add or remove but cannot update an existing element
# Duplicates are not allowed in a set (Two elements of same value is not allowed)
# unindexed(indexing is not allowed) & unordered
# enclosed within {...}
# We cannot include a list inside a set
# a=set() this is how we create an empty set if we do set{} then it will create an empty dictionary
#list cannot be included under set because sets in python require all their elements to be immutable and hashable and snce list are mutable it cannot be included under sets.



fruits ={"apple","mango","banana"}

#To access elements in a set we cannot use indexing
#we have to run "for" loop for that

#for i in fruits:
#   print(i)

#To check elements in a set
#if "apple" in fruits:
#   print("apple is present")
    
#To add elements in a set we use add function
#fruits.add("Cherry")

#To add sequence of another datatype
#we use update function

#name_list =["Sia","Kate","Joy"]
#fruits.update(name_list)

#To remove an element in a set we use remove function

#fruits.remove("mango")

#remove function will give error if we try to remove something which is not present in a set
#we use discard function in that case
#if the element is present it will be removed
#if the element is not present then it prints the existing set without giving any error.

#fruits.discard("pear")

#joining 2 sets
s1 = {1,2,3,4}
s2 = {5,6,7,8,4}

#1 .use of union function
#Duplicate values are not printed in a set i.e 4 is printed only once
#s3 =s1.union(s2)
#print(s3)

#use of update function
#s1.update(s2)
#print(s1)    

#keep only duplicates while joining
#s1.intersection_update(s2)
#intersection_update will store the comoon values of both set in s1 thus it will update s1
#intersection will store the duplicates in a new set , no update in the existing set
#print(s1)

#Keep all values except duplicates
#s1.symmetric_difference_update(s2)
#print(s1)

#Program to find common elements in 3 sets

list1 =[1,2,3,4]
list2 =[3,4,5,6]
list3 =[3,4,7,8]

#typecasting
set1 =set(list1)
set2 =set(list2)
set3 =set(list3)

#Here we use intersection because we want to store common values in a new set
common_1 =set1.intersection(set2)
common_2 =common_1.intersection(set3)

final_list = list(common_2)

print(final_list)