import os

file=r"C:\Users\INOOOOOOO\Desktop\ser"
files=os.listdir(file)
for i in files:
    if not "." in files:
        txt=file+"\\"+i
        txtt=file+"\\"+i+".txt"
        os.rename(txt,txtt)
