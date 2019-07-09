from pygame import *
from random import *

init()
display.init()
screen = display.set_mode((400, 400))
clock = time.Clock()
colors = [
	'#070707',
	'#1F0707',
	'#2F0F07',
	'#470F07',
	'#571707',
	'#671F07',
	'#771F07',
	'#8F2707',
	'#9F2F07',
	'#AF3F07',
	'#BF4707',
	'#C74707',
	'#DF4F07',
	'#DF5707',
	'#DF5707',
	'#D75F07',
	'#D75F07',
	'#D7670F',
	'#CF6F0F',
	'#CF770F',
	'#CF7F0F',
	'#CF8717',
	'#C78717',
	'#C78F17',
	'#C7971F',
	'#BF9F1F',
	'#BF9F1F',
	'#BFA727',
	'#BFA727',
	'#BFAF2F',
	'#B7AF2F',
	'#B7B72F',
	'#B7B737',
	'#CFCF6F',
	'#DFDF9F',
	'#EFEFC7',
	'#FFFFFF']
blocks = []
for i in range(0, 400, 20):
	for j in range(0, 400, 20):
		blocks.append(rect.Rect(i, j, 20, 20))

while True:
	for eve in event.get():
		if eve.type == QUIT:
			quit()
		screen.fill((255, 0, 0))
		for block, color in zip(blocks, colors):
			draw.rect(screen, Color(color), block, 0)
		display.flip()
		clock.tick(35)