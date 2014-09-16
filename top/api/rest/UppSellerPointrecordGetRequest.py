'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class UppSellerPointrecordGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.page_size = None
		self.status = None
		self.transaction_id = None
		self.transaction_time_begin = None
		self.transaction_time_end = None
		self.type = None

	def getapiname(self):
		return 'taobao.upp.seller.pointrecord.get'
