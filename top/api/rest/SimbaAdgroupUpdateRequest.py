'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SimbaAdgroupUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.default_price = None
		self.nick = None
		self.nonsearch_max_price = None
		self.online_status = None
		self.use_nonsearch_default_price = None

	def getapiname(self):
		return 'taobao.simba.adgroup.update'
