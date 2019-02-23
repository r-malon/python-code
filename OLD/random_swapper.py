from random import *
def swapper(frase):
    #frase=list(frase)
    #x=list({randint(0, len(frase)) for i in range(len(frase))})
    #for i in range(len(frase)):
        #frase[i]=frase[x[i]]
    #frase=shuffle(frase)
    return shuffle(list(frase))
print(swapper('jailson'))
