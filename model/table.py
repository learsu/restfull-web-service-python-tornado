#!/bin/env python
#coding = utf-8

from validate import Validate

class Table():
	'''docstring for Table'''
	db = None
	_name = ''
	_primary = ''
	_dataValidate = {}
	
	
	def get(self, id = 0):
		'''retrieve only one record by primary key'''
		sql = 'select * from ' + self._name + ' where ' + self._primary + " ='" + str(id) + "'"
		return self.db.get(sql)

	def find(self, where = '', fields = [], order = '', limit = ''):
		'''retrieve data from table by where clause'''
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if fields :
			field = '`' + "`, `".join(fields) + '`'
		else :
			field = "*"
		if not order:
			order = ''
		else:
			order = ' order by ' + order
		if not limit:
			limit = ' limit 200'
		else:
			limit = ' limit ' + limit
		sql = 'select ' + field + ' from ' + self._name + where + order + limit

		return self.db.query(sql)

	def fetch(self, where = '', fields = [], order = ''):
		'''retrieve only one record by where clause'''
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if fields :
			field = '`' + "`, `".join(fields) + '`'
		else :
			field = "*"
		if not order:
			order = ''
		else:
			order = ' order by ' + order
		limit = ' limit 1'
		sql = 'select ' + field + ' from ' + self._name + where + order + limit

		return self.db.get(sql)

	def insert(self, data = {}):
		'''add record'''
		#check and validate data
		validate = Validate()
		validate._validate(data, self._dataValidate)

		fields = ''
		values = ''
		for key,value in data.items():
			fields = fields + "`" + key + "`, "
			values = values + "'" + value + "', "
		fields = fields[:-2]
		values = values[:-2]
		sql = 'insert into '+ self._name +' (' + fields + ') values (' + values + ')'

		return self.db.execute_lastrowid(sql)

	def update(self, data = {}, where = "", flag = 0):
		'''update record'''
		#check and validate data
		validate = Validate()
		validate._validate(data, self._dataValidate)

		fields = ''
		for key,value in data.items():
			fields = fields + "`" + key + "` = '" + value + "', "
		fields = fields[:-2]
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if flag == 0:
			limit = ' limit 200'
		else:
			limit = ''
		sql = 'update '+ self._name +' set ' + fields + where + limit

		return self.db.execute(sql)

	def save(self, data = {}, id = 0):
		'''update record by primary'''
		#check and validate data
		validate = Validate()
		validate._validate(data, self._dataValidate)
		
		fields = ''
		for key,value in data.items():
			fields = fields + "`" + key + "` = '" + value + "', "
		fields = fields[:-2]
		if id == 0:
			where = ' limit 1'
		else:
			where = ' where ' + self._primary + " ='" + str(id) + "'"
		sql = 'update '+ self._name +' set ' + fields + where

		return self.db.execute(sql)

	def delete(self, where = '', flag = 0):
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if flag == 0:
			limit = ' limit 200'
		else:
			limit = ''
		sql = 'delete from '+ self._name + where + limit

		return self.db.execute(sql)

	def deld(self, id = 0):
		if id == 0:
			where = ' limit 1'
		else:
			where = ' where ' + self._primary + " ='" + str(id) + "'"
		sql = 'delete from '+ self._name + where

		return self.db.execute(sql)