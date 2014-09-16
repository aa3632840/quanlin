'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class UppShoppointPresendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.business_info = None
		self.buyer_nick = None
		self.point_num = None
		self.transaction_time = None

	def getapiname(self):
		return 'taobao.upp.shoppoint.presend'
