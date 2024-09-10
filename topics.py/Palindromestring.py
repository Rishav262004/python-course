def palindrome(str):
    
    #cleaning string : removing whitespaces
    clean_str = (str.replace(" ","")).lower()
    
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str= input("Enter a string :")

if palindrome(str):
    print("It is palindrome")
else:
    print("Not a palindrome")