from pygame import *
from pygame import event as events
from random import *

init()
display.init()
screen = display.set_mode((512, 512))
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
	'#FFFFFF'
]

def render():
	screen.fill((0, 0, 0))
	j = -1
	line = 0
	for i in range(len(blocks)):
		if j <= -38:
			break
		if randrange(0, line + 1) < 3:
			draw.rect(screen, Color(colors[j]), blocks[i], 0)
		if i % 64 == 0:
			j -= 1
			line += 1
	display.flip()

blocks = []
for i in range(512, 0, -8):
	for j in range(0, 512, 8):
		blocks.append(rect.Rect(j, i, 8, 8))

running = True
while running:
	for event in events.get():
		if event.type == QUIT:
			running = False
		elif event.type in [KEYUP, KEYDOWN]:
			if event.key == K_ESCAPE:
				running = False

		render()
		clock.tick(60)