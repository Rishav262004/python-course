# Using replace function 

# Replace the following with input name and date

letter='''Dear <|Name|>
        You are selected
        for the interview on <|Date|>.'''
        
name=input("Enter your name : ")

date=input("Enter the interview date (dd/mm/yyyy) : ")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))