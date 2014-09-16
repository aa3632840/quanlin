'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class UppShoppointDeductRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.point_num = None
		self.seller_nick = None
		self.transaction_id = None
		self.transaction_status = None
		self.transaction_time = None

	def getapiname(self):
		return 'taobao.upp.shoppoint.deduct'
