# File Name: lecture5.py

# 1. User se number lekar uski multiplication table (pahada) print karna
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


# 2. List ke saare elements ko sequence mein print karna
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# 3. List mein koi number search karna (Linear Search using while loop)
x = 36
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at index", i)
    i += 1
