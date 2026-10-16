# File Name: lecture6.py

# Question 1: Write a recursive function to calculate the sum of first n natural numbers.
# Logic: sum(n) = n + sum(n - 1)
def calc_sum(n):
    if (n == 0):  # Base Case
        return 0
    return calc_sum(n - 1) + n

print("Sum of first 5 natural numbers:", calc_sum(5))  # Output: 15


# Question 2: Write a recursive function to print all elements in a list.
# Hint: Use list and index as parameters
def print_list(list_arg, idx=0):
    if (idx == len(list_arg)):  # Base Case: Jab index list ke end tak pahunch jaye
        return
    print(list_arg[idx])
    print_list(list_arg, idx + 1)  # Agle index ke liye recursive call

fruits = ["mango", "apple", "banana", "litchi"]
print("\nPrinting list elements using recursion:")
print_list(fruits)
