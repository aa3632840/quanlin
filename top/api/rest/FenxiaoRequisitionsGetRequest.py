'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoRequisitionsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.apply_end = None
		self.apply_start = None
		self.page_no = None
		self.page_size = None
		self.status = None

	def getapiname(self):
		return 'taobao.fenxiao.requisitions.get'