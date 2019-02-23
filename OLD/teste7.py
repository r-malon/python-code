n1=float(input("Digite a nota 1:"))
n2=float(input("Digite a nota 2:"))
media=(n1+n2)/2
if 9<=media<=10:
    print("Conceito A(provado)")
elif media<6:
    print("Reprovô, ce e buro!!!")
else:
    print("passou, mas vc no é grands coisa")
