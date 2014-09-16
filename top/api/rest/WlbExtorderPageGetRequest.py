'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WlbExtorderPageGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.ext_order_code = None
		self.ext_order_source = None
		self.ext_order_status = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.wlb.extorder.page.get'
