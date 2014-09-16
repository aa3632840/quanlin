'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WeitaoFeedIsrelationRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fans_nick = None
		self.seller_nick = None

	def getapiname(self):
		return 'taobao.weitao.feed.isrelation'
