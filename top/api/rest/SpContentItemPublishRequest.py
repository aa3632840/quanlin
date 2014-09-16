'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SpContentItemPublishRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.classname = None
		self.comments = None
		self.coverpicurl = None
		self.detailurl = None
		self.item_id = None
		self.site_key = None
		self.tags = None
		self.title = None

	def getapiname(self):
		return 'taobao.sp.content.item.publish'
