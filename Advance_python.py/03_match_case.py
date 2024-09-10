
    
def status_check(status):
    match status:
        case 'active':
            print("Account is active")
        case 'inactive':
            print("Account is inactive")
        case 'suspended':
            print("Account is suspended")
        case 'deleted':
            print("Account is deleted")
        case _:
            print("Invalid status")
            
status =input("Enter the status : ")
print( status_check(status))