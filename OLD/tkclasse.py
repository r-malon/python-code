from tkinter import *
from tkinter import messagebox
def add():
    messagebox.showinfo("Resultado", float(a.get())+float(b.get()))
win=Tk()
win.geometry('300x200')
a=StringVar()
b=StringVar()
in1=Entry(win, textvariable=a)
in2=Entry(win, textvariable=b)
btn=Button(win, text="Somar", activebackground='green', command=add)
in1.pack()
in2.pack()
btn.pack()
win.mainloop()
