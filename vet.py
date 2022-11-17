class Employee:
    def __init__(self): #Constructor
        self.__id = 0
        self.__name = ""
        self.__gender = ""
        self.__city = ""
        self.__salary = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

def main():
    print("Enter Employee Data:")
    i = int(input("Enter Id\t:"))
    n = input("Enter Name\t:")
    g = input("Enter Gender:")
    c = input("Enter City\t:")
    s = int(input("Enter Salary:"))

    e=Employee()
    e.id=i
    e.name=n
    e.gender=g
    e.city=c
    e.salary=s
    id2 = e.id
    name2 = e.name
    gender2 = e.gender
    city2 = e.city
    salary2 = e.salary


    print("\nDisplaying Employee Data:")
    print("Id\t\t:", id2)
    print("Name\t:", name2)
    print("Gender\t:", gender2)
    print("City\t:", city2)
    print("Salary\t:", salary2)


if __name__=="__main__":
    main()
