from tkinter import *

root = Tk()
root.attributes("-alpha", 0)
root.attributes('-topmost', 1) #???
root.title('My App')
top = Toplevel(root)
top.overrideredirect(True)
top.geometry('800x600+300+100')

title_bar = Frame(top, bg='red', relief='raised', height=50)

def onRootIconify(event):
	top.withdraw()
	root.bind("<Unmap>", onRootIconify)

def onRootDeiconify(event):
	top.deiconify()
	root.bind("<Map>", onRootDeiconify)

if __name__ == '__main__':
	title_bar.pack(expand=True, fill=X, side=TOP)
	#window = Frame(master=top)
	root.mainloop()