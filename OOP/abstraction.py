# Abstraction provides a layer of protection and ensures that the internal state of the object can only be altered in a controlled manner
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return f"{self.name} is {self.__age}"
    
    def set_age(self, age):
        if age == 5:
            self.__age = age
        return(self.__age)
    
    def increase_age(self,age):
        self.__age = age
        if self.__age > 30:
            self.__age = self.__age + 1
        return self.__age
    
    def have_birthday(self):
        self.__age += 1
        return self.__age
    

person = Person("Bob",30)
print(person.get_age())
print(person.increase_age(32))

person1 = Person("Thomas", 15)
print(person1.set_age(5))
print(person1.increase_age(31))

person2 = Person("Charles", 15)
print(person2.have_birthday())
print(person2.__age)