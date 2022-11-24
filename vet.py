#zach jones 
#10/23/22
#cis 129 

class Pet:
    def __init__(self, age = 0,name= " ",type= " "):
         self._name = name
         self._age = age
    
    def get_age(self):
        return self._age
      

    def set_age(self, vet):
        self._age = vet
    
    def get_name(self):
        return self._name
    
    def set_name(self, vet):
        self._name = vet

    def set_type(self, vet):
        self._type = vet

    def get_type(self):
        return self._type
    
  
p = Pet()
  
# setting the age using setter
p.set_age(float(input("Enter the age: ")))
p.set_name(input("Enter the name: "))
p.set_type(input("Enter the type: "))
  
# retrieving age using getter
print("the pets age is: ",p.get_age())
print("the pets name is: ",p.get_name())
print("the pets type is: ",p.get_type())
  
