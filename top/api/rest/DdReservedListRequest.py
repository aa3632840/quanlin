'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class DdReservedListRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.buyer_phone = None
		self.ends = None
		self.option = None
		self.pn = None
		self.ps = None
		self.starts = None
		self.store_id = None

	def getapiname(self):
		return 'taobao.dd.reserved.list'
