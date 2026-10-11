# File Name: lecture4.py

# Question 1: Store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}
print("Word Dictionary:", dictionary)


# Question 2: You are given a list of subjects for students. Assume one classroom 
# is required for 1 subject. How many classrooms are needed by all students?
# subjects = "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("Classrooms needed (Unique Subjects):", len(subjects))


# Question 3: WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}
x = int(input("Enter phy marks: "))
marks.update({"phy": x})

x = int(input("Enter chem marks: "))
marks.update({"chem": x})

x = int(input("Enter math marks: "))
marks.update({"math": x})

print("Student Marks:", marks)


# Question 4: Figure out a way to store 9 & 9.0 as separate values in the set.
# Method 1: String ke roop mein store karke
values1 = {9, "9.0"}
print("Separated using string:", values1)

# Method 2: Built-in data types (Tuple) ka use karke
values2 = {("float", 9.0), ("int", 9)}
print("Separated using tuple:", values2)
