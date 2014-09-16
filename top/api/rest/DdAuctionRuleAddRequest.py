'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class DdAuctionRuleAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.day_end = None
		self.day_start = None
		self.features = None
		self.is_diandian = None
		self.is_takeout = None
		self.name = None
		self.rule_end = None
		self.rule_start = None
		self.sort = None
		self.status = None
		self.store_id = None
		self.weeklys = None

	def getapiname(self):
		return 'taobao.dd.auction.rule.add'
