# File Name: lecture3.py

# 1. Lists define karna (different data types)
marks = [87, 64, 33, 95, 76]
student = ["Karan", 85, "Delhi"]

print(student[0])     # Output: Karan
print(len(student))    # Output: 3

# 2. List Elements Modify karna (Lists are Mutable)
student[0] = "Arjun"
print(student)        # Output: ['Arjun', 85, 'Delhi']

# 3. List Slicing
marks = [87, 64, 33, 95, 76]
print(marks[1:4])     # Output: [64, 33, 95]
print(marks[:4])      # Output: [87, 64, 33, 95]
print(marks[1:])      # Output: [64, 33, 95, 76]
print(marks[-3:-1])   # Output: [33, 95]

# File Name: lecture3.py

list = [2, 1, 3]

# 1. append: End mein element add karta hai
list.append(4)
print("After append:", list)  # Output: [2, 1, 3, 4]

# 2. sort: Ascending order mein sort karta hai
list.sort()
print("After sort:", list)    # Output: [1, 2, 3, 4]

# 3. sort(reverse=True): Descending order mein sort karta hai
list.sort(reverse=True)
print("After sort reverse:", list)  # Output: [4, 3, 2, 1]

# 4. reverse: List ko ulta kar deta hai
list.reverse()
print("After reverse:", list)  # Output: [1, 2, 3, 4]

# 5. insert: Specific index par element insert karta hai
list.insert(1, 5)
print("After insert at index 1:", list)  # Output: [1, 5, 2, 3, 4]

# 6. remove: Pehli occurrence wale element ko remove karta hai
list2 = [2, 1, 3, 1]
list2.remove(1)
print("After remove(1):", list2)  # Output: [2, 3, 1]

# 7. pop: Specific index ka element hata deta hai
list2.pop(0)
print("After pop(0):", list2)  # Output: [3, 1]
