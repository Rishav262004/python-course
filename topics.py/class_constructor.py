#special function that gets invoked everytimne an object is created for the class

#syntax:
#def __init__(self,parameter1,parameter2,...):
#initialize instance variables(attributes) here
#self shows the object instance

class Rectangle:
    
    def __init__(self, height , width):
        print("The height of rectangel is {} , and width is {}".format(n1,n2))
        self.height=height
        self.width=width
    
    def area(self):
        return self.height * self.width    
    

n1=int(input("Enter your height : "))
n2=int(input("Enter your width : "))

#creating objects
rectangle1=Rectangle(n1,n2) #passing parametres with class
print("The height and width are : " , rectangle1.height , rectangle1.width)
print(rectangle1.area())
 


