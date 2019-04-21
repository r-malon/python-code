from pygame import *
from random import *
'''import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
embed = tk.Frame(root, width = 800, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
'''
init()
screen = display.set_mode((800, 500)) #(width, height)
#surf=Surface((100,100))
color = [255, 255, 255]
position = [30, 30]
active = True
clock = time.Clock()
ball_size = 20
reta = rect.Rect(40, 50, 60 , 70) #calling module
#img=image.load("C:\\Users\\RAFAEL\\Pictures\\img103.png", 'imagem bonita') #legenda??
#img_small=transform.scale(img, (75, 50))
#img_small=transform.rotozoom(img, 30, 1.2) #buggy???
display.set_caption('jailson mendes')
icon = image.load(r"C:\Users\RAFAEL\Videos\Python and other random things\fallout.ico")
display.set_icon(icon)
mouse_pos = mouse.get_pos()
fonte = font.Font(None, 56)
txt = fonte.render('perdeu!', 1, (90, 75, 210))
while active:
    for eve in event.get():
        if eve.type == QUIT:
            active = False
        if eve.type == KEYDOWN:
            if eve.key == K_DOWN:
                position[1] += 10
                screen.fill((255, 0, 0)) #impede efeito "minhoca escavando"
            if eve.key == K_UP:
                position[1] -= 10
                screen.fill((0, 255, 0))
            if eve.key == K_LEFT:
                position[0] -= 10
                screen.fill([255, 175, 0]) #list ou tuple, tanto faz
            if eve.key == K_RIGHT:
                position[0] += 10
                screen.fill((0, 0, 100))
            if eve.key == K_SPACE:
                for i in range(3):
                    color[i] = randint(0, 255)
            if position[0] > 780 or position[0] < 20:
                #active=False
                quit()
            if reta.collidepoint(50, 30) == 1:
                ball_size = 50
        '''if eve.type == MOUSEMOTION: #ao mover o botão!!
            mpos=mouse.get_pos()
            position=list(mpos)
            screen.fill((0,0,0))'''
        draw.circle(screen, color, position, ball_size)
        draw.rect(screen, (60, 70, 80), (100, 100, 150, 50), 0)
        screen.blit(txt, (400, 250)) #texto
        #screen.blit(img_small, position) #move junto c/ mouse
        #surf.fill((100, 0, 150))
        display.flip()
        clock.tick(240)#frames per second(fps)
