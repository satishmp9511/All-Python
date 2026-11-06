# 1. @classmethod Example
class Person:
    name = "anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name  # Directly updates the class attribute

p1 = Person()
p1.change_name("Rahul Kumar")
print("Updated Class Attribute Name:", Person.name)


# 2. @property Decorator Example
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 97, 99)
print("Student Percentage:", s1.percentage)  # Property ki tarah bina () call hota hai

s1.phy = 88  # Dynamic value update check
print("Updated Percentage:", s1.percentage)


# 3. Polymorphism & Operator Overloading (__add__)
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(f"{self.real}i + {self.img}j")

    # Overloading the '+' operator using dunder method __add__
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

num1 = Complex(1, 3)
num1.show_number()

num2 = Complex(4, 6)
num2.show_number()

num3 = num1 + num2  # Uses overloaded __add__
print("Sum of Complex Numbers:")
num3.show_number()
