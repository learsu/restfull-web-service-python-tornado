#!/bin/env python
#coding = utf-8

import re

class Validate(object):
	"""docstring for Validate"""
	def _validate(self, data = {}, rule = {}):
		if len(rule) == 0:
			return data
		for key,value in rule.items():
			if data.has_key(key) == False:
				continue
			for fun_name, msg in value.items():
				fun_name += 'Valid'
				
				status = False
				try:
					status = getattr(self, fun_name)(data[key])
				except AttributeError:
					raise Exception(3, 'validate method don\'t exist')
				if status == False:
					raise Exception(msg['code'], msg['msg'])
			
	def isNotEmptyValid(self, strings):
		if not strings:
			return False
		else:
			return True
	def isUserNameValid(self, strings):
		if re.match(r"^[a-zA-Z][0-9a-zA-Z\-]{3,14}$", strings):
			return True
		else:
			return False