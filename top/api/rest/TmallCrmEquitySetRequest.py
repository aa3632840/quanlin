'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TmallCrmEquitySetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.exclude_area = None
		self.grade = None
		self.point = None
		self.postage = None

	def getapiname(self):
		return 'tmall.crm.equity.set'
