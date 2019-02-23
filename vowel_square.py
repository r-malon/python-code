def VowelSquare(x):
	vowels = ['a', 'e', 'i', 'o', 'u']
	topleft = []
	for line in x:
		for i in range(len(line)-1):
			if line[i] in vowels and line[i+1] in vowels:
				topleft.append([x.index(line), i])
	return topleft

if __name__ == '__main__':
	print(VowelSquare(["aqrst", "ukaei", "ffooo"]))
	print(VowelSquare(["abcd", "eikr", "oufj"]))
	print(VowelSquare(["fff", "ggg"]))