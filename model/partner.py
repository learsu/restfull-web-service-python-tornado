# This Python file uses the following encoding: utf-8
#!/bin/env python
#coding = utf-8

from table import Table

class Partner(Table):
	"""docstring for Partner"""
	db = None
	_name = 'partner'
	_primary = 'id'

	def __init__(self, db):
		'''connect to database'''
		self.db = db