'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class LogisticsOrderstorePushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_split = None
		self.occure_time = None
		self.operate_detail = None
		self.operator_contact = None
		self.operator_name = None
		self.sub_tid = None
		self.trade_id = None

	def getapiname(self):
		return 'taobao.logistics.orderstore.push'
