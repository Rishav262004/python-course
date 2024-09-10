# Create a class 2D vector and use it to create another class representing 3D vector

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
            print(f"The vector is {self.x}x + {self.y}y ")
        
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z
        
    def show(self):
        print(f"The vector is {self.x}x + {self.y}y + {self.z}z")
        

o=Vector2D(1,2)
o.show()
p=Vector3D(5,6,7)
p.show()