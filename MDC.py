def mdc(a, b):
	c = a % b
	while c != 0:
		print(f'a: {a}\nb: {b}')
		a = b
		b = c
		c = a % b
		print(f'a: {a}\nb: {b}')

if __name__ == '__main__':
	mdc(48, 30)