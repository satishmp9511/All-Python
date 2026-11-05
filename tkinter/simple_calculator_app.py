import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("sum")
root.geometry("400x300")
root["bg"]="#69a0ac"

def press(char):
    curent=root.focus_get()
    if curent in [input1,input2]:
        curent.insert(tk.END,char)
    if char in ["+","-","*","/"]:
        input3.insert(tk.END,char)

def clear_all():
    input1.delete(0,tk.END)
    input2.delete(0,tk.END)
    input3.delete(0,tk.END)
    to.config(text="total:")

def hi():
    try:
        text1=input1.get()
        text2=input2.get()
        text3=input3.get()

        if text1 =="" or text2 =="" or text3=="":
            messagebox.showwarning("Waring","enter number and operator!")
            return
        
        texthi=float(text1)
        texthii=float(text2)

        if text3=="+":
            sum=texthi + texthii
        elif text3=="-":
            sum=texthi - texthii
        elif text3=="*":
            sum=texthi * texthii
        elif text3=="/":
            if texthii ==0:
                messagebox.showerror("Error","Invalid number not 0")
            sum=texthi / texthii
        to.config(text=f"total={sum}")

    except ValueError:
        messagebox.showerror("Error","Invalid number enterd!")
    
input1=tk.Entry(root,font=("Arial",20),fg="#2b2ee3")
input1.grid(row=0, padx=20, pady=20)

input2=tk.Entry(root,font=("Arial",20),fg="#3a57e9")
input2.grid(row=0,column=2, padx=20, pady=20)

input3=tk.Entry(root,font=("Arial",20),fg="#e51212")
input3.grid(row=0,column=1, padx=20, pady=20)

to=tk.Label(root,text="total=0",fg="#3d0fe0",bg="#a3a3a3",font=("Areal",16))
to.grid(row=6,column=1)
   
btn1=tk.Button(root,text="1",bg="red",font=("Arial",16),command=lambda: press("1"))
btn1.grid(row=2,column=0 ,padx=20, pady=20)

btn2=tk.Button(root,text="2",bg="red",font=("Arial",16),command=lambda: press("2"))
btn2.grid(row=2,column=1 ,padx=20, pady=20)

btn3=tk.Button(root,text="3",bg="red",font=("Arial",16),command=lambda: press("3"))
btn3.grid(row=2,column=2 ,padx=20, pady=20)

btn4=tk.Button(root,text="4",bg="red",font=("Arial",16),command=lambda: press("4"))
btn4.grid(row=3,column=0 ,padx=20, pady=20)

btn5=tk.Button(root,text="5",bg="red",font=("Arial",16),command=lambda: press("5"))
btn5.grid(row=3,column=1 ,padx=20, pady=20)

btn6=tk.Button(root,text="6",bg="red",font=("Arial",16),command=lambda: press("6"))
btn6.grid(row=3,column=2 ,padx=20, pady=20)

btn7=tk.Button(root,text="7",bg="red",font=("Arial",16),command=lambda: press("7"))
btn7.grid(row=4,column=0 ,padx=20, pady=20)

btn8=tk.Button(root,text="8",bg="red",font=("Arial",16),command=lambda: press("8"))
btn8.grid(row=4,column=1 ,padx=20, pady=20)

btn9=tk.Button(root,text="9",bg="red",font=("Arial",16),command=lambda: press("9"))
btn9.grid(row=4,column=2 ,padx=20, pady=20)

btnm=tk.Button(root,text="<",bg="red",font=("Arial",16),command=clear_all)
btnm.grid(row=5,column=0 ,padx=20, pady=20)

btn0=tk.Button(root,text="0",bg="red",font=("Arial",16),command=lambda: press("0"))
btn0.grid(row=5,column=1 ,padx=20, pady=20)

btn_=tk.Button(root,text="=",bg="red",font=("Arial",16),command=hi)
btn_.grid(row=5,column=2,padx=20, pady=20)

btn1=tk.Button(root,text="+",bg="red",font=("Arial",16),command=lambda: press("+"))
btn1.grid(row=2,column=4 ,padx=20, pady=20)

btn2=tk.Button(root,text="-",bg="red",font=("Arial",16),command=lambda: press("-"))
btn2.grid(row=3,column=4 ,padx=20, pady=20)

btn3=tk.Button(root,text="*",bg="red",font=("Arial",16),command=lambda: press("*"))
btn3.grid(row=4,column=4 ,padx=20, pady=20)

btn4=tk.Button(root,text="/",bg="red",font=("Arial",16),command=lambda: press("/"))
btn4.grid(row=5,column=4,padx=20, pady=20)

root.mainloop()
