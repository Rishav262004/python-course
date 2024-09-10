# Strip a word from string and add it into a list

def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
    
l=["Rishav","Madhav","Keshav","av"]
print(rem(l,"av"))    # ['Rish', 'Madh', 'Kesh']