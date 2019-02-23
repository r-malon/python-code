from tkinter import *
from datetime import datetime as dt
master=Tk()
master.geometry('300x200+300+100')
master.title('Relógio')
msg=Message(master, text=dt.now().second)
msg.pack()
while True:
    msg.config(bg='blue', text=dt.now().second)
master.mainloop()
