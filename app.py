import re
import socket
from views import about_handler, contact_handler


HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s' % PORT)

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	request_string = str(request)
	print(request_string)
	about_handler(request_string, client_connection)
	contact_handler(request_string, client_connection)
