#Strings are immutable during runtime but can be modified in a list
#We can manipulate and make new string out of them
#enclosed within single or double quotes '..' or "..."
#Multiline strings such as paragraphs can be written in '''...''' quotes
#Array like indexing , negative indexing is also allowed

#indexing
text ="Hello world"
#print(text[4]) #out : o

#traverse in a string
#using for loop
#for i in text:
 #   print(i)

#using list comprehension
#list =[char for char in text]
#for i in list:
 #   print(i)

#finding length of string
#spaces are also countred in string while calculating length and even at indexing
#print(len(text))

#To find a char/substring in a string
#we can use find() function
#find function gives the index of first occurence of char/sub-string
#if we try to find a char which is not present in our string then the find function will give output as -1.
#if we try to find a sub-strring then the index value of starting char is given a soutput which has its first occurence in string
#we can also find whitespace ' ' with help of find function. it will give us index value of first occurence of whitespace

#print(text.find('o')) #gives output as index value of given char 'o'
#print(text.find("ello")) #gives output as 1 beacuse 'e' comes at index value 1


# Functions in a string

#lower() function converts all uppercase characters to lowercase
#upper() function converts all lowercase characters to uppercase
#islower() function returns true if all characters in the string are lowercase
#isupper() function returns true if all characters in the string are uppercase
#isalpha() function returns true if all characters in the string are alphabets
#isalnum() function returns true if all characters in the string are alphanumeric
#isdecimal() function returns true if all characters in the string are decimal numbers
#isspace() function returns true if all characters in the string are whitespace


name="Thiruvananthapuram"

print(name.lower()) #thiruvananthapuram

print(name.upper()) #THIRUVANANTHAPURAM

print(name.islower()) #False

print(name.isupper()) #False

print(len(name))  # 18 :- finds the length of the string. 

print(name.find('a')) # 6  :-finds the location of particular character of the string

print(name.endswith("puram")) # True

print(name.startswith("Thiru")) # True  
print(name.startswith("thiru"))  # False :- case sensitive

