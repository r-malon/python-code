from random import sample

ALPHABET= ' abcdefghijklmnopqrstuvwxyz'
MAX_KEY_SZ = 9

def gen_key(length):
	return sample(range(0, MAX_KEY_SZ), length)

def clamp(n):
	return max(0, min(n, MAX_KEY_SZ))

def encode(text, key):
	encoded = []
	key_index = 0
	key_sz = len(key)
	text = text.lower()
	text += ' ' * (key_sz - (len(text) % key_sz)) # padding
	for i in text:
		index = ALPHABET.index(i)
		encoded.append((index + key[key_index % key_sz]))
		key_index += 1

	return ''.join([ALPHABET[i] for i in encoded]) # >26 overflow

def decode(text, key):
	decoded = []
	key_index = 0
	key_sz = len(key)
	text = text.lower()
	for i in text:
		index = ALPHABET.index(i) - key[abs(key_index) % key_sz]
		decoded.append((index))
		key_index -= 1

	return ''.join([ALPHABET[i] for i in decoded])


if __name__ == '__main__':
	while input('Continuar? (y/n) ').lower() == 'y':
		opt = input('Criptografar ou descriptografar? (c/d) ').lower()
		if opt == 'c':
			msg = input('Frase a ser criptografada: ')
			sz = int(input('Tamanho da chave: '))
			key = gen_key(sz)
			print('Resultado: ', encode(msg, key))
			print('Chave: ', str(key).strip(']['))
		elif opt == 'd':
			msg = input('Frase a ser descriptografada: ')
			key = list(map(int, input('Insira a chave: ').split(',')))
			print('Resultado: ', decode(msg, key))
		else:
			break
	frase = 'abortar operacao'
	chave = [11,7,9,3,4]
	codigo = encode(frase, chave)
	print(codigo)
	print(decode('MPHKCESEVGUGSRKVVECB', [0,7,5,3,2]))
