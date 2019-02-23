from sqlalchemy_create import *

session = DBsession()

for client in session.query(Client).order_by(Client.name):
	print(client.id, client.name)