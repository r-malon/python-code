def mdc(a, b):
	c = a % b
	while c != 0:
		print(f'A: {a}\nB: {b}')
		a = b
		b = c
		c = a % b
		print(f'A: {a}\nB: {b}')

if __name__ == '__main__':
	mdc(48, 30)
