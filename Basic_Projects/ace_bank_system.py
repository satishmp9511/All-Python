dis={}
try:
    with open("t.txt") as f:
        for i in f:
            o=i.strip()
            ac,pa,ba=o.split("-")
            i_ac=ac.strip()
            i_pa=pa.strip()
            i_ba=ba.strip()
            dis [int(i_ac)]=[i_pa,int(i_ba)]
except FileNotFoundError as q:
    print(q)

# class Bank:
#     def __init__(self,acc,pas,bal):
#         self.acc=acc
#         self.pas=pas
#         self.__bal=bal
#     def d(self,a):
#         self.bal +=a
#         print(f"ammount {a} in your account {self.acc}\ntotal:{self.bal}")
#     def w(self,a):
#         if self.bal > a:
#             self.bal -= a
#             print(f"ammount {a} in your account {self.acc}\ntotal:{self.bal}")
#         else:
#             print("sorry bal ....\nyour bal {self.bal}")
#     def c(self):
#         print(f"account number={self.acc}\ntotal bal={self.bal}")

while True:
    print("-"*35)
    print("1.login\n2.create a account")
    a1=input("enter a number(1-2) : ")
    print("-"*35)
    if a1=="1":
        try:
            a2=int(input("enter youer account number in number: "))
            a3=input("enter your password : ")
            if a2 in dis and a3==dis[a2][0]:
                print("*"*35)
                print("1.d\n2.w")
                a5=input("choice a number(1 or 2) : ")
                print("*"*35)
                if a5=="1":
                    try:
                        aa=int(input("enter ammount : "))
                        dis[a2][1] += aa
                        print(f"ammount {aa} in your account {a2}\ntotal:{dis[a2][1]}")
                    except ValueError as q:
                        print(q)
                elif a5=="2":
                    try:
                        aa=int(input("enter ammount : "))
                        if aa<=dis[a2][1]:
                            dis[a2][1] -= aa
                            print(f"ammount {aa} in your account {a2}\ntotal:{dis[a2][1]}")
                        else:
                            print("min ammount in your account..")
                    except ValueError as q:
                        print(q)
                else:
                    print("worng choice..")
                print("yes")
            else:
                print("password or account number is not corrte..")
        except TypeError as q:
            print(q)
        except ValueError as q:
            print(q)
        except FileNotFoundError as q:
            print(q)
    elif a1=="2":
        try:
            print("welcome to ace bank")
            a2=int(input("enter youer account number in number: "))
            a3=input("enter your password : ")
            dis[a2]=[a3,0]
            print(f"your account add\naccount number={a2}\naccount bal=0\nyour password={a3}")
        except TypeError as q:
            print(q)
        except ValueError as q:
            print(q)
        except FileNotFoundError as q:
            print(q)
        
    else:
        print("good by...")
        break
    try:
        with open("t.txt" , "w") as f1:
            for i in dis:
                f1.write(f"{i}-{dis[i][0]}-{dis[i][1]}\n")
            print("add all in file good by..")
    except FileNotFoundError as q:
        print(q)
