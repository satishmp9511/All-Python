import tkinter as tk
from tkinter import messagebox
try:
    root=tk.Tk()
    root.geometry("600x500")
    root.title("wellcome")
    l=tk.Label(root,text="enter a year:" ,fg="#594ae1", font=("Areal",16))
    l.grid(row=0,column=1)

    input=tk.Entry(root,text="enter",bg="#a8e7ee",font=("Areal",16))
    input.grid(row=1,column=1)
     
    def chak():
        i=int(input.get())
        year=2026-i
        if i=="":
            messagebox.showwarning("warning","box khali he")
        elif i >=2026:
            messagebox.showwarning("warning","age gaalet he")
        else:
            messagebox.showinfo("result",f"tumne age {year} he ")

    b=tk.Button(root,text="chak",bg="#cac448",font=("Areal",16),command=chak)
    b.grid(row=1,column=2 ,padx=10, pady=10)

except ValueError:
    messagebox.showwarning("only a number ...")

root.mainloop()
