# File Name: lecture6.py

# 1. Basic Function Definition & Call
def calc_sum(a, b):
    sum = a + b
    return sum

output = calc_sum(5, 10)
print("Sum is:", output)  # Output: Sum is: 15


# 2. Function without arguments and without return
def print_hello():
    print("Hello, Welcome to Python Functions!")

print_hello()


# 3. Average of 3 numbers using Function
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

print("Average:", calc_avg(10, 20, 30))  # Output: Average: 20.0

# File Name: lecture6.py

# 1. Default Parameters (Default value hamesha end mein aati hai)
def cal_prod(a=1, b=1):
    print("Product:", a * b)
    return a * b

cal_prod()        # a=1, b=1 -> Output: 1
cal_prod(4)       # a=4, b=1 -> Output: 4
cal_prod(4, 5)    # a=4, b=5 -> Output: 20


# Default parameter positional rules:
def greet(name, msg="Hello"):
    print(msg, name)

greet("Rahul")             # Output: Hello Rahul
greet("Rahul", "Good Morning") # Output: Good Morning Rahul


# 2. Built-in Functions vs User-defined Functions
# Built-in: Python mein pehle se hote hain (e.g. print(), len(), type(), range())
print("Length of list:", len([1, 2, 3, 4]))

# User-defined: Jo hum khud banate hain (e.g. cal_prod, greet)
