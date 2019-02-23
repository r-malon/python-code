print("Gerador de Tabuadas")
x=int(input("Digite o nº da tabuada que quer aprender: "))
print('\nTabuada de %d \n' % x)
for n in range(1, 11):
    print('%d X %d = %d' % (x, n, n*x))
