# File Name: lecture8.py

class Student:
    # Class Attribute
    college_name = "ABC College"

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method 1: Welcome message print karna
    def welcome(self):
        print("Welcome student,", self.name)

    # Method 2: Student ke marks return karna
    def get_marks(self):
        return self.marks


# Object creation
s1 = Student("Karan", 97)

# Methods call karna
s1.welcome()
print("Marks:", s1.get_marks())
