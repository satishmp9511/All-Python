# 1. Single Inheritance
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):  # Child inherits Parent (Car)
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car1.start()
print("Car Color:", car1.color)


# 2. Multi-level Inheritance & super() Method
class Vehicle:
    def __init__(self, type_name):
        self.type_name = type_name

class ElectricCar(Vehicle):
    def __init__(self, name, type_name):
        super().__init__(type_name)  # Parent class ka constructor call
        self.name = name

ev1 = ElectricCar("Nexon EV", "Electric Vehicle")
print(f"Vehicle: {ev1.name}, Type: {ev1.type_name}")


# 3. Multiple Inheritance
class ClassA:
    varA = "Welcome to Class A"

class ClassB:
    varB = "Welcome to Class B"

class ClassC(ClassA, ClassB):  # Inherits both A and B
    varC = "Welcome to Class C"

obj_c = ClassC()
print(obj_c.varA)
print(obj_c.varB)
print(obj_c.varC)
