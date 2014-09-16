'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WeitaoCloudtagsGroupGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.status = None

	def getapiname(self):
		return 'taobao.weitao.cloudtags.group.get'
