'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AlipayEbppOweBillUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charge_inst = None
		self.chargeoff_inst = None
		self.digest_owe_bill = None
		self.order_type = None
		self.owe_bill = None
		self.sub_order_type = None

	def getapiname(self):
		return 'alipay.ebpp.owe.bill.upload'

	def getMultipartParas(self):
		return ['owe_bill']
