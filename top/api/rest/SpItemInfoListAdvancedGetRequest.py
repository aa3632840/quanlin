'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SpItemInfoListAdvancedGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.cid = None
		self.end_commission_rate = None
		self.end_credit = None
		self.end_price = None
		self.keyword = None
		self.page_no = None
		self.page_size = None
		self.site_key = None
		self.sort = None
		self.start_commission_rate = None
		self.start_credit = None
		self.start_price = None
		self.tmall_item = None

	def getapiname(self):
		return 'taobao.sp.item.info.list.advanced.get'
