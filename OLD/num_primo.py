'''print('2 é primo!')
for i in range(n):
    if i % 2 != 0:
        for z in range(3, n, 2):
            if i % z != 0:
                print('%d é primo!' % i)'''

def prime(n):
	primos=[]
	for i in range(2, 10):
		if n%i != 0 or n==i:
			primos.append(True)
		else:
			primos.append(False)
	return primos

if __name__ == '__main__':
    n = int(input('diga: '))
    if False in prime(n):
        print('not prime!')
    else:
        print('prime')
