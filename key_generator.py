from string import ascii_letters, digits
from random import choice
import os

def key_gen(char_num, blocks, charset=list(ascii_letters + digits)):
	key = ''
	for i in range(blocks):
		for j in range(char_num):
			key += choice(charset)
		key += separator
	return key.strip(separator)

if __name__ == '__main__':
	print('\n' + "Serial Key Generator".center(80, '-'))
	print("Example: 5Sxn-M9p1-08MN-11Pg\n")

	key_number = int(input("Type how many keys will be generated: "))
	char_num = int(input("Type how many characters per block: "))
	blocks = int(input("Type how many blocks: "))
	separator = input("Type the block separator e.g. hyphen, can be empty: ")
	print()
	file = open("output.txt", "a+")

	for i in range(key_number):
		key = key_gen(char_num, blocks)
		file.write(key + '\n')
		print(key)

	file.close()
	print("\nGenerated keys written to 'output.txt'")
	print("Type any key to exit...")
	os.system("pause >nul")