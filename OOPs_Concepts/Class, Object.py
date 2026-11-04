# File Name: lecture8.py

# 1. Class definition (Blueprint)
class Student:
    # Class Attribute (sab objects ke liye common)
    college_name = "ABC College"

    # Constructor (__init__ method)
    def __init__(self, name, marks):
        # Instance Attributes (har object ke apne unique attributes)
        self.name = name
        self.marks = marks
        print("Adding new student in database...")


# 2. Objects create karna (Instances)
s1 = Student("Karan", 97)
print("Student 1 Name:", s1.name)
print("Student 1 Marks:", s1.marks)
print("College:", s1.college_name)

print("---")

s2 = Student("Arjun", 88)
print("Student 2 Name:", s2.name)
print("Student 2 Marks:", s2.marks)
print("College:", s2.college_name)
