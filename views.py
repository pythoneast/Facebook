import re

from decorators import address
from helpers import send_response
from renderer import render
from db_manager import db_mng


@address('about')
def about_handler(request, conn, match=True, method=None):
	template = 'about.html'
	content = render(template)
	resp = """\
	HTTP/1.1 200 OK

	{}
	""".format(content)

	send_response(resp, conn, match)


@address('contacts')
def contact_handler(request, conn, match=True, method=None):
	template = 'contacts.html'
	if method == 'post':
		firstname = re.search(r'firstname=(\w+)', request).groups()[0]
		lastname = re.search(r'lastname=(\w+)', request).groups()[0]
		data = {
			'firstname': firstname,
			'lastname': lastname,
		}
		print(data)
		results = db_mng(firstname, lastname)
		print(results)
	content = render(template)
	resp = """\
	HTTP/1.1 200 OK

	{}
	""".format(content)

	send_response(resp, conn, match)
