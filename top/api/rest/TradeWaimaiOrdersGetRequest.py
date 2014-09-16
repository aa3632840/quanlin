'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TradeWaimaiOrdersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_all_order = None
		self.is_all_shop = None
		self.keyword = None
		self.order_status = None
		self.page_no = None
		self.page_size = None
		self.shop_id = None

	def getapiname(self):
		return 'taobao.trade.waimai.orders.get'
