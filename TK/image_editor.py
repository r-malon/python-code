from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageGrab, Image, ImageTk

def about():
	messagebox.showinfo('About',
	 'Text Editor v0.1\nCreated by Jailson.')

def locate(event):
	global x
	global y
	x = event.x
	y = event.y

def draw(event):
	canvas.create_line(x, y, event.x, event.y, fill="black", width=3)
	locate(event)

def get_img(event=None):
	x1 = root.winfo_rootx() + canvas.winfo_x()
	y1 = root.winfo_rooty() + canvas.winfo_y()
	x2 = x1 + canvas.winfo_width()
	y2 = y1 + canvas.winfo_height()
	ImageGrab.grab().crop((x1,y1,x2,y2)).save("file.png") #Windows only

def maximize(event):
	root.attributes("-fullscreen", True)
	root.bind("<F11>", minimize)

def minimize(event):
	root.attributes("-fullscreen", False)
	root.bind("<F11>", maximize)

root = Tk()
root.geometry("600x480")
menu = Menu(root)
bottom_bar = Frame(relief=SUNKEN)
img = PhotoImage(file=r"C:\Users\RAFAEL\Pictures\Nova pasta\Locker\secur\animal_mother_charge.gif")
canvas = Canvas(root, cursor="cross")
canvas.create_image((0, 0), image=img)

file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
options_menu = Menu(menu, tearoff=0)

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Edit', menu=edit_menu)
menu.add_cascade(label='Options', menu=options_menu)

file_menu.add_command(label='New file', command=lambda: canvas.delete(ALL))
file_menu.add_command(label='Open file')#, command=open_file)
file_menu.add_command(label='Save file')#, command=saveas)

options_menu.add_cascade(label='Change line width')
options_menu.add_cascade(label='Change line color')
options_menu.add_cascade(label='Change canvas color')

root.bind("<F11>", maximize)
canvas.bind("<Motion>", locate)
canvas.bind("<B1-Motion>", draw)
root.bind("<Control-s>", get_img)
root.bind("<Control-n>", lambda x: canvas.delete(ALL))

if __name__ == '__main__':
	canvas.pack(fill="both", expand=True)
	bottom_bar.pack(fill=X)
	root.config(menu=menu)
	root.mainloop()