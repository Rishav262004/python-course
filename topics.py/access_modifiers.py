#control the visibility/access of class attributes and functions

#eg : public # by default
    #protected
    #private
    


#public modifier  #by default
#class abc:
    
    #def __init_(self):
     #   self.public_attribute=None #public attribute
    
    #def public_function(): #public function
     #   pass
    
#obj1 = abc()
#obj1.public_attribute
#obj1.public_function()
            
#private modifier

# class abc:
      #def __init_(self):
     #   self.__private_attribute=None #private attribute
     # prefix of two underscore is used
    #def __private_function(): #private function
     #   pass
    
# obj1 =abc()
#print(obj1.__private_attribute)  :- output : error
    # now these attributes or class which are now private modifiers can be accssed only within the class and not outside it.
    
#protected modifier
# sub class or the class which inherit the properties of parent class can access these attributes
 # class abc:
      #def __init_(self):
     #   self._protected_attribute=None #protected attribute
     # prefix of one underscore is used
    #def _protected_function(): #protected function
     #   pass
    

    
    
    
    