#   x=funcionario('jose', 300, 'faxineiro')
class funcionario:
    def __init__(self, nome, salario, funcao):
        self.nome = nome
        self.salario = salario
        self.funcao = funcao
        self.arq = open('C:\\Users\\RAFAEL\\Videos\\cadastroV2.txt', 'a')
        #self.arq.write('Lista dos %d cadastrados: \n' % x)
        self.num = 0
        #num += 1 unboundlocalerror
        #person = [nome, funcao, salario] ---> nonsense
        
    def show(self): #método idiota, mostra apenas o funcionario atual
        self.num += 1
        print('Há %d funcionarios atualmente' % self.num)
    def info(self):
        print('%s é um %s e ganha R$%d por mês' % (self.nome, self.funcao, self.salario))
    def demite(self):
        print('%s foi expulso!' % self.nome)
        del self.nome
    def cadastra(self):
        try:
            self.arq.write('Nome: '+self.nome+'\n'+'Função: '+self.funcao+'\n'+'Salário: '+str(self.salario)+'\n\n')
            print('Usuário cadastrado...')
        except FileNotFoundError:
            print('Não foi possível criar o arquivo!')
        finally: #executa isso independentemente do resultado
            self.arq.close()
