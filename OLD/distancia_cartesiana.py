def cartesian_distance(x1, x2, y1, y2):
	return ((x1 - x2) ** 2 + (y1-y2) ** 2) ** 0.5

if __name__ == '__main__':
	print(cartesian_distance(2, 4, 1, 4))