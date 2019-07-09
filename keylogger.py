from msvcrt import kbhit, getch

while True:
	#if kbhit(): #laggy
		#print(getch())
	with open('log.txt', 'ab+') as f:
		f.write(getch())