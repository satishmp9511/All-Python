import os
import datetime
file=r"C:\Users\INOOOOOOO\Desktop\ser"
b_file=r"C:\Users\INOOOOOOO\Desktop\ser\backup"
today_t=datetime.datetime.now()
files=os.listdir(file)
for i in files:
    f=file+"\\"+i
    new=b_file+"\\"+i
    i=os.path.getatime(f)
    file_d=datetime.datetime.fromtimestamp(i)
    if file_d < today_t:
        if not os.path.exists(b_file):
                  os.makedirs(b_file)
        os.rename(f,new)
    else:
        if i in ['backup',"qw.py","ser"]:
            continue
print("ok...")

