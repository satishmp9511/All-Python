import tkinter as tkk
from time import strftime
import random
tm = strftime("time:%H:%M:%S\tdate:%D")
print("----------------------------------")
print("wellcome to bank ATM")
print(f'time:{tm}')
print("----------------------------------")
des={}
while True:
    try:
        print("new account=1 and you account=2")
        acco=input("enter account new or old:")
        if acco=='1':
            accou=list(range(1,10000000,1))
            accoun=random.choice(accou)
            print(f"your account number {accoun}")
            pa=int(input("enter your new password:"))
            add=int(input("enter amount you add in account:"))
            with open (r"bank.txt",mode="a") as fff:
                fff.write(f"{accoun},{pa},{add}\n")
            print("your account done.")
            print(f"youer aacount nuber is {accoun},password is {pa}.")
            break
        else:
            acc=int(input("enter a account number:"))
            pas=int(input("enter a password:"))
        print("----------------------------------")
    except ValueError:
        print("you typed a wrong keyword...")
    try:
        while True:
            with open (r"bank.txt",mode="r") as f:
                for i in f:
                    if i.strip():
                        p=i.split(",")
                        account=int(p[0].strip())
                        passwo=int(p[1].strip())
                        bl=int(p[2].strip())
                        des[account]=[passwo,bl]
            if acc in des:
                passw=(des[acc][0])
                if passw==pas:
                    print("----------------------------------")
                    print("1.check balance,\n2.money,\n3.exit.")
                    print("----------------------------------")
                    choose=input("enter number.:")
                    if choose=='1':
                        print(f"your balance:{des[acc][1]}")
                    elif choose=='2':
                        print("----------------------------------")
                        print("1.debit,\n2.credit.")
                        print("----------------------------------")
                        df=input("choose number:")
                        print("----------------------------------")
                        if df=='1':
                            debit=int(input("enter amount debit:"))
                            if debit>des[acc][1]:
                                print("amount<debit....")
                            else:
                                des[acc][1]-=debit
                                print(f"debit amount is {debit}and your total balance is {des[acc][1]}")
                        elif choose=='2':
                            print("----------------------------------")
                            credit=int(input("enter amount tpu credit:"))
                            des[acc][1]+=credit
                            print(f"credit amount is {credit}and your total balance is {des[acc][1]}")
                        else:
                            print("----------------------------------")
                            print("you typed a wrong keyword")
                        with open (r"bank.txt",mode="w") as ff:
                            for account,des in des.items():
                               passwo=des[0]
                               bl=des[1]
                               ff.write(f"{account},{passwo},{bl}\n")
                    elif choose=='3':
                        break  
                    else:
                        print("----------------------------------")
                        print("you typed a wrong keyword")
                else:
                    print("----------------------------------")
                    print("password or account number not found....")
                    break
            else:
                print("----------------------------------")
                print("password or account number not found..")
                break
        print("----------------------------------")
    except ValueError:
        print("you typed a wrong keyword...")
    except FileNotFoundError:
        print("file not found.")
    except IndexError:
        print("amount debit/credit succfully or chek..")

    r=input(" new login enter y/n:")
    if r=='y':
        continue
    else:
        print("----------------------------------")
        print("see you next time..")
        break
print("----------------------------------")
