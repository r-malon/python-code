from tkinter import *
from tkinter import messagebox
from web_scraper import get_scrap

def about():
	messagebox.showinfo('About', 'Web Scraper v0.1\nCreated by Jailson.')

#def change_bg(color):
#	win.config(background=color)

colorlist = ['lightgreen', 'red', 'lightblue']

win = Tk()
win.geometry("600x480+350+50")
win.title('Web Scraper v0.1')
link = StringVar()
box = Entry(win, textvariable=link)
msg = Message(win, text='Put the link you want to scrap here: ', font=('Rockwell', 18), aspect=600)
btn = Button(win, text='Go!', command=lambda: get_scrap(link, 'li'))
datalist = Label(win, text='')
menu = Menu(win)
optmenu = Menu(menu, tearoff=0)
colormenu = Menu(optmenu, tearoff=0)

menu.add_cascade(label='Options', menu=optmenu)
menu.add_command(label='About', command=about)
menu.add_separator()
menu.add_command(label='Quit', command=win.quit)

for color in colorlist:
	colormenu.add_command(label=color, command=lambda: win.config(background=color))
optmenu.add_cascade(label='Change Background', menu=colormenu)

if __name__ == '__main__':
	msg.pack(pady=15)
	box.pack(pady=5)
	btn.pack()
	datalist.pack(pady=10)
	win.config(menu=menu)
	win.mainloop()