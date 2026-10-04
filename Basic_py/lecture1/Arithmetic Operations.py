# 1. Sum of 2 Numbers
a = 5
b = 10
sum_val = a + b
print("Sum:", sum_val)

# 2. Type Conversion (Python automatically converts int to float)
x = 1
y = 2.0
sum_conversion = x + y
print("Conversion Sum:", sum_conversion)  # Output: 3.0
print(type(sum_conversion))             # Output: <class 'float'>

# 3. Type Casting (Manual conversion from String to Integer)
p = 1
q = "2"
c = int(q)  # String "2" ko Integer 2 mein cast kiya
sum_casting = p + c
print("Casting Sum:", sum_casting)        # Output: 3
