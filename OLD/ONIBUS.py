money=int(input("Digite quanto dinheiro você tem:"))
tipo=input("Qual seu tipo: ")
if tipo=="estudante":
        print("Estudante paga meia, ou seja, R$ 2")
        if money/30>=4:
                print("Tudo OK, você pode fazer",money/2,"viagens")
        else:
                print("Saldo insuficiente")                                                                                        
elif tipo=='adulto':
        print("Você paga inteira")
        if money/30>=4:
                print("Tudo OK, você pode fazer",money/4,"viagens")
        else:
                print("Saldo insuficiente")
else:
        print("ERRO!!!")
