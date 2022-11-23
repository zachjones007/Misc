
  
class Pet:
    def __init__(self, age = 0,name = '',type = ''):
         self._age = age
         self._name = name
         self._type = type
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x

    def set_name(self):
        return self._name

    def get_name(self,y):
        self._name = y

    
  
p = Pet()
  
# setting the age using setter
p.set_age(21)
  
# retrieving age using getter
print(p.get_age())
  
print(p._age)