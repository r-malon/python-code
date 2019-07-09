print("Este caixa devolve apenas notas de R$ 100,R$ 50 ,R$ 10, R$ 5, R$ 1!!!")
x = int(input("Digite quanto dinheiro você vai sacar: "))
nota100 = x // 100
nota50 = (x%100)//50
nota10 = ((x%100)//50)//10
nota5 = (((x%100)//50)//10)//5
nota1 = 
if x >= 1000 or x < 1:
    print("Valor Inválido")
else:
    print("Você sacou %d de R$100, %d de R$50, %d de R$10, %d de 5 e %d de R$1..." % (nota100, nota50, nota10, nota5, nota1)) 
