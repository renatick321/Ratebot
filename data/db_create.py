import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

try:
	cursor.execute("""CREATE TABLE User
			        (
			    	 user_id int NOT NULL,
			    	 dt datetime NOT NULL
			        )
			        """)
except:
	pass


try:
	cursor.execute("""CREATE TABLE Free
			        (
			    	 user_id int NOT NULL,
			    	 used boolean NOT NULL,
			    	 dt datetime NOT NULL
			        )
			        """)
except:
	pass