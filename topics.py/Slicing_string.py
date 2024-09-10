#Syntax :- string= name [ind_start : ind_end]
# start is inclusive(included) and end is exclusive(not included) : Eg n, n-1
#slicing is used to get part of  a string
#slicing from start : str[:end] ; str[:endvalue+1]
#slicing till end : str[start:]
#negative indexing also work in slicing : str[-stratvalue: ]; str[-startvalue:-endvalue]

name="Rishav"
name_2="Vishakapatnam"
name_short= name[0:4]


print(name_short)               # output:- Rish
print(name[-6:-1])              # output:- Risha  
print(name[:4])                 # output:- Rish   is same as name[0:4]
print(name[0:6])                # output:- Rishav
print(name[0:])                 # output:- Rishav  is same as name[0:length] = [0:6]

print(name_2[1:6:2])            # output:- ihk    [x:y:z]= [range_start:range_end-1:jump/skipvalue]