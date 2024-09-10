#   Understanding the len behaviour

# s={18,"18"}

# print(s)
# print(len(s)) # Returns the number of items in the set and as both values are of different data 
# types it includes both int 18 and string 18 

s={18,18.0,"18"}

# print(s)            {18, '18'}
# print(len(s))         2   :- Because in python the value is compared and not the data type hence 18==18.0 gives True