'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TmallEaiOrderRefundMessageGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.refund_id = None
		self.refund_phase = None

	def getapiname(self):
		return 'tmall.eai.order.refund.message.get'
