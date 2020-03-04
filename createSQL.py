#!/usr/bin/python3
# create SQL
# author Dreammer12138
# ------------------+-----------+------------------------
# Variable 		   |Type	   |Description			
# ------------------+-----------+------------------------
# __SQL: 		   |string	   |SQL statement
# columns:		   |list	   |is table's columns
# table_name:	   |string	   |table's name
# database_name:   |string	   |database's name
# __init__:		   |function   |Constructor function
# add_column:	   |function   |add a new column
# del_column:	   |function   |delete a column
# update_column:   |function   |update an existing column
# SQL:			   |function   |return SQL statement
# ------------------+-----------+-------------------------

class Data_Table:
    __SQL = ""
    columns = []
    table_name = ""
    database_name = ""

    def __init__(self, database_name, table_name):
        self.__SQL = "CREATE TABLE `{}`.`{}`".format(database_name, table_name)

    def add_column(self, column_name, variable_type, is_NULL=True, Default="", is_primarykey=False):
        column = {
            'name': column_name,
            'variable_type': variable_type,
            'is_NULL': is_NULL,
            'Default': Default,
            'is_primarykey': is_primarykey
        }
        self.columns.append(column)

    def del_column(self, column_name):
        for index, column in enumerate(self.columns):
            if column_name == column['name']:
                del self.columns[index]

    def update_column(self, column_name, variable_type=None, is_NULL=None, Default=None, is_primarykey=None):
        for column in self.columns:
            if column_name == column['name']:
                if variable_type is not None:
                    column['variable_type'] = variable_type
                if is_NULL is not None:
                    column['is_NULL'] = is_NULL
                if Default is not None:
                    column['Default'] = Default
                if is_primarykey is not None:
                    column['is_primarykey'] = is_primarykey

    def SQL(self):
        columns = "({})"
        column = ""
        for c in self.columns:
            if column != "":
                column += ","
            column += "`{}` {} ".format(c['name'], c['variable_type'])
            if not c['is_NULL']:
                column += "NOT NULL "
            else:
                column += "NULL "
            if c['Default'] != "":
                column += "DEFAULT `{}`".format(c['Default'])
            if c['is_primarykey']:
                column += "PRIMARY KEY "
        self.__SQL = self.__SQL + columns.format(column)
        return self.__SQL
