import pymysql.cursors


def db_mng(firstname, lastname):
	connection = pymysql.connect(host='localhost',
		user='root',
		password='mali1995',
		db='fb',
		charset='utf8',
		cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql = 'INSERT INTO users (firstname, lastname) VALUES (%s, %s)'
			cursor.execute(sql, (firstname, lastname))
		connection.commit()

		with connection.cursor() as cursor:
			sql = 'SELECT id, firstname, lastname FROM users'
			cursor.execute(sql)
			results = cursor.fetchall()
	finally:
		connection.close()
	return results
