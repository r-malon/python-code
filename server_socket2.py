from socket import *
from threading import Thread

def accept():
	while True:
		clientsock, addr = sock.accept()
		ip, _ = addr
		msg = input('YOU: ')
		clientsock.send(bytes(msg, 'utf-8'))
		#print("Connection from ", ip)
		data = clientsock.recv(2048)
		print('%s -' % ip, data.decode('utf-8'))
		if not data:
			break
		clientsock.shutdown(SHUT_WR)
		clientsock.close()

def server(address, port):
	global sock
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((address, port))
	sock.listen(5)
	while True:
		x = Thread(target=accept)
		try:
			x.start()
		except OSError:
			return False
		x.join()
	sock.close()

if __name__ == '__main__':
	server('192.168.0.101', 5000)