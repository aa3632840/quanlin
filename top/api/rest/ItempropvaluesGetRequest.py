'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class ItempropvaluesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.attr_keys = None
		self.cid = None
		self.fields = None
		self.pvs = None
		self.type = None

	def getapiname(self):
		return 'taobao.itempropvalues.get'
