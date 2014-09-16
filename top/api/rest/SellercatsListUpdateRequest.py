'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SellercatsListUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.name = None
		self.pict_url = None
		self.sort_order = None

	def getapiname(self):
		return 'taobao.sellercats.list.update'
