def armstrong(n):
	n = str(n)
	soma = 0
	for i in n:
		soma += int(i)**len(n)
	return soma == int(n)

if __name__ == '__main__':
	number = 407
	print(f"Is {number} an Armstrong number? ", armstrong(number))