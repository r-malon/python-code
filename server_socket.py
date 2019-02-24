from socket import *

def serve():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(('localhost', 9000))
	sock.listen(3)
	while True:
		clientsock, addr = sock.accept()
		ip, _ = addr
		print("Connection from: " + str(ip))
		#msg = input('Say: ')
		clientsock.send(b"HTTP/1.1 200 OK\n"
         + b"Content-Type: text/html\n\n"
         + b"<html><body><h1 style='color: red;'>Hello world</h1></body></html>\n")
         #open(r"C:\Users\RAFAEL\Videos\Site_PI\app\templates\index.html",'r')
		clientsock.shutdown(SHUT_WR)
		clientsock.close()
	sock.close()

if __name__ == '__main__':
	serve()