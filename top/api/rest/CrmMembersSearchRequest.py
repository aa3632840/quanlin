'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class CrmMembersSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.city = None
		self.current_page = None
		self.grade = None
		self.group_id = None
		self.max_avg_price = None
		self.max_close_trade_num = None
		self.max_item_num = None
		self.max_last_trade_time = None
		self.max_trade_amount = None
		self.max_trade_count = None
		self.min_avg_price = None
		self.min_close_trade_num = None
		self.min_item_num = None
		self.min_last_trade_time = None
		self.min_trade_amount = None
		self.min_trade_count = None
		self.page_size = None
		self.province = None
		self.relation_source = None

	def getapiname(self):
		return 'taobao.crm.members.search'
