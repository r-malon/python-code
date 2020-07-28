print("Conversor para horário P.M.")
h = int(input("Digite que horas são: "))
m = int(input("Digite os minutos: "))
if m > 59 or h > 24:
	 print("Erro!!!")
elif h >= 12:
	print("São ", h-12,":", m, " P.M.")
else:
	if len(str(h)) < 2:
		print("São 0%d:%d" % (h, m))
	else:
		print("São %d:%d" % (h, m))