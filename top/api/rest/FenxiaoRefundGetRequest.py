'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoRefundGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.query_seller_refund = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.get'
