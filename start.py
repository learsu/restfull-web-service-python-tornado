#!/bin/env python
#coding = utf-8

import sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
import torndb

from tornado.options import define,options

define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="pay", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="123456", help="database password")

from service.test import TestGetHandler, TestListHandler

class MainHandler(tornado.web.RequestHandler):
	"""docstring for MainHandler"""
	def get(self):
		self.write("hello world, this is learsu test")

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(
			xsrf_cookies=True,
			debug=True,
		)
		handlers = [
			('/favicon.ico', tornado.web.ErrorHandler, dict(status_code=404)),
			(r"/", MainHandler),
			(r"/testget/([0-9]+)", TestGetHandler),
			(r"/test", TestListHandler),
		]
		self.db = torndb.Connection(
			host=options.mysql_host, database=options.mysql_database,
			user=options.mysql_user, password=options.mysql_password
		)
		super(Application,self).__init__(handlers,**settings)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	listen_port =  sys.argv[1]
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(listen_port)
	tornado.ioloop.IOLoop.instance().start()