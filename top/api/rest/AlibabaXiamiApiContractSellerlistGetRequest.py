'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AlibabaXiamiApiContractSellerlistGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.page = None
		self.time_end = None
		self.time_start = None

	def getapiname(self):
		return 'alibaba.xiami.api.contract.sellerlist.get'
