'''
Tk widgets: button,canvas,checkbutton, combobox, entry, frame
label, labelframe, listbox, menu, menubutton,message
notebook, tk_optionMenu, panedwindow
progressbar, radiobutton, scale, scrollbar
separator, sizegrip, spinbox, text, treeview

TopLevel windows:
tk_chooseColor - pops up a dialog box for the user to select a color.
tk_chooseDirectory - pops up a dialog box for the user to select a directory.
tk_dialog - creates a modal dialog and waits for a response.
tk_getOpenFile - pops up a dialog box for the user to select a file to open.
tk_getSaveFile - pops up a dialog box for the user to select a file to save.
tk_messageBox - pops up a message window and waits for a user response.
tk_popup - posts a popup menu.
toplevel - creates and manipulates toplevel widgets.
'''
from tkinter import *
from tkinter import messagebox
from time import sleep
#Pricedown BL
#foreground: text color
win = Tk()
win.geometry("800x600+250+50") #offset: places window in PC screen
win.title('Testinhos Aleatórios!!!')
x=StringVar()
frost=StringVar()
var=IntVar()
frost.set('congelado!\n espera um pouco...')
inp=Entry(win, textvariable=x, show="*")
scroller=Scrollbar(win)
scroller.pack(side=RIGHT, fill=Y)
listbox = Listbox(win)#, yscrollcommand=scroller.set) #Listbox: lista de alternativas
for i in range(2000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)
scroller.config(command=listbox.yview)

def hello():
    messagebox.showerror("msg de guina", x.get())

def typewriter(frase):
    for i in frase:
        Message(win, text=i).pack()
        sleep(0.1)

def ola(evento):
    print('label movido na posição', evento.x, evento.y)

msg=Message(win, text=('mensagem saudável!!!'), relief=GROOVE)#decoração da borda
msg.config(bg='lightblue', font=('Pricedown BL', 14, 'italic'), aspect=250, padx=40, pady=30)
btn=Button(win, text="clique!", cursor="dot", bd=1, activeforeground="red", height=2, width=4, command=hello)
cv=Canvas(win, height=250, width=450, cursor="circle") #desenhos!
ln=cv.create_oval(30, 50, 70, 20, fill="darkgreen")
arq=PhotoImage(file="C:\\Users\\RAFAEL\\Pictures\\van gogh.png" )
img=cv.create_image(200, 200, image=arq)
txt=Text(win)
frostxt=Label(win, textvariable=frost, font=('Old English Text MT', 20))#, text='ola'#, relief=RAISED)
frostxt.bind('<Motion>', ola) #ao mexer o mouse no Label

filho=Toplevel(bg='navy')
filho.title('Siga-me filho...')
filho.geometry('300x240')
Message(filho, text='...mas tenha cuidado!').grid(row=0,column=0, pady=5)
Button(filho, text='Exit', command=filho.destroy).grid(row=1,column=0, pady=5)

def retornar():
    #messagebox.showinfo('you selected %d' % var.get())
    msg.config(text='vc escolheu %s' % lang[var.get()])

lang = [("Python"), ("Perl"), ("Java"), ("C++")]
cv.pack()
inp.pack()#side=RIGHT)
btn.pack()
txt.insert(INSERT, "ola jailson")
txt.insert(END, 'como vai')
#txt.pack()
frostxt.pack()
msg.pack()
for val, name in enumerate(lang):
    radio=Radiobutton(win, text=name, font=28, #indicatoron para bloquinho
                variable=var,
                value=val,
                command=retornar)#.pack(anchor=W)
    radio.pack(pady=5)
win.mainloop()
