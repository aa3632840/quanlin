'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SimbaCreativeUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.creative_id = None
		self.img_url = None
		self.nick = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.creative.update'
