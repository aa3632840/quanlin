'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AitaobaoRealtimeReportGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.span = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.aitaobao.realtime.report.get'
