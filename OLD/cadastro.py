import time
import os

dados = {}

try:
	x = int(input('Digite o número de cadastrados, pressione Enter se deseja um valor infinito: '))
except ValueError:
	x = 0
	while x < 100000:
		x = x + 1

for i in range(0, x):
	n = input('Digite seu nome ou QUIT para encerrar: ')
	if n == 'QUIT':
		break
	dados['nome%d' % i] = n
	time.sleep(0.5)

while n == "":
	n = input('Nome invalido, digite seu nome: ')
	time.sleep(0.5)

try:
	file = open("C:\\Users\\RAFAEL\\Music\\cadastro.txt", "w+")
	file.write('Lista dos %d cadastrados: \n' % x)
	for i in range(0, x):
		print(dados['nome%d' % i])
		file.write('%d - ' % (i+1))
		file.write(dados['nome%d' % i])
		file.write('\n')
except FileNotFoundError:
	print('Não foi possível criar o arquivo!')
finally:
	print('Execução terminada...')
	file.close()