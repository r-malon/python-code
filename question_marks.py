def qmark(x):
	num_list = []
	for i in x:
		if i.isdigit():
			num_list.append(x.index(i))
			print(x.index(i))
	for i in range(0, len(num_list), 2):
		#if '?' in x[num_list[i]:num_list[i+2]]:
		if x[num_list[i]:num_list[i+2]].count('?') != 3 and '?' in x[num_list[i]:num_list[i+2]]:
			return False
	return True

if __name__ == '__main__':
	print(qmark("arrb6???4xxbl5???eee5"))
	print(qmark("5??aaaaaaaaaaaaaaaaaaa?5?5"))
	print(qmark("acc?7??sss?3rr1??????5"))