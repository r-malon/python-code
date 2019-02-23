n1=int(input("Digite a 1º nota:"))
n2=int(input("Digite a 2º nota:"))
n3=int(input("Digite a 3º nota:"))
media=(n1+n2+n3)/3
if n1 or n2 or n3 > 11:
    print("Nota Inválida")
elif media < 7:
    print("Reprovô, nota", media)
elif media==10:
    print("Aprovado com honraria máxima da nação!!!")
elif media >= 7:
    print("Aprovado, tirou",media,"!!!")
