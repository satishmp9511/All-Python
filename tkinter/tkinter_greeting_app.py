import tkinter as tk

root = tk.Tk()
root.title("Hello World App")
root.geometry("600x400")

def on(a="enter",b='label',c='label_2',d='button_1'):
    name=a.get()
    if d.get()==True:
        b_b="ho"
    else:
        b_b="nahi ho"
    b.config(text=f"hello {name}",fg="green",font=("Arial",20,"bold"))
    c.config(text=f"kese ho {name}\n tum 18+ {b_b}",fg="green",font=("Arial",20,"bold"))

def off():
    label.config(text="hi",fg="red")
    label_2.config(text="",fg="green",font=("Arial",20,"bold"))

label = tk.Label(root,text="hi",fg="red")
label.place(x=0,y=0)

enter=tk.Entry(root)
enter.insert(0,"enter a name")
enter.place(x=230,y=50)

button=tk.Button(root,text="normal",bg="red",command=off)
button.place(x=380,y=50)

button_1=tk.Button(root,text="Click me",bg="blue",command=lambda:on(enter,label,label_2,b_c))
button_1.place(x=380,y=90)

label_2=tk.Label(root,text="",fg="green",font=("Arial",20,"bold"))
label_2.place(x=170,y=250)

b_c=tk.BooleanVar()
c_k=tk.Checkbutton(root,text="you are 18+",variable=b_c)
c_k.place(x=450,y=50)

root.mainloop()




