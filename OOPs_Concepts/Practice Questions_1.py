# Question 1: Define a Circle class to create a circle with radius r using constructor.
# Define Area() and Perimeter() methods for the class.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * (self.radius ** 2)

    def perimeter(self):
        return 2 * (22 / 7) * self.radius

c1 = Circle(21)
print("Circle Area:", c1.area())
print("Circle Perimeter:", c1.perimeter())


# Question 2: Define an Employee class with attributes role, department, and salary.
# Create an Engineer class that inherits from Employee and adds name and age.
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role}, Dept: {self.dept}, Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Software Engineer", "IT", 75000)

eng1 = Engineer("Aman", 24)
print("\nEngineer Details:")
print("Name:", eng1.name)
print("Age:", eng1.age)
eng1.show_details()


# Question 3: Create an Order class which stores item & price.
# Use __gt__() dunder function to check if order1 > order2 based on price.
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # Overloading '>' operator using __gt__
    def __gt__(self, ord2):
        return self.price > ord2.price

order1 = Order("Chips", 20)
order2 = Order("Ice Cream", 50)

print("\nIs order1 price > order2 price?", order1 > order2)  # Output: False
