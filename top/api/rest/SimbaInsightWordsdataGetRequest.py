'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SimbaInsightWordsdataGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bidword_list = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.simba.insight.wordsdata.get'
