#!/bin/env python
#coding = utf-8

version = "1.0 beta"

class testb(object):
	"""docstring for test"""

	def test(self):
		testc().test()
		print "this is testb test"

	
class testc(object):
	def test(self):
		print "this is testc test"
	
