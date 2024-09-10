#Object oriented programming
#procedure oriented programming
#is a programming paradigm where the software design revolves around the object/data rather than functions
#helps to mimic real world entities and their interactions
#code reusability, regulation , organisation , sustainability of code

#classes and objects

# classes :
# user defined data types
#blueprint or template for an object
# eg : admission form
#class has some properties like : attributes(length , colour etc...), methods , functions


#object
# an instance of type class
# mimic real world entities
# eg : filling out data in admission froms such as : name, age is an example of object

# ---------------------------------------------------------------- #

# class Student:
#     name="Rishav"   #class attribute
#     age=20
# details=Student()

# details.gender="male"
# details.name="Rishav Mishra" #instance attribute

# #accessing the attributes of the class
# #instance attribute has more priority over class attribute.

# print(details.name,f"age is {details.age} and gender is {details.gender}")
    
    
# ----------------------------------------------------------------- #

# class Student:
#     language ="Python" #class attribute
#     salary = 100000
    
    
#     def __init__(self):   #no need to call this function 
#         # dunder method which is automatically called and starts with double underscore {only in it function}
#         print("Rishav Mishra") 
        
#     def display_details(self):
#         print(f"Language: {self.language}, Salary: {self.salary}")
     
#     @staticmethod #no need of self then
#     def trying():
#      print("This is a method")
       
# #creating objects

# student1 = Student()
# student1.language ="Java" #instance attribute more preference than class attribute



# student1.display_details() # object_name.function_name()
# #or this is nothing but Student.display_details(student1) = class_name.function_name(object_name)
# student1.trying()

# ----------------------------------------------------------------------------------------------------------- #

# class Student:
#     language ="Python" #class attribute
#     salary = 100000
    
#     def __init__(self,name,salary,language):
        
#         self.name=name
#         self.salary=salary
#         self.language=language
#         print("just a call")
        
#     def getinfo(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}")
    
#     @classmethod or @staticmethod ---> decorator
#     def great():
#         print("called without slef")
        
# student1 = Student("Rishav",132000,"Kotlin")
# print(student1.name , student1.language)

#-------------------------------------------------------------------------------------------------#

# class demo:
#     a=5
# c=demo()
# print(c.a) #5   class attribute gets printed

# c.a=7
# print(c.a) # 7 Instance attribute gets printed

# print(demo.a) #5 But the original value of class attribute does not gets changed

#--------------------------------------------------------------------------------------------------#