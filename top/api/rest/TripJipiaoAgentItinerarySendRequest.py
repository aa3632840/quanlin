'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TripJipiaoAgentItinerarySendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.company_code = None
		self.express_code = None
		self.itinerary_id = None
		self.itinerary_no = None
		self.send_date = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.itinerary.send'
