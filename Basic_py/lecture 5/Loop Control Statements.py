# File Name: lecture5.py

# 1. break statement: Jab x mil jaye toh loop wahi rok do
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0

while i < len(nums):
    if (nums[i] == x):
        print("FOUND at index", i)
        break  # Loop turant stop ho jayega
    i += 1

print("Loop terminated after break\n")


# 2. continue statement: Specific condition par iteration skip karna
# Example: Only EVEN numbers print karna (ODD numbers ko skip karna)
i = 1
while i <= 10:
    if (i % 2 != 0):
        i += 1
        continue  # Baaki code skip karke wapas while condition par chala jayega
    print(i)
    i += 1
