
import tkinter as tk
import time

root=tk.Tk()
root.title("hi")
root.geometry("500x600")
root["bg"]="#a6e8eb"

l=tk.Label(root,text="00:00:00",fg="#3BEF3B",bg="black",font=("Areal",16,"bold"))
l.grid(row=0,column=0)

def c():
    time1=time.strftime("%H:%M:%S %p")
    l.config(text=time1)
    l.after(1000,c)

c()

lp=tk.Label(root,text="00:00:00",fg="#DEAE35",bg="black",font=("Areal",16,"bold"))
lp.grid(row=1,column=0)

re=True
co=0

def g():
    global co,re
    if re==True:
        co+=1
        lp.config(text=co)
        lp.after(1000,g)
g()

def pp():
    global re,co
    re=False

def ss():
    global re,co
    if re==True:
        return
    re=True
    co=0
    lp.config(text=co)
    g()
    
def rr():
    global re,co
    co=0
    lp.config(text=co)
    re=False

b1=tk.Button(root,text="p",bg="red",font=("Areal",15),command=pp)
b1.grid(row=4,column=0)

b2=tk.Button(root,text="s",bg="red",font=("Areal",15),command=ss)
b2.grid(row=4,column=2)

b3=tk.Button(root,text="r",bg="red",font=("Areal",15),command=rr)
b3.grid(row=4,column=3)

root.mainloop()


