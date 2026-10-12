# File Name: lecture5.py

# Question 1: WAP to find the sum of first n natural numbers (using while loop or for loop).
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum of first", n, "natural numbers:", sum)


# Question 2: WAP to find the factorial of first n numbers (using for loop).
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact)
