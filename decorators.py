import re


def address(path):
	def wrapper(func):
		def wrap_func(*args, **kwargs):
			request = args[0]
			match_object = re.search(r'GET\s\/(\w+)|POST\s\/(\w+)', request).groups()
			if path == match_object[0] or path == match_object[1]:
				kwargs['method'] = 'post' if match_object[1] else 'get'
				func(*args, **kwargs)
			else:
				kwargs['match'] = False
				func(*args, **kwargs)

		return wrap_func
	return wrapper

"""
	{
		'firstname': 'Aktanbek',
		'lastname': 'Semenovna'
	}
"""