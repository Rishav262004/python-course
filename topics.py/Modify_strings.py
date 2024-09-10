#for converting strings into uppercase
#str1 = "hello world"
#str2 = str1.upper()
#print(str2) :out : HELLO WORLD

#into lowercase
#str3 = str2.lower()
#print(str3) Out : hello world

#for capitalising first character of my string
#str4 = str3.capitalize()
#print(str4) out: Hello world

# for stripping/removing any trailing whitespaces
#str5="   hello world    " #trailing white spaces before and after string
#str6= str5.strip()
#print(str6)
#however these functions will not change the actual string i.e str5 on printing will give the same string with whitespaces trailing.

#replace() function
#replace old substring with new substring 'count' number of times
#giving count is optional
#if count is not given then all occurences of old substring is replaced
#if count is given then only the first occurence of that sub-string is replaced

#str1 = " hello world , hii world"
#str2 = str1.replace("world", "everyone") #count is not given then all the instances of "world" will get replaced by "everyone"
#str3 =  str1.replace("world","everyone",1) #count is given as 1 which means only the first occurence of "world" will be replaced by "everyone"

#print(str2) # hello everyone, hii everyone
#print(str3) #hello everyone , hii world.

#split() function
#Syntax: string.split(sep ,maxsplit) #contains optional parameters
#Used to split a string into list of substring
#maxsplit parameteres is used to give the value of how many number of times we need to split at the seperator
#default value of maxsplit(): is no limit : number of times seperator occurs it will split the function
#if we do not specify the value of seperator then by default it takes the value of whitespace " "

#str = "Apple Banana  Mango"
#str1=str.split()
#print(str1) #results into a list of substring

#str1= "ria,pia, sia, tia, nia"
#list= str1.split(",",2) #seperator , maxsplit(): when & where to seperate and how many times to sepearte
#print(list) # output : ['ria', 'pia', ' sia, tia, nia']

#use of format() function : used to insert some variable values in a string
#creates a placeholder value
fruit1="Mango"
fruit2="Apple"

#print("I have two fruits : {f1} and {f2}".format(f1= fruit1, f2=fruit2))
#print("I have two fruits : {} and {}".format(fruit1,fruit2))

#Escape characters
#Special characters that are used to sepearte some non-functional/ reserved characters in strings.
#eg: to print " ' " single aphostophie, it might showe some error while porinting it directly so we use " \' " to print it.
#for new line : "\n", for tab: "\t"
