class Car:
    def __init__(self,make, model,year,color, Wheels):
        self.Wheels = Wheels
        self.make = make
        self.model = model
        self.year = year
        self.color= color
        self.engine_on = False

    def wheels(self):
        print(f"{self.make} car is a  {self.Wheels} wheel drive.")
    
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print("Engine is turned on!")
        else:
            print(f"Engine is already running")
    
    def accelarate(self, increement):
        self.engine_on = True
        self.speed = 50
        if self.engine_on:
            self.speed = self.speed + increement
            print(f"{self.make} car is accelarating at {self.speed} mph.")
        else:
            print(f"Start the {self.make} engine first.")
    
    def brake(self, decreement):
        self.engine_on = True
        self.speed = 50
        self.decreement = decreement
        if self.speed <= 0:
            print(f"{self.make} car is not moving")
        else:
            self.speed = self.speed - decreement
            print(f"{self.make} is now moving at {self.speed} mph.")


car = Car("BMW","xdrive40i", 2025, "Wintergreen",4)
car.wheels()
print(f"{car.make} is {car.model} from {car.year}. Its color is {car.color} and is a {car.Wheels} wheel drive.")
car.start_engine()
car.accelarate(5)
car.brake(10)