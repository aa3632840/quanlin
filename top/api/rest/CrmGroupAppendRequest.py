'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class CrmGroupAppendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.from_group_id = None
		self.to_group_id = None

	def getapiname(self):
		return 'taobao.crm.group.append'