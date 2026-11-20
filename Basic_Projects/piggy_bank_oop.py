import tkinter as tkk
from time import strftime


class account():
    def __init__(self,name,account_number,balance,password=123):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.__password=password

    def debit(self,amount):
        self.balance -= amount
        print("--------------------------------------")
        print(f"app nr {amount} debit kara he .")

    def credit(self,amount):
        self.balance += amount
        print("--------------------------------------")
        print(f"app {amount} dale he apne account me.")

    def chek(self):
        total=self.balance
        print("--------------------------------------")
        print(f"youer total balance {total} he.")

account_1=account("satish",4566541,500)
account_2=account("om",4566542,1000,321)
a3=account("mahendra",4566543,5000,1234)

print("--------------------------------------")
print("wellcome to piggy bank")
print("--------------------------------------")
tm = strftime("%H:%M:%S \ndate:%D")
print(f'name is {account_1.name } \t\t time:{tm}')

print("--------------------------------------")
print("1.check balance\n2.debit\n3.credit\n4.ex")
print("--------------------------------------")

while True:

    cho=input("enter a number to go next page :")

    if cho=='1':
        account_1.chek()
    elif cho=='2':
        debit1=int(input("enter a amount you debit:"))
        account_1.debit(debit1)
    elif cho=='3':
        credit1=int(input("enter a amount you credit:"))
        account_1.credit(credit1)
    elif cho=='4':
        break
    else:
        print("typeing error....")

print("----------------------------------------")
print("good day.")    
