# File Name: lecture5.py

# 1. for loop se List/Tuple traverse karna
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

# 2. range(stop) - 0 se start hakar (stop-1) tak chalta hai
print("\nrange(5):")
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# 3. range(start, stop)
print("\nrange(2, 6):")
for i in range(2, 6):
    print(i)  # Output: 2, 3, 4, 5

# 4. range(start, stop, step)
print("\nrange(1, 10, 2) - Odd Numbers:")
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9
