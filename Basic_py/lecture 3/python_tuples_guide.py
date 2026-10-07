# File Name: lecture3.py

# 1. Tuples define karna (Immutable - Values change nahi ho sakti)
tup = (87, 64, 33, 95, 76)
print(type(tup))      # Output: <class 'tuple'>
print(tup[0])         # Output: 87
print(tup[1:4])       # Slicing: (64, 33, 95)

# Single element tuple likhne ka tarika (Comma zaroori hai)
tup_single = (1,)     # Correct tuple
# tup_wrong = (1)     # Yeh integer ban jayega, tuple nahi!

# 2. Tuple Methods
tup2 = (1, 2, 3, 4, 2, 2)

# index: Element ka pehla occurrence index batata hai
print("Index of 3:", tup2.index(3))    # Output: 2

# count: Element kitni baar aaya hai wo count karta hai
print("Count of 2:", tup2.count(2))    # Output: 3
