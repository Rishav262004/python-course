# ---------------------------------------------- for single text line --------------------------------------------- #

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

""" The same can be written as """

with open("file.txt") as f:
    data = f.read()
    print(data)   #or directly print(f.read())
    
"""In this you don't have to explicitly close the file."""    

# ---------------------------------------------- for single line with comments --------------------------------------------- #
# ---------------------------------------------for multiple text line -------------------------------------------- #

# f=open("file.txt")
# lines=f.readlines()

# print(lines , type(lines))

# f.close()

# --------------------------------------------- for writing into a file ------------------------------------------- #

"""
w is open for writing the file
r is open for reading
a is open for appending to the file (it creates the file if it does not exist)
+ is open for updating
rb is open for read in binary module
rt is open for raed in text module




"""
