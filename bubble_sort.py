def sorter(l):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(l) - 1):
			if l[i] > l[i + 1]:
				l[i], l[i + 1] = l[i + 1], l[i]
				swapped = True
	return l

if __name__ == '__main__':
	print(sorter([12, 5, 13, 11.2, 14, 1, 3, 2, 2.5]))
