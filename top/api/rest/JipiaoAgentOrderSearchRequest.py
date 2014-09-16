'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class JipiaoAgentOrderSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.begin_time = None
		self.end_time = None
		self.has_itinerary = None
		self.page = None
		self.status = None
		self.trip_type = None

	def getapiname(self):
		return 'taobao.jipiao.agent.order.search'
