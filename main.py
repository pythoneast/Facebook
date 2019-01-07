import re
import socket


HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s' % PORT)

def send_response(resp, conn, match):
	if match:
		conn.sendall(resp.encode())
		conn.close()


def address(path):
	def wrapper(func):
		def wrap_func(*args, **kwargs):
			request = args[0]
			match_object = re.search(r'GET\s/(\w+)', request).groups()
			print(match_object[0])
			if path == match_object[0]:
				func(*args, **kwargs)
			else:
				kwargs['match'] = False
				func(*args, **kwargs)

		return wrap_func
	return wrapper


@address('about')
def about_handler(request, conn, match=True):
	resp = """\
	HTTP/1.1 200 OK

	'This is about page'
	"""
	send_response(resp, conn, match)


@address('contacts')
def contact_handler(request, conn, match=True):
	resp = """\
	HTTP/1.1 200 OK

	'This is contact page'
	"""
	send_response(resp, conn, match)


while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print(request)
	request_string = str(request)

	about_handler(request_string, client_connection)
	contact_handler(request_string, client_connection)
