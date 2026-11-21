import tkinter as tk
from time import strftime

print("--wellcome to personal expense--")
print("1.add new expense")
print("2.view all expense")
print('3.exit')

try:
    
    while True:
        time = strftime("%H:%M:%S \ndate:%D")
        choose=input("choose an option:")
        if choose=='1':
            with open (r"o.txt",mode="a") as file:
                item=input("item name:")
                amount=input("enter amount:")
                file.write(f"item name:{item}\namount:{amount} time:{time}\n")
        
        elif choose=='2':
            with open (r"o.txt",mode="r") as file:
                read=file.read()
            print(read)

        elif choose=='3':
            print("good by")
            break

        else:
            print("you typed a wrong keyword.")

except FileNotFoundError:
    print("youer file not found")


print("-----------------------------------------")
