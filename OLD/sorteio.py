import random
x1 = input("Digite o nome do 1º jogador: ") 
x2 = input("Digite o nome do 2º jogador: ") 
x3 = input("Digite o nome do 3º jogador: ") 
sort = random.randint(1, 3) 
if sort == 1:
    print("Parabéns",x1,"vc ganhou!!!")
elif sort == 2:
    print("Parabéns",x2,"vc ganhou!!")
elif sort == 3:
    print("Parabéns",x3,"vc ganhou!!")
