# File Name: lecture4.py

# 1. Set Basics (Duplicates ignore karta hai)
collection = {1, 2, 2, 2, "hello", "world", 4}
print(collection)        # Duplicates remove ho jayenge
print(type(collection))  # Output: <class 'set'>

# Empty Set banana ( {} se dictionary banti hai, set ke liye set() use hota hai )
empty_set = set()
print(type(empty_set))   # Output: <class 'set'>

# 2. Set Methods
num_set = set()

# add(): Element add karne ke liye
num_set.add(1)
num_set.add(2)
num_set.add(2) # Duplicate ignore hoga
print("After add:", num_set)

# remove(): Element remove karne ke liye
num_set.remove(1)
print("After remove:", num_set)

# 3. Union & Intersection Operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# union(): Dono sets ke all unique elements jodta hai
print("Union:", set1.union(set2))         # Output: {1, 2, 3, 4}

# intersection(): Dono sets ke common elements nikalta hai
print("Intersection:", set1.intersection(set2)) # Output: {2, 3}
