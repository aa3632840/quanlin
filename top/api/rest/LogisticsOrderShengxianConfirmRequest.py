'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class LogisticsOrderShengxianConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cancel_id = None
		self.delivery_type = None
		self.logis_id = None
		self.out_sid = None
		self.seller_ip = None
		self.sender_id = None
		self.service_code = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.order.shengxian.confirm'
