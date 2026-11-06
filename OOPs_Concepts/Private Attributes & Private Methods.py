class Account:
    def __init__(self, acc_no, acc_pass):
        self.account_no = acc_no
        self.__acc_pass = acc_pass  # Private attribute

    def reset_pass(self):
        print("Your password is:", self.__acc_pass)  # Class ke andar access ho sakta hai


acc1 = Account("12345", "abcde")

print("Account No:", acc1.account_no)
# print(acc1.__acc_pass)  # Error dega: Private attribute ko bahar access nahi kar sakte!

acc1.reset_pass()  # Class method ke zariye private data access hota hai


# Private Method Example
class Person:
    __name = "anonymous"  # Private attribute

    def __hello(self):    # Private method
        print("Hello Person!")

    def welcome(self):
        self.__hello()    # Internal call allowed hai

p1 = Person()
p1.welcome()
# p1.__hello()            # Error dega: Direct call disallowed
