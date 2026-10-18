# File Name: lecture7.py

# Question 1: Create a new file "practice.txt" and add the following data:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.\n")


# Question 2: WAP that replaces all occurrences of "Java" with "Python" in "practice.txt".
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_data)

print("--- Updated practice.txt Content ---")
print(new_data)


# Question 3: Search if the word "learning" exists in the file or not.
def check_for_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()
        if word in data:
            print(f"Found '{word}' in the file.")
        else:
            print(f"'{word}' not found in the file.")

check_for_word("learning")


# Question 4: WAP to find in which line of the file does the word "learning" occur first.
def check_for_line(word):
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"'{word}' found in line number:", line_no)
                return
            line_no += 1
    print("-1")

check_for_line("learning")


# Question 5: From a file containing numbers separated by comma, count how many even numbers are there.
# Pehle 'numbers.txt' file create karte hain
with open("numbers.txt", "w") as f:
    f.write("1, 2, 45, 84, 92, 100, 33, 77")

count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")  # Comma se numbers ki list banayenge
    for val in nums:
        if int(val) % 2 == 0:
            count += 1

print("Total Even Numbers in file:", count)
