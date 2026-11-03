import tkinter as tk

root=tk.Tk()
root.title("Hello World App")
root.geometry("600x500")

user=0
computer=0

def on():
    import random
    global user, computer
    t=tk_var.get()
    c_choose=random.choice(["r","p","s"])
    if t==c_choose:
        label_f.config(text=f"match draw : you both choose same:{c_choose}",fg="red",font=("Arial",12))
    elif t=="r" and c_choose=="s":
        label_f.config(text=f"you win : computer choose scissors",fg="green",font=("Arial",12))
        user+=1
        label_1.config(text=f"your score: {user}")
    elif t=="r" and c_choose=="p":
        label_f.config(text=f"you lose : computer choose paper",fg="red",font=("Arial",12))
        computer+=1
        label_2.config(text=f"computer score: {computer}")
    elif t=="p" and c_choose=="r":
        label_f.config(text=f"you win : computer choose rock",fg="green",font=("Arial",12))
        user+=1
        label_1.config(text=f"your score: {user}")
    elif t=="p" and c_choose=="s":
        label_f.config(text=f"you lose : computer choose scissors",fg="red",font=("Arial",12))
        computer+=1
        label_2.config(text=f"computer score: {computer}")
    elif t=="s" and c_choose=="p":  
        label_f.config(text=f"you win : computer choose paper",fg="green",font=("Arial",12))
        user+=1
        label_1.config(text=f"your score: {user}")
    elif t=="s" and c_choose=="r":
        label_f.config(text=f"you lose : computer choose rock",fg="red",font=("Arial",12))
        computer+=1
        label_2.config(text=f"computer score: {computer}")
    else:
        label_f.config(text=f"invalid input",fg="red",font=("Arial",12))

def reset():
    global user, computer
    user=0
    computer=0
    label_1.config(text=f"your score: {user}",fg="red",font=("Arial",12))
    label_2.config(text=f"computer score: {computer}",fg="red",font=("Arial",12))

label=tk.Label(root,text="Welcome to rock, paper, scissors !",fg="red",font=("Arial",20,"bold"))
label.grid(row=0,column=1)

label_1=tk.Label(root,text="your score: 0",fg="red",font=("Arial"))
label_1.grid(row=2,column=0)

label_2=tk.Label(root,text="computer score: 0",fg="red",font=("Arial"))
label_2.grid(row=2,column=2)

label_f=tk.Label(root,text="",fg="red",font=("Arial"))
label_f.grid(row=3,column=1)

tk_var=tk.StringVar(value="r")

tk.Radiobutton(root,text="rock",value="r",variable=tk_var).grid(row=1,column=0)
tk.Radiobutton(root,text="paper",value="p",variable=tk_var).grid(row=1,column=1)
tk.Radiobutton(root,text="scissors",value="s",variable=tk_var).grid(row=1,column=2)

btn=tk.Button(root,text="play",bg="#1e90ff",width=10,command=on)
btn.grid(row=2,column=1)

btn=tk.Button(root,text="reset",bg="#ff0000",width=10,command=reset)
btn.grid(row=4,column=2)

btn=tk.Button(root,text="exit",bg="#ff0000",width=10,command=root.destroy)
btn.grid(row=5,column=2)

root.mainloop()

