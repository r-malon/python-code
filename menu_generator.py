import os  #and os.popen('stty size')
#import shutil #console size: only for unix?
from platform import system as plt

def clear():
	if plt() == "Linux":
		os.system("clear")
	elif plt() == "Windows":
		os.system("cls")
	else:
		print(80 * "\n")

def pause():
	if plt() == 'Windows':
		os.system('pause')
	else:
		input('Press ENTER to continue...')

def menu(options): #options should be dict? and *prevmenu?
	for i in range(len(options)): #use zip()?
		print("%d - %s" % (i + 1, options[i][0])) #list(options.items())[i][0]))
	'''for i in options: #made for dicts?
    print("%d - %s" % (i+1, options[i]))'''

	print('-' * 75) #default size for windows
	print('0 - Exit')

	while True:
		try:
			choose = int(input('What will you do? '))
			while choose - 1 not in range(len(options)): #int vs str!!!
				choose = int(input('Wrong option, type again: '))
			break
		except ValueError:
			print("Bad value, type again! ", end='')

	exec(options[choose-1][1])

if __name__ == '__main__':
	menu([['say something', 'for i in range(10):\n\tprint("hi")'], ['shit', 'os.system("pause")']])