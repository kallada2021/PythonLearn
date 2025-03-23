# Base Class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make of the car is {self.make} and the model is {self.model}")   

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        self.num_doors = num_doors
        super().__init__(make, model)
    
    def display_info(self):
        print(f"Make of the car is {self.make} and the model is {self.model} and has {self.num_doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, make, model, type_of_handlebars):
        self.type_of_handlebars = type_of_handlebars
        super().__init__(make, model)

    def display_info(self):
        print(f"Make of the motorcycle is {self.make} and the model is {self.model} and has {self.type_of_handlebars} handlebars")

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity
    
    def display_info(self):
        print(f"Make of the truck is {self.make} and the model is {self.model} and its payload capacity is  {self.payload_capacity} lbs")
        


def main():
    vehicles = [
        Car("Toyota", "Corolla", 4),
        Motorcycle("Yamaha", "MT-07", "Sport"),
        Truck("Ford", "F-150", 1000)
    ]

    for vehicle in vehicles:
        vehicle.display_info()

main()
# vehicle = Vehicle("Fiat", 1956)
# vehicle.display_info()
# car = Car("Tesla", "Model Y", 4)
# car.display_info()
# motorcycle = Motorcycle("Harley Davidson", 2025, "Beach Bar")
# motorcycle.display_info()
# truck = Truck("Ford", "F150", 5000)
# truck.display_info()