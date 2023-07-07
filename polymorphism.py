class Vehicle:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("moving the vehicle on the road")

class Bike(Vehicle):
    def __init__(self,name,speed):
       super().__init__(name,speed)

    def move(self):
        print("Bike..")

bike = Bike()
bike.move()