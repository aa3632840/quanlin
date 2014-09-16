'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SpItemListGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.cid = None
		self.end_biz30day = None
		self.end_commission_rate = None
		self.end_credit = None
		self.end_price = None
		self.hdfk = None
		self.jyps = None
		self.keyword = None
		self.myf = None
		self.page_no = None
		self.page_size = None
		self.qtth = None
		self.site_key = None
		self.sort = None
		self.start_biz30day = None
		self.start_commission_rate = None
		self.start_credit = None
		self.start_price = None
		self.tmall_item = None
		self.xfzbz = None
		self.zpbz = None

	def getapiname(self):
		return 'taobao.sp.item.list.get'
