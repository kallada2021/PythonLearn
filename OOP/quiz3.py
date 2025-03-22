class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        self.food = food
        return food
    
    def sleep(self, state):
        self.state = state
        return state

class Lion(Animal):
    def roar(self,state):
        return state
        



animal = Animal("Mufasa", 7)
# eating = animal.eat("rabbit")
# print(f"{animal.name} is {animal.age} and ate a {eating} ")
# sleepstate = animal.sleep("sleeping")
# print(f"{animal.name} is now {sleepstate}")

lion = Lion("Scar",7)
print(f"{lion.name} is {lion.roar("roaring")}")