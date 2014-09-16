'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SimbaKeywordsvonAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.keyword_prices = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.keywordsvon.add'
