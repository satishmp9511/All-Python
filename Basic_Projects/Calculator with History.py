def save_file(a):
    try:
        with open("c.txt", "a") as f:
            f.write(f"{a}\n")
            return "calculation ki history saved successfully!"
    except FileNotFoundError:
        return "File not found! Please check the file path."
def input_():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1,num2
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def f(num1,num2,result,k):
    print(f"The result of {num1} and {num2} is: {result}")
    print(save_file(f"{num1} {k} {num2} = {result}"))

def addittion():
    try:
        a=input_()
        num1, num2 = a
        result = num1 + num2
        f(num1,num2,result,"+")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def subtraction():
    try:
        a=input_()
        num1, num2 = a
        result = num1 - num2
        f(num1,num2,result,"-")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def multiplication():
    try:
        a=input_()
        num1, num2 = a
        result = num1 * num2
        f(num1,num2,result,"*")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def division():
    try:
        a=input_()
        num1, num2 = a
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        f(num1,num2,result,"/")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

while True:
    print("----------------------------------------------------------")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    print("----------------------------------------------------------")
    choice = input("Choose an option: ")
    print("----------------------------------------------------------")
    if choice == "1":
        addittion()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
