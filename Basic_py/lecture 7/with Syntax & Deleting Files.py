# File Name: lecture7.py

import os

# 1. with Syntax: Automatically file ko close kar deta hai (close() likhne ki zarurat nahi hoti)
with open("sample.txt", "r") as f:
    data = f.read()
    print("Content using with statement:\n", data)


# with statement for writing
with open("sample.txt", "a") as f:
    f.write("Adding one more line using 'with'.\n")


# 2. File Delete karna (os module ka remove function)
# Pehle test karne ke liye ek dummy file banate hain
with open("demo.txt", "w") as f:
    f.write("This file will be deleted.")

# os.remove() se file delete hoti hai
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("\n'demo.txt' successfully deleted!")
