'''
Write a solution that will return the numbers of ways
you can sum to n using no more than any two numbers in the form of 2^n
(i.e. for n=10, you can use at most 2x1, 2x2, 2x4, 2x8)

Order doesn't count.

Examples:

5 -> 2 ([4+1], [2+2+1])
10 -> 5 ([8+2], [8+1+1], [4+4+2], [4+2+2+1+1], [4+4+1+1])
47 -> 2 ([32+8+4+2+1], [16+16+8+4+2+1])
'''

from random import randrange

def shift(n):
	arr = []
	for i in range(1, n):
		shifted = n >> i
		if not shifted:
			break
		print(shifted)
		arr.append(shifted)
	arr.append(n - sum(arr))
	return arr

if __name__ == '__main__':
	print(shift(randrange(15, 100000)))
