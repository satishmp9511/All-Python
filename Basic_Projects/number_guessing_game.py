import random
number=list(range(1,10000000,1))
com = random.choice(number)
#print(com)
man=int(input("enter a number :"))

while man>=0:
    if com == man :
        print(f"yoyo you choice prfet number{man}")
        break  
    else:
        if com < man :
            print("youer number a big")    
        elif com > man :
            print("youer number a small")
        man=int(input("enter a number:"))
        if man==com:
            print(f"yoyo you choice prfet number{man}")
        elif man>com:
            print("youer number a big")
        elif man<com:
            print("youer number a small")
        else:
            print("good")
        if man==com:
            break
