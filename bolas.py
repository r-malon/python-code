def bolas(diff, total, x, y):
	price_x = (total - diff * x) / (x + y)
	price_y = price_x + diff
	print("Preço de um x: ", price_x)
	print("Preço de um y: ", price_y)
	print("Preço de todos x: ", price_x * y)
	print("Preço de todos y: ", price_y * x)

def convidador(por_amigo, amigos, convites):
	return convites - (amigos * por_amigo)

print(convidador(4, 40, 105))
#bolas(40, 1280, 6, 10)