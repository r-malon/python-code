from sqlalchemy_create import *

session = DBsession()

n = int(input("How many clients will you register? "))
for i in range(n):
	client_name = input("Type your name: ")
	session.add(Client(name=client_name))

session.commit()