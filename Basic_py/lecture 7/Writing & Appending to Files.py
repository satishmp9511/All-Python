# File Name: lecture7.py

# 1. 'w' (Write Mode): Purana data overwrite (mita) kar naya content likhta hai
# Agar file exist nahi karti, toh nayi file bana deta hai
f = open("sample.txt", "w")
f.write("I am learning Python File I/O from Apna College.\n")
f.close()


# 2. 'a' (Append Mode): Purane data ke aage naya content add karta hai
f = open("sample.txt", "a")
f.write("This line is appended at the end of the file.\n")
f.close()


# Updated content check karne ke liye read karke dekhte hain
f = open("sample.txt", "r")
print("Updated File Content:\n", f.read())
f.close()
