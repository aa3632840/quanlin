'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class TradeFullinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.fullinfo.get'
