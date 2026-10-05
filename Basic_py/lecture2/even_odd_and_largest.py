# File Name: lecture2.py

# Question 1: WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("EVEN")
else:
    print("ODD")


# Question 2: WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a >= c):
    print("First number is largest:", a)
elif (b >= c):
    print("Second number is largest:", b)
else:
    print("Third number is largest:", c)


# Question 3: WAP to check if a number is a multiple of 7 or not.
x = int(input("Enter number: "))

if (x % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
