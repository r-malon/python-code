num=int(input("Digite um numero menor que 10: "))
if num>10:
    raise FileNotFoundError
    print("numero maior q 10")
else:
    print("menor q 10")
