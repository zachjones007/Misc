global list 

class Pet:
    
    def __init__(self, age = 0,name= " ",type= " ",doctor= " "):
         self._name = name
         self._age = age
         self._type = type
         self._doctor = doctor

    def get_list(self):
        return [self._age] + [self._name] + [self._type]
        petlist = [get_list]

    def get_doctor(self):
        return self._doctor 
        doctor = get_doctor
  
    def set_age(self, vet):
        self._age = vet
    
    def set_name(self, vet):
        self._name = vet

    def set_type(self, vet):
        self._type = vet

    def set_doctor(self, vet):
        self._doctor = vet
       

    def get_age(self): 
        return self._age

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type 

    def get_doctor(self):
        return self._doctor
    
  
p = Pet()
  
# setting the age using setter
p.set_age(float(input("Enter the age: ")))
p.set_name(input("Enter the name: "))
p.set_type(input("Enter the type: "))
p.set_doctor(input("Enter the doctor: "))
  
# retrieving age using getter
print("the pets age is: ",p.get_age())
print("the pets name is: ",p.get_name())
print("the pets type is: ",p.get_type())
print("the pets doctor is: ",p.get_doctor())

#orginze the lists
petlist = p.get_list()
doctor = p.get_doctor()
list = [doctor,petlist]
print(list)



  
