import os

file=r"C:\Users\INOOOOOOO\OneDrive\Pictures\whatsapp"
w=0
files=os.listdir(file)
for i in files:
    if i.endswith(".png")or i.endswith(".jpg")or i.endswith(".jpeg")or i.endswith(".webp"):
        old=file+'\\'+i
        p=(f"\\{w}")
        new=(f"{file+p+".png"}")
        os.rename(old,new)
        w+=1
