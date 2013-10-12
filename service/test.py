#!/bin/env python
#coding = utf-8

import tornado.web
import json
from model.test import Test

class TestGetHandler(tornado.web.RequestHandler):
	"""docstring for TestGetHandler"""

	def get(self, id):
		try:
			id = int(id) 
		except ValueError:
			id = 0
		try:
			test = Test(self.application.con)
			b=test.get(id)
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")
		except Exception, e:
			#self.write(e[1].decode("utf8")+"<br>")
			self.write(str(e)+"<br>")
			#a = {'msg':e[0], 'code':e[1]}
			#self.write(json.dumps(a)+"<br>")

class TestListHandler(tornado.web.RequestHandler):
	def get(self):
		try:
			self.application.cursor()
			test = Test(self.application.con, self.application.cursor)

			b=test.get(1)
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")
			self.write("++++++++++++++++++++++++++++get+++++++++++++++++++++++++++++<br>")

			b = test.find(where = '`id` > 1', fields = ['id', 'name'], order = '`id` desc', limit = '10')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")
			self.write("++++++++++++++++++++++++++++find+++++++++++++++++++++++++++++<br>")

			b = test.find(where = '`id` > 1', fields = ['id', 'name'], order = '`id` desc', limit = '10, 4')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")
			self.write("++++++++++++++++++++++++++++++find+++++++++++++++++++++++++++<br>")

			b = test.find(where = '`id` > 1', fields = ['id', 'name'], order = '`id` desc')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")
			self.write("++++++++++++++++++++++++++++++fetch+++++++++++++++++++++++++++<br>")

			data = {'name': 'python', 'pwd': '123456'}
			b = test.insert(data)
			self.write(str(b)+" insert<br>")
			self.write("++++++++++++++++++++++++++++++insert+++++++++++++++++++++++++++<br>")

			data = {'name': 'aaaaa', 'pwd': '123456'}
			b = test.update(data)
			self.write(str(b)+" update<br>")
			self.write("+++++++++++++++++++++++++++++update++++++++++++++++++++++++++++<br>")

			status = test.commit()
			self.write(str(status)+" commit<br>")
			self.write("++++++++++++++++++++++++++++++++commit+++++++++++++++++++++++++<br>")

			b = test.update(data, 'id = 1', 0)
			self.write(str(b)+" update<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

			b = test.update(data, '`id` = 2', 1)
			self.write(str(b)+" update<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

			b = test.update(data, '`id` > 2')
			self.write(str(b)+" update<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

			b = test.delete('`id` > 10')
			self.write(str(b)+" delete<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

			b = test.delete('`id` > 10', 1)
			self.write(str(b)+" delete<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

			b = test.deld(10)
			self.write(str(b)+" deld<br>")
			self.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>")

		except Exception, e:
			self.write(e[1].decode("utf8")+"<br>")
			self.write(str(e)+"<br>")
			a = {'msg':e[0], 'code':e[1]}
			self.write(json.dumps(a)+"<br>")