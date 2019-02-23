from random import *
x = []
tent = 0
mx = int(input('tamanho da lista: '))
while True:
    n = randint(0, mx)
    x.append(n)
    tent+=1
    if x.count(n) > 1:
        x.remove(n)
    if len(x) > mx:
        break
print('A lista é %s e o nº de tentivas foi %d' % (x, tent))
