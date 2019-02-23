def tri(n):
    while n <= 0: # use if ...: return 'erro'
        n = int(input('diga: '))
    lista = []
    for i in range(n):
        char = n-i
        lista.append(i*' ' + char*'*')
    return lista

if __name__ == '__main__':
    x = tri(6)
    for i in x:
        print(i)