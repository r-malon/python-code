class Filme:
	def __init__(self):
		self.ano = 0
		self.nome = 0
		self.nota = 0
	def __str__(self):
		return 'Nome: %s\n Ano de lançamento: %d\n Nota: %d\n' % (self.nome, self.ano, self.nota)

filmes = []

def check():
	try:
		global choose
		choose = int(input('Escolha uma opção: '))
	except ValueError:
		print('Valor inválido!')
		check()
		
def options():
	opt = ['remover', 'adicionar', 'ver itens']
	for i in range(1, len(opt) + 1):
		print('%d - %s' % (i, opt[i - 1]))
	check()

def remover():
	if not filmes:
		return 'Nada para remover!\n'
	for i in range(1, len(filmes) + 1):
		print('%d - %s' % (i, filmes[i - 1].nome))
	n = int(input('Qual vc quer remover? '))
	filmes.remove(n - 1)
	return '%s foi removido!' % filmes[i - 1].nome

def ver():
	if not filmes:
		return "Nada para mostrar...\n"
	for y in filmes:
		print('Filme: \n', y)

if __name__ == '__main__':
	options()
	#choose=int(input('Escolha uma opção: '))
	while True:
		if choose == 1:
			print(remover())
			options()
			
		elif choose == 2:
			n = int(input('Digite quantos irá adicionar: '))
			for i in range(n):
				x = Filme()
				x.nome = input('Nome: ')
				x.ano = int(input('Anos: '))
				x.nota = int(input('Nota: '))
				filmes.append(x)
			options()
		else:
			print(ver())
			options()