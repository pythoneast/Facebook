def send_response(resp, conn, match):
	if match:
		conn.sendall(resp.encode())
		conn.close()
