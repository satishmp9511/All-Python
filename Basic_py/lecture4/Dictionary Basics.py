# File Name: lecture4.py

# 1. Dictionary define karna (Key-Value pairs, Unordered, Mutable)
info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "coding",
    "age": 35,
    "is_adult": True,
    "marks": 94.4
}

print(info)
print(info["name"])      # Output: apnacollege
print(info["age"])       # Output: 35

# Dictionary modify karna
info["name"] = "Shradha" # Key "name" ki value update kar di
info["surname"] = "Khapra" # Nayi key-value pair add kar di
print(info)

# 2. Nested Dictionary (Dictionary ke andar Dictionary)
student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(student["subjects"])         # Output: {'phy': 97, 'chem': 98, 'math': 95}
print(student["subjects"]["chem"]) # Output: 98

# File Name: lecture4.py

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

# 1. keys(): Saari outer keys return karta hai
print("Keys:", list(student.keys()))

# 2. values(): Saari values return karta hai
print("Values:", list(student.values()))

# 3. items(): Saare (key, value) pairs ko tuples ke roop mein return karta hai
print("Items:", list(student.items()))

# 4. get(): Key ki value nikalne ke liye (agar key na mile toh Error nahi deta, None return karta hai)
print("Get name:", student.get("name")) 

# 5. update(): Nayi key-value pairs add/update karne ke liye
new_data = {"city": "Delhi", "age": 21}
student.update(new_data)
print("Updated Student:", student)
