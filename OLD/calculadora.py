x = int(input("Digite o nº que vai somar: "))
oper = input("Digite a operação que vai fazer: ")
y = int(input("Agora o outro nº: "))
if oper == "/":
    print("O resultado é", x/y)
elif oper == "*":
    print("O resultado é", x*y)
elif oper == "-":
     print("O resultado é", x-y)
elif oper == "+":
    print("O resultado é", x+y)
else:
    print("Inválido")
