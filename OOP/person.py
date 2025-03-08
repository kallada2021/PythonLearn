class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def person_info(self):
        print(f"{self.name} is {self.age} years old.")

person_information = Person("John", 42)
person_information.person_info()

###Encapsulation

class Person:
    name = "Public name"
    def __init__(self, name):
        self.name = name
    
    def public_method(self):
        print(f"I am a public method.")
        print(f"I am {self.name}.")

person_info = Person("Thomas")
person_info.public_method()

# Public and Private attributes

class Person:
    # name = "Public Name"
    # __address = "Private Address"

    def __init__(self,name,__address):
        self.name = name
        self.__address = __address
    
    def public_method(self):
        print(f"Hi, I am {self.name}")
    
    def private_method(self):
        # self.__address = "800 Blvd of Dreams"
        print(f"Hi, I am {self.name} and I live at {self.__address}")
    
person_info1 = Person("Bob", "700 Queens Rd")

print(person_info1.name)
person_info1.public_method()

# print(person_info1.__address)
person_info1.private_method()

