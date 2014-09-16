'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AlipayTopatsUserAccountreportGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.end_time = None
		self.fields = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'alipay.topats.user.accountreport.get'
