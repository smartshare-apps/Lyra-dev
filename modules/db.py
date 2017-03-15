import sqlite3

DEFAULT_db = "ecomm.db"
#DEFAULT_db = smartshare-core.chpryfodqoop.us-east-1.rds.amazonaws.com:3306

def db_handle():
	try:
		conn = sqlite3.connect(DEFAULT_db)
		conn.text_factory = str
	except Exception as e:
		print(e)
	return conn
