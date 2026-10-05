# File Name: lecture2.py

# 1. Basic Voting Check
age = 21

if (age >= 18):
    print("Can vote & drive")
else:
    print("Cannot vote")

# 2. Student Grade Example
marks = int(input("Enter student marks: "))

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)
