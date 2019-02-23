x=int(input("Digite um numero:"))
cent=x//100
dez=(x%100)//10
uni=(x%100)%10
if cent>0 or dez>0:
    print("Esse número tem",cent,"centenas,",dez,"dezenas e",uni,"unidades")
    print("E de trás pra frente ele é", uni, dez, cent)
elif cent==0:
    print("Esse número tem",dez,"dezenas e",uni,"unidades")
    print("E de trás pra frente ele é", uni, dez)
elif dez==0:
    print("Esse número tem",uni,"unidades")
    print("E de trás pra frente ele é", uni)

                                        #ou: list(str(x)) == fácil?
