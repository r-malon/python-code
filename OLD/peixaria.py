print("Pesa-Peixes")
peso=int(input("Digite o peso dos peixes: "))
exc=peso-50
if peso>50:
    print("Você pescou",peso-50,"kg a mais e vai pagar uma multa de R$",exc*4)
else:
    print("Tudo OK, não vai ter multa")
