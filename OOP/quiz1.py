class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return "woof"

animal = Animal("Buddy")
print(f"{animal.name} produces {animal.speak()}")
dog = Dog("woof")
print(f"{animal.name} says {dog.speak()}")