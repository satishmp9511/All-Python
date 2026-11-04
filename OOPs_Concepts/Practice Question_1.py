# Question: Create Student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks ek list hogi, e.g., [98, 92, 95]

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:", sum / len(self.marks))


# Object creation with 3 subjects marks
s1 = Student("Tony Stark", [99, 98, 95])
s1.get_avg()

s1.name = "Iron Man"  # Attribute modify karna
s1.get_avg()
