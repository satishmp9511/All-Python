import os
file=r"C:\Users\INOOOOOOO\Desktop\ser\newtdhhd.txt"
E_file=r"C:\Users\INOOOOOOO\Desktop\ser\Ero.txt"
for i in file:
    with open(file,"r") as r ,open(E_file,"w") as f:
        for line in r:
            if "err:" in line:
                f.write(line)
print("ok...")
