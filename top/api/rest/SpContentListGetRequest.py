'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SpContentListGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.pagerequest = None
		self.query = None
		self.site_key = None

	def getapiname(self):
		return 'taobao.sp.content.list.get'
