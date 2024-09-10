# properties

# 1. INHERITANCE :- 2 types - Single inheritance ,multiple inheritance , Multilevel inheritance , Hierarhical inheritance , hybrid inheritance
# where one class can inherit properties (attributes,functions) from another class

# syntax :

#class SuperClass:
    #Attributes and methods of superclass go here
    
#class SubClass(SuperClass):
    #Additional attributes and methods of the subclass gop here 
    
# class parent:
#     def __init__(self):
#         self.super_attribute = True
#         print("This is the parent class")
        
# class child(parent):
#     def __init__(self):
#        super().__init__() 
#        print("This is a child class")
#        print(self.super_attribute)
       
# child1 = child()
  
# -------------------------Multiple Inheritance --------------------------------------------------- #

# class Employee:
#     company = "Apple"
#     name="default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the comapny is {self.company} ")  
    
    
# class Coder:
#     language="Python"
#     def print_language(self):
#         print(f"The language used by the coder is {self.language}")
        
# class programmer(Employee,Coder):
#     company="Apple of MAANG"
#     def show_language(self):
#         print(f"The name is {self.company} and is good with {self.language} language")
    
# a=Employee()
# b=programmer()

# b.show()
# b.print_language()
# b.show_language()

# -------------------------------------- Multilevel Inheritance ------------------------------------- #


# class Employee:
#     company = "Apple"
#     name="default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the comapny is {self.company} ")  
    
    
# class Coder(Employee):
#     language="Python"
#     def print_language(self):
#         print(f"The language used by the coder is {self.language}")
        
# class programmer(Coder):
#     company="Apple of MAANG"
#     def show_language(self):
#         print(f"The name is {self.company} and is good with {self.language} language")
    
# a=Employee()
# b=programmer()

# b.show()
# b.print_language()
# b.show_language()

# -----------------------------SUPER Class------------------------------------------------------------------- #

class Employee:
    company = "Apple"
    name="default name"
    
    def __init__(self):
        print("Constructor of Employee")
    a=1
    
class Coder(Employee):
    language="Python"
    def __init__(self):
        print("Constructor of Coder")
    b=2  
        
class programmer(Coder):
    company="Apple of MAANG"
    def __init__(self):
        super().__init__()  # calling constructor of superclass Employee  output :- # Constructor of Coder
                                                                                    # Constructor of programmer 
                                                                                    # 3
        print("Constructor of programmer")
    c=3   
    
# o=Employee()
# print(o.a) #Constructor of Employee

# o=Coder()
# print(o.b) #Constructor of Coder

o=programmer()
print(o.c) #Constructor of programmer