'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class HotelSoldTypesIncrementGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.hotel.sold.types.increment.get'
