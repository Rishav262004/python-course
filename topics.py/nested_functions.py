def outer_function():
    x=1 #Variable in outer function
    
    def inner_function():
        y=2 # variable in inner function
        result = x+y
        return result
    
    return inner_function() #returning the result by returning the function at the end

output = outer_function() # calling the main function : i.e oiuter

print(output)