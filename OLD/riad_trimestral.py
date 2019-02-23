def square(n):
	inicio=n * '* '
	lista=[inicio, inicio]
	for i in range(n-2):
		line = '*%s*' % ((n+2)*' ')
		lista.insert(1, line)
	return lista

x=square(4)
for i in x:
    print(i)

class Disciplina:
	def __init__(self, nome, tempo, alunos):
		self.nome=nome
		self.tempo=tempo
		self.alunos=alunos

def gravar(name):
	arq=open(name, 'a')
	for n in lista:
		arq.write(n.nome + ';' + str(n.tempo) + ';' + str(n.alunos) + '\n')
	arq.close()

def recuperar(name):
    arq = open(name, 'r')
    recuperado = []
    for line in arq.readlines():
        for x in line.split(';'):
            if x != '':
                recuperado.append(x)
    arq.close()
    return recuperado

global lista
lista=[Disciplina('Hardware', 60, ['jaja', 'igor']), Disciplina('Inglês', 30, ['jose', 'joao'])]

gravar(r"C:\Users\RAFAEL\Music\cadastro.txt")
for dado in recuperar(r"C:\Users\RAFAEL\Music\cadastro.txt"):
    print(dado)
