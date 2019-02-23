tipo=input("Qual seu sexo: ")
alt=int(input("Qual sua altura: "))
peso=int(input("Qual seu peso: "))
ideal1=(alt*70)-60
ideal2=(alt*60)-50
if tipo=="homem":
    print("Seu peso ideal é",ideal1)
    if peso>=(ideal1+5):
        print("gordo")
    elif peso<=(ideal1-5):
        print ("magro")
    else:
        print("Peso ideal para homem")
elif tipo=="mulher":
    print("Seu peso ideal é", ideal2)
    if peso>=(ideal2+5):
        print("gordaa")
    elif peso<=(ideal2-5):
        print("magrela")
    else:
        print("Peso ideal para mulher")
else:
    print("Sexo Inváalido")
