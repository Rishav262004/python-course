class Student:
    
    def set_name(self, name):
        self.name=name #class attribute
    
    def get_name(self):
        return self.name
    
student1=Student() #object is created for class student
student1.set_name("Rishav") #calling a function by making an object
#print(student1.name) : out : Rishav
#self by default signifies the object that is to be passed
print(student1.get_name())# get_name function is called and student1 goes to the self parameter as an object
#student1.eng_marks = 45 : #instance attribute

student2 = Student()
student2.set_name("Parag")

print(student2.get_name())