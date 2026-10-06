# File Name: lecture3.py

# Question 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
movies.append(input("Enter first favorite movie: "))
movies.append(input("Enter second favorite movie: "))
movies.append(input("Enter third favorite movie: "))
print("Favorite Movies:", movies)


# Question 2: WAP to check if a list contains a palindrome of elements.
# (Hint: Use copy() method to copy list and reverse it)
list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
