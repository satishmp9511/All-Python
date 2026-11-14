import time

def countdown(m):
    print("----------------------------------------------------------")
    for i in range(m,0,-1):
        time.sleep(1)
        print(i)
    print("Countdown complete!")
    print("----------------------------------------------------------")


while True:
    try:
        print("----------------------------------------------------------")
        print("1.enter countdown in sec\n2.enter countdown in min\n3.exit\n(0 number not printed)")
        print("----------------------------------------------------------")
        choose_1=int(input("choose: "))
        print("----------------------------------------------------------")
        if choose_1 == 1:
            sec=int(input("enter seconds: "))
            countdown(sec)
        elif choose_1 == 2:
            min=int(input("enter minutes: "))
            countdown(min*60)
        elif choose_1 == 3:
            break
        else:
            print("----------------------------------------------------------")
            print("Invalid choice!")
    except ValueError:
        print("----------------------------------------------------------")
        print("Countdown interrupted!")
