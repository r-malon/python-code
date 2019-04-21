from socket import *
from threading import Thread

def client(address, port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((address, port)) #0.0.0.0 isnt valid
	while True:
		data = sock.recv(2048)
		print('%s -' % address, data.decode('utf-8'))
		msg = input('YOU: ')
		sock.send(bytes(msg, 'utf-8'))
	sock.close()
	#return "Received data: \n" + data.decode('utf-8')

if __name__ == '__main__':
	#x = Thread(target=lambda: client('192.168.0.101', 5000))
	#x.start()
	client('192.168.10.199', 5000)