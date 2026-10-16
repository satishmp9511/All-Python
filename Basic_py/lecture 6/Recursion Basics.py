# File Name: lecture6.py

# 1. Basic Recursion: n se 1 tak numbers print karna
def show(n):
    if (n == 0):  # Base Case: Jahan recursion rukti hai
        return
    print(n)
    show(n - 1)   # Recursive Call

show(5)  # Output: 5, 4, 3, 2, 1


# 2. Recursion se Factorial calculate karna
# Logic: n! = n * (n - 1)!
def fact(n):
    if (n == 0 or n == 1):  # Base Case
        return 1
    return n * fact(n - 1)

print("Factorial of 5 using Recursion:", fact(5))  # Output: 120
