import os

try:
    print("---------------------------------")
    file=r"C:\Users\INOOOOOOO\Desktop\ser"
    word=input("enter the word to search:")
    files=os.listdir(file)
    print("---------------------------------")
    for i in files:
        if i.endswith(".txt"):
            txt=file+"\\"+i
            with open(txt,"r") as f:
                read=f.read()
                if word.lower() in read.lower():
                    id=word.find(word)
                    print(f"index number is {id}")
                    print(f"found the word in file path:\n=={txt }")
                    break
        else:
            print("not found in your file...")
except FileNotFoundError as gg:
    print(gg)
print("---------------------------------")
print("Note,\nyou type a word or number he chek a 1st file \nand found that give you ...")
print("---------------------------------")
