#/usr/bin/python3
# insert SQL
#-------------------+-----------+-----------------------
# Variable 			| Type		| Description			
#-------------------+-----------+-----------------------
# __SQL				| string	| SQL statement
# __table_name		| string	| table's name
# __params			| dict		| values of insert
# __init__			| function	| Constructor function
# SQL 				| function	| return SQL statement
#-------------------+-----------+-----------------------

class insertSQL:
	__SQL = "INSERT INTO "
	__table_name = ""
	__params = {}

	def __init__(self, table_name, insert_params):
		self.__table_name = table_name
		self.__params = insert_params

	def SQL(self):
		SQL = self.__SQL + "`{}`".format(self.__table_name)
		columns = ""
		values = ""
		for i, p in enumerate(self.__params):
			if i != 0:
				columns += ", "
				values += ", "
			columns += "`{}`".format(p)
			if isinstance(self.__params[p], int):
				values += "{}".format(self.__params[p])
			elif isinstance(self.__params[p], str):
				values += "'{}'".format(self.__params[p])
		SQL += "({}) VALUES ({})".format(columns, values)
		return SQL

