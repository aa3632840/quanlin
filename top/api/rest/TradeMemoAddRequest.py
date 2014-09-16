'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class TradeMemoAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.flag = None
		self.memo = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.memo.add'
