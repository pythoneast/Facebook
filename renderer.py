def render(file_name):
	with open(file_name, 'r') as html_file:
		html = html_file.read()
		return html
