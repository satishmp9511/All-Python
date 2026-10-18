# File Name: lecture7.py

# Pehle test karne ke liye 'sample.txt' naam ki file create karein 
# usme kuch text likhein: "Hello, Python Lecture 7 File I/O!"

# 1. File open karna (default mode 'r' - read hota hai)
f = open("sample.txt", "r")

# 2. File ka saara data read karna
data = f.read()
print("File Content:\n", data)
print("Type of data:", type(data))

# 3. File close karna (Memory free karne ke liye)
f.close()


# Extra: Character-wise limit & Line-by-Line Read
f = open("sample.txt", "r")

# Sirf pehle 5 characters read karna
line1 = f.read(5)
print("\nFirst 5 characters:", line1)

# readline(): Ek poori line read karta hai
line2 = f.readline()
print("Rest of the line:", line2)

f.close()
