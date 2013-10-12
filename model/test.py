# This Python file uses the following encoding: utf-8
#!/bin/env python
#coding = utf-8

from table import Table

class Test(Table):
	"""docstring for Test"""
	_name = 'test'
	_primary = 'id'
	_dataValidate = {
		'name':{
			'isNotEmpty':{'msg':'密码不能为空', 'code':1001},
			'isUserName':{'msg':'用户名不符合规则', 'code':1002},
		},
		'pwd':{
			'isNotEmpty':{'msg':'密码不能为空', 'code':1003},
		},
	}

	def __init__(self, db):
		'''connect to database'''
		self.db = db

	def commit(self):
		try:
			sql = [
				"update test set pwd = 'aaaaa' where id = 1",
				"insert test(name, pwd) values('aaaaaa', '123456')", 
				"insert partner(`member_id`, `partner`, `key`) values(1, 'aaaaa', '123456')"
			]
			status = self.db.transaction(sql)
			return status
		except Exception, e:
			return e