# 1. Static Methods (@staticmethod)
class Student:
    def __init__(self, name):
        self.name = name

    # Static method - self parameter ki zarurat nahi hoti
    @staticmethod
    def hello():
        print("Hello, Welcome to OOPs concepts!")

s1 = Student("Rahul")
s1.hello()


# 2. Abstraction Example (Car Start Mechanism)
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

car1 = Car()
car1.start()  # User ko andar ka clutch/acc details nahi dekhna padta, bas start() call karta hai


# 3. Encapsulation Example (Bank Account Practice)
# Class ke andar Data + Methods ko ek sath wrap karna Encapsulation hai
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_no = acc_no

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


# Account object testing
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
