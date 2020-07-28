def vowel_square(x):
	vowels = ['a', 'e', 'i', 'o', 'u']
	topleft = []
	for line in x:
		for i in range(len(line)-1):
			if line[i] in vowels and line[i+1] in vowels:
				topleft.append([x.index(line), i])
	return topleft

if __name__ == '__main__':
	print(vowel_square(["aqrst", "ukaei", "ffooo"]))
	print(vowel_square(["abcd", "eikr", "oufj"]))
	print(vowel_square(["fff", "ggg"]))