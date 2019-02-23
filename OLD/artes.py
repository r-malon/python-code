import winsound as ws
from random import *
import os
for i in range(100):
    freq=randrange(200, 32000, 100)
    time=randrange(300, 1500, 100)
    ws.Beep(freq, time)
ws.PlaySound('SystemHand',SND_ALIAS)
os.system('pause')
