import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>?/"


def random_password():
    try:
        length = int(input("Enter the length of the password: "))
        password = ""
        for i in range(1, length + 1):
            p=random.choice(characters)
            password += ''.join(p)
        return password
    except ValueError:
        return "Invalid input! Please enter a valid number."

def save_pass(a):
    try:
        with open(r"C:\Users\INOOOOOOO\OneDrive\Desktop\random_file\for_py_project\Secure Password Generator.txt","a") as f:
            f.write(f"{a}\n")
            return "Password saved successfully!"
    except FileNotFoundError:
        return "File not found! Please check the file path."

while True:
    print("----------------------------------------------------------")
    print("1.Generate password\n2.Exit")
    print("----------------------------------------------------------")
    choice = input("Choose an option: ")
    print("----------------------------------------------------------")
    if choice == "1":
        password_word=random_password()
        print(f"Generated password: {password_word}")
        save_choice = input("Do you want to save the password? (y/n): ")
        if save_choice.lower() == "y":
            print(save_pass(password_word))
        else:
            print("Password not saved.OK")
    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break 
    else:
        print("Invalid choice! Please try again.")

