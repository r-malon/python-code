from socket import *
from threading import Thread

def accept(clientsock):
	while True:
		msg = input('YOU: ')
		clientsock.send(bytes(msg, 'utf-8'))
		#print("Connection from ", ip)
		data = clientsock.recv(2048)
		print('%s -' % ip, data.decode('utf-8'))
		if not data:
			break

def server(address, port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((address, port))
	sock.listen(10)
	while True:
		clientsock, addr = sock.accept()
		ip, _ = addr
		x = Thread(target=lambda: accept(clientsock))
		x.start()
		clientsock.shutdown(SHUT_WR)
		clientsock.close()
	sock.close()

if __name__ == '__main__':
	server('192.168.0.101', 5000)