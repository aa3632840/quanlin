'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class QtReportsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.nick = None
		self.qt_type = None
		self.servcie_item_code = None
		self.sp_name = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.qt.reports.get'
