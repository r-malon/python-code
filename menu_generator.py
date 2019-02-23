import os  #and os.popen('stty size')
#import shutil #console size: only for unix?
import platform as plt

def clear():
	if plt.system() == "Linux":
		os.system("clear")
	elif plt.system() == "Windows":
		os.system("cls")
	else:
		print(80 * "\n")

def pause():
	if plt.system() == 'Windows':
		os.system('pause')
	else:
		input('Press ENTER to continue...')

#mustexit is for events!

def menu(opt, mustexit=True): #opt should be dict? and *prevmenu?
	for i in range(len(opt)):  #use zip()?
		print("%d - %s" % (i + 1, opt[i][0])) #list(opt.items())[i][0]))
	'''for i in opt: #made for dicts?
    print("%d - %s" % (i+1, opt[i]))'''

	if mustexit:
		print('-' * 75) #default size for windows
		print('0 - Exit')

	while True:
		try:
			choose = int(input('What will you do? ')) #use check?
			break
		except ValueError:
			print("Bad value, type again! ", end='')

	if choose == 0 and mustexit: #or choose=='0'
		clear()
		#menu(prevmenu, opt, mustexit) #fix it!
		return
	#join these 2?
	while choose-1 not in range(len(opt)): #int vs str!!!
		choose = int(input('Wrong option, type again: '))
	exec(opt[choose-1][1])
	pause()

if __name__ == '__main__':
	menu([['say something', 'print("delicia")'], ['shit', 'os.system("pause")']], True)
	 #[['play game', 'clear()'], ['die', 'print("yo dead!")']], 1)