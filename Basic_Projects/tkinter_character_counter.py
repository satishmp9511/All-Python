import tkinter as tk

root=tk.Tk()
root.geometry('500x600')
root.title("letter countr..")

l=tk.Label(root,text="Type your paragrapy below:",fg="#0ac8ee",font=("Areal",16))
l.grid(row=0,column=0)

input=tk.Text(root,bg="#dcde69",fg="#2b16ee",font=("Areal",16),width=20,height=2)
input.grid(row=1,column=0)

llw=tk.Label(root,text=f"total word=0",fg="#d27d27",font=("Areal",16))
llw.grid(row=3,column=0)
lll=tk.Label(root,text=f"total letter=0",fg="#c02dca",font=("Areal",16))
lll.grid(row=4,column=0)

def ck():
    inp=input.get("1.0","end-1c")
    ll=len(inp)
    lw=inp.split()
    lww=len(lw)
    llw.config(text=f"total word={lww}")
    lll.config(text=f"total letter={ll}")

b=tk.Button(root,text="chek",bg="#79dc3b",font=("Areal",16),command=ck)
b.grid(row=1,column=1)

root.mainloop()




