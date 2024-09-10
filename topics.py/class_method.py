# class Employee:
#     a=1
#     def show(self):
#         print(self.a)

# e=Employee()
# e.a=10
# e.show()  #10 : instance attribute

# To show or diplay class attribute we use class methos or decorator
       
class Employee:
    a=1
    @classmethod
    def show(cls):
        print(cls.a)

e=Employee()
e.a=10
e.show()  #1: class attribute is displayed
