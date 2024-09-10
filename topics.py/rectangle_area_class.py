class Rectangle:
    
    def set_dimension(self,height,width):
        self.height=height
        self.width=width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
#creating objects
rectangle1=Rectangle()
n1=int(input("Enter your height : "))
n2=int(input("Enter your width : "))
rectangle1.set_dimension(n1,n2)
print("The height and width are :" , rectangle1.height , rectangle1.width)
print(rectangle1.area())
print(rectangle1.perimeter())