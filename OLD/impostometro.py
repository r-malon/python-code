print("IMPOSTOS")
sb=int(input("Digite seu salario: "))
inss=sb*0.10
ir=sb*0.15
sind=0.05*sb
sl=sb-(ir+inss+sind)
imptotal=ir+inss+sind
print("O seu salario líquido é R$", sl,"e foram descontados R$",imptotal,"de seu salario bruto")
