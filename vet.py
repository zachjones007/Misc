def main():
    animals = []
    while True :
        class Pet:
        
            def __init__(self, options):
                self._name = options
                self._animal_type = options
                self._age = options

            def set_name(self, new_name):
                self._name = new_name

            def set_animal_type(self, new_type):
                self._animal_type = new_type

            def set_age(self, new_age):
                self._age = new_age

            def get_name(self):
                return self._name

            def get_animal_type(self):
                return self._animal_type

            def get_age(self):
                return self._age

        animal_type = input("input pet type")
        name = input("input pet name")
        age = input("pet age")

        pet = Pet({'name': name, 'type': animal_type, 'age': age})
        animals.append (animal_type)

        print("pet name is", pet.get_name())

        print (animals)
        option = str(input('would you like to contiune? yes or quit '))
        for letter in option:
                if letter in "n,N,q,Q":
                    quit("quittting")
main()