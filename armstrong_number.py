def armstrong(n):
	n = str(n)
	soma = 0
	for i in n:
		soma += int(i)**len(n)
	return soma == int(n)

'''def happy(n):
	n = str(n)
	soma = 0
	while soma != 1:
		for i in n:
			soma += int(i)**2'''

if __name__ == '__main__':
	number = 407
	print("Is %d an Armstrong number? " % number, armstrong(number))
	#print("Is %d a happy number? " % number, happy(number))