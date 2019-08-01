from math import pi

neg, result = True, 1
limit = int(input('Input the limit: '))

for i in range(3, limit, 2):
	if neg:
		result -= 1/i
	else:
		result += 1/i
	neg = not neg

print('π: ', pi)
print(result * 4)