# File Name: lecture6.py

# Question 1: WAP to print the length of a list. (list is the parameter)
cities = ["Delhi", "Gurgaon", "Noida", "Mumbai", "Chennai"]

def print_len(list_arg):
    return len(list_arg)

print("Length of cities list:", print_len(cities))


# Question 2: WAP to print the elements of a list in a single line. (list is the parameter)
def print_list(list_arg):
    for item in list_arg:
        print(item, end=" ")
    print()  # new line ke liye

print_list(cities)


# Question 3: WAP to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5:", cal_fact(5))


# Question 4: WAP to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83  # Assuming 1 USD = 83 INR
    print(usd_val, "USD =", inr_val, "INR")

converter(100)
