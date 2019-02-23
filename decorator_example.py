def dec(func):
	def wrap():
		print('before')
		func()
		print('after!')
	return wrap

@dec
def my_func():
	print('I said hey!')
	return 15

my_func('bla')