import os
file=r"C:\Users\INOOOOOOO\Desktop\fake"
img=file+"\\"+"img"
txt=file+"\\"+"txt"
pdf=file+"\\"+"pdf"
other=file+"\\"+"other"
files=os.listdir(file)
for i in files:
    if i.endswith(".png") or i.endswith(".jpg"):
        if not os.path.exists(img):
            os.makedirs(img)
        old_img=file+"\\"+i
        new_img=img+"\\"+i
        
        os.rename(old_img,new_img)
    elif i.endswith(".txt"):
        if not os.path.exists(txt):
            os.makedirs(txt)
        old_txt=file+"\\"+i
        new_txt=txt+"\\"+i
        os.rename(old_txt,new_txt)
    elif i.endswith(".pdf"):
        if not os.path.exists(pdf):
            os.makedirs(pdf)
        old_pdf=file+"\\"+i
        new_pdf=pdf+"\\"+i
        os.rename(old_pdf,new_pdf)
    else:
        if i in ["img","txt","pdf","other","qw.py"]:
            continue
        if not os.path.exists(other):
            os.makedirs(other)
        old_other=file+"\\"+i
        new_other=other+"\\"+i
        os.rename(old_other,new_other)

print("ok...")


