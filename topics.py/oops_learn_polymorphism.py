# 2. polymorphism : many forms
# It allows objects of different classes to behave as objects of the same superclass
# 2 types : Run time and compile time polymorphism
# compile time polymorphism is resolved during compile time and can be achieved through :
# 1. Method overloading and operator overloading

#run time is resolved during run time and achieved through method over-riding



class animal:
    def speaks(): # Abstract method which will be overwritten  
        pass

class dog(animal):
    def speaks(self):
        print("Barks")

class cat(animal):
    def speaks(self):
        print("meow")
        
dog = dog() #creating instances
cat = cat()
        
dog.speaks() #calling a function
cat.speaks()
