#We store key-value pairs
#"keys" can be any primitive data type while the "values" can be any arbitary python object
#enclosed in { key1:value1 , key2:value2 ...}
#values can be same but keys are always unique
#Dictionary is : unordered , Changable/mutable , indexed , Duplicates not allowed , Any datatype

# phones ={"Rish": 7874, "Abhi": 2222,"Tejus":9595 }

# print(phones, type(phones)) #{'Rish': 7874, 'Abhi': 2222, 'Tejus': 9595} <class 'dict'>
# print(phones['Rish']) #7874
#print(type(phones)) = dict
#print(len(phones)) = 3

#To access dictionary
#print(phones["Rish"])

#or by using get function
#print(phones.get("Rish"))

#To print keys
#print(phones.keys())

#To update values
# phones.update({"Rish":1234}) #{'Rish': 1234, 'Abhi': 2222, 'Tejus': 9595, 'Pranj': 4567, 'Amrit': 8521}
# Or
#phones["Rish"] = 9638

#-------------------------------------------------------------------------#

# print(phones["Rish"]) # 7874
# print(phones.get("Rish")) # 7874
# But
# print(phones["Rishav"]) # error
# print(phones.get("Rishav")) # none

# print(phones.items()) # dict_items([('Rish', 7874), ('Abhi', 2222), ('Tejus', 9595)])

#To add new entry in dict
# phones["Aadish"] = 1234
#print(phones) {'Rish': 7874, 'Abhi': 2222, 'Tejus': 9595, 'Aadish': 1234}

#To add a new dict we use update function

# more_phones ={"Pranj": 4567, "Amrit":8521}
# phones.update(more_phones)
# print(phones)

#To remove an element from dict
#phones.pop("Rish") 
#print(phones) = {'Abhi': 2222, 'Tejus': 9595}

#phones.popitem() : this will remove the last added item i.e Aadish in this case
#phones.popitem()
#print(phones)

#To clear the dictionary
# we ue phones.clear() function :- OUTPUT :{}

#To traverse

#This will print only keys not values
#for x in phones:
 #   print(x)
 
#This will print only values 
#for x in phones:
 #   print(phones[x])
 
 #To print both keys and values together
#for x in phones.items():
 #   print(x)
 
 #To print both keys and values seperately
#for x,y in phones.items():
 #   print(x,y)
     
 #Nested dictionary
#dict = { "dict1" :{"x":1, "y":2,"z":3}, "dict2" :{"a":4, "b":5 , "c":5}}

#print(dict["dict1"]["y"]) = output: 2

#To sum all the values of dict

# dict1= {"x":1 , "y": 2, "z":3}
# print(sum(dict1.values())) # output : 6

# User input 

# user_dict = {}
# num_entries = int(input("Enter the number of entries you want to add: "))
# for i in range(num_entries):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     # user_dict.update({key:value}) # Most imprtant to remember
#     # Or
#     # user_dict[key] = value # Most imprtant to remember 
# print("Dictionary after adding user input:", user_dict)


#  ------------------------------------------------------ #

words={"chair": "kursi" ,"sleepers" :"chappal","electricity":"power" }

word=input("Enter your english word : ")

if word in words:
    print(f"The translation for {word} in hindi is  {words[word]}")
else:
    print("Word not found in dictionary")
 
 