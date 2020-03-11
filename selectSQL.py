# /usr/bin/python3
# select SQL
# author Dreammer12138
# -------------------+-----------+-----------------------
# Variable 			|Type		|Description			
# -------------------+-----------+-----------------------
# __SQL				|string		|SQL statement
# __column 			|list		|column for select
# __as_column		|list		|as
# __table_name		|string		|table's name
# __distinct		|bool		|Whether to remove duplicate data
# __where			|string		|condition
# __init__			|function	|Constructor function
# where 			|function	|condition function
# SQL 				|function	|return SQL statement
# -------------------+-----------+-----------------------

class selectSQL:
    __SQL = "SELECT "
    __column = []
    __as_column = []
    __table_name = ""
    __distinct = False
    __where = ""

    def __init__(self, table_name, attribute, distinct = False):
        self.__table_name = table_name
        if isinstance(attribute, str):
            self.__column.append(attribute)
        elif isinstance(attribute, list):
            self.__column += attribute
        elif isinstance(attribute, dict):
            for a in attribute:
                self.__column.append(a)
                self.__as_column.append(attribute[a])
        self.__distinct = distinct

    def where(self, wh):
        self.__where += wh

    def SQL(self):
        SQL = self.__SQL
        if self.__distinct:
            SQL += "DISTINCT "
        for index, c in enumerate(self.__column):
            if index != 0:
                SQL += ", "
            SQL += "`{}`".format(c)
        if self.__as_column:
            SQL += " AS "
            for index, a in enumerate(self.__as_column):
                if index != 0:
                    SQL += ", "
                SQL += "`{}`".format(a)
        SQL += " FROM `{}`".format(self.__table_name)
        if self.__where != "":
            SQL += self.__where
        return SQL
