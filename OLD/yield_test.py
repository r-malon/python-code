def createGenerator():
	mylist = range(5)
	for i in mylist:
		yield i * i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
	print(i)