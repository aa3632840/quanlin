'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderFailRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fail_memo = None
		self.fail_type = None
		self.order_id = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.fail'
