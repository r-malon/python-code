from socket import *
from sys import argv
#from time import sleep

def P2P(con_address, con_port, address, port):
	con_port = int(con_port)
	port = int(port)
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((address, port))
	sock.listen(2)
	#sleep(1)
	sock.connect((con_address, con_port))
	while True:
		clientsock, addr = sock.accept()
		ip, _ = addr
		msg = input("YOU: ")
		clientsock.send("Content-Type: text/*; encoding=utf8\nConnection: close\n" + msg.encode('ascii'))
		data = sock.recv(2048)
		if not data:
			break
		print(str(ip) + " says: " + data.decode('utf-8'))
		clientsock.close()
	sock.close()

if __name__ == '__main__':
	argv.remove(argv[0])
	P2P(*argv)