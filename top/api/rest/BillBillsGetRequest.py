'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class BillBillsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.account_id = None
		self.end_time = None
		self.fields = None
		self.order_id = None
		self.page_no = None
		self.page_size = None
		self.start_time = None
		self.time_type = None
		self.trade_id = None

	def getapiname(self):
		return 'taobao.bill.bills.get'
