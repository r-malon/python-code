import math

def xand1(lado1, lado2, lado3):
	x = lado1**2 - lado2**2 - lado3**2
	tocos = x/(-2*lado2*lado3)
	return math.degrees(math.acos(tocos))

def xand2(lado1, lado2, ang):
	lado3 = lado1**2 + lado2**2 - 2*lado1*lado2*math.cos(math.radians(ang))
	x = lado1**2 - lado2**2 - lado3**2
	y = x/(-2*lado2*lado3)
	ang2 = math.degrees(math.cos(y))
	ang3 = 180-(ang+ang2)
	return ang2, '\n', ang3

def xand3(ang, lado1, lado2): #errors
	hiddenside = math.sqrt(lado1**2 + lado2**2 - 2*lado1*lado2*math.cos(math.radians(ang)))
	return hiddenside

def xand4(ang1, ang2):
	return 180 - (ang1 + ang2)

def xand5(ang1,ang2,lado):
	ang3 = 180 - (ang1 + ang2) #huge flaw here!
	a = lado*math.sin(math.radians(ang1)) / math.sin(math.radians(ang2))
	b = lado*math.sin(math.radians(ang3)) / math.sin(math.radians(ang2))
	return a, '\n', b

def xand6(ang1, ang2, ang3):
	#impossible!
	pass

if __name__ == '__main__':
	print('alpha: ', xand1(7,6,5), 'beta:', xand1(5,6,7), 'gamma: ', xand1(6,5,7))