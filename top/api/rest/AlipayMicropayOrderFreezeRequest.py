'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AlipayMicropayOrderFreezeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.amount = None
		self.auth_token = None
		self.expire_time = None
		self.memo = None
		self.merchant_order_no = None
		self.pay_confirm = None

	def getapiname(self):
		return 'alipay.micropay.order.freeze'
