
print("----------------------------------------------")
print("wellcome a contact list")
print("----------------------------------------------")
print("1.add new contact\n2.search contact\n3.view all contacts\n4.exit")
print("----------------------------------------------")

phone={}

try:
    with open (r"number.txt",mode="r") as f:
        for i in f:
            if i.strip():
                p=i.split("-")
                name=p[0].strip()
                number=p[0].strip()
                phone[name]=number
    while True:
        choose=input('enter to:')
        print("----------------------------------------------")
        if choose=='1':
            print("----------------------------------------------")
            name=input("enter a name you save:")
            number=int(input("enter number you save your contact list:"))
            phone[name]=number
        elif choose=='2':
            print("----------------------------------------------")
            search=input("enter a name you see in contact list:")
            if search in phone :
                print(f"name:{search}\tnumber:{phone[search]}")
            else:
                print("contact lot found in list...")
            print("----------------------------------------------")
        elif choose=='3':
            print("----------------------------------------------")
            with open (r"number.txt",mode="r") as file:
                read=file.read()
                print(read)
        elif choose=='4':
            print("----------------------------------------------")
            print("good by..")
            print("----------------------------------------------")
            break
        else:
            print("you typed a wrong keyword.")
    number_list=str(phone)
    with open (r"number.txt",mode="a") as file:
        file.write(f'{number_list},\n')
except ValueError:
    print("you enter only number ...")
