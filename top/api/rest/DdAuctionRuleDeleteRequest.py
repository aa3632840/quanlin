'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class DdAuctionRuleDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.is_takeout = None
		self.store_id = None

	def getapiname(self):
		return 'taobao.dd.auction.rule.delete'
