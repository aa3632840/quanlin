'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoRefundUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_return_goods = None
		self.refund_desc = None
		self.refund_reason_id = None
		self.return_fee = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.update'
