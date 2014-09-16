'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class JuCatitemidsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.child_categoryid = None
		self.city = None
		self.page_no = None
		self.page_size = None
		self.parent_categoryid = None
		self.platform_id = None
		self.terminal_type = None

	def getapiname(self):
		return 'taobao.ju.catitemids.get'
