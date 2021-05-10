import sqlite3
from config import DB_URL, format_
import datetime


conn = sqlite3.connect(DB_URL)
cursor = conn.cursor()

def user_save(user_id, days=30):
	if is_exist(user_id):
		for i in cursor.execute("SELECT dt FROM User WHERE user_id = {}".format(user_id)):
			dt = i[0]
		date = datetime.timedelta(days=days) + datetime.datetime.strptime(dt, format_)
		cursor.execute("UPDATE User SET dt = ? WHERE user_id = ?", (date.strftime(format_), user_id))
	else:
		date = datetime.timedelta(days=days) + datetime.datetime.now()
		cursor.execute("INSERT INTO User(user_id, dt) VALUES (?, ?)", (user_id, date.strftime(format_)))
	conn.commit()


def user_del(user_id):
	cursor.execute("DELETE FROM User WHERE user_id = {}".format(user_id))
	conn.commit()


def is_exist(user_id):
	for i in cursor.execute("SELECT * FROM User WHERE user_id = {}".format(user_id)):
		return True
	return False


def get_users():
	users = []
	for i in cursor.execute("SELECT user_id, dt FROM User"):
		data = {}
		data[str(i[1])] = i[0]
		users.append(data)
	free = []
	for i in cursor.execute("SELECT user_id, dt FROM Free"):
		data = {}
		data[str(i[1])] = i[0]
		free.append(data)
	users += free
	users_ = []
	while users:
		i = users[0]
		index = -1
		for j in range(1, len(users)):
			if list(i.values())[0] == list(users[j].values())[0]:
				date = max(datetime.datetime.strptime(list(i.keys())[0], format_), datetime.datetime.strptime(list(users[j].keys())[0], format_)).strftime(format_)
				d = {}
				d[str(list(i.keys())[0])] = list(i.values())[0]
				users_.append(d)
				index = j
				break
		else:
			d = {}
			d[list(i.keys())[0]] = list(i.values())[0]
			users_.append(d)
		if index != -1:
			del users[index]
		del users[0]
	return users_


def get_free(user_id):
	bl = False
	for i in cursor.execute("SELECT used FROM Free"):
		bl = i[0]
	if bl:
		return False
	else:
		date = datetime.timedelta(minutes=60) + datetime.datetime.now()
		cursor.execute("INSERT INTO Free(user_id, dt, used) VALUES (?, ?, ?)", (user_id, date.strftime(format_), True))
		conn.commit()
		return True