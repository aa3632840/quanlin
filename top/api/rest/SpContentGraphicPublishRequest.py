'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SpContentGraphicPublishRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.classname = None
		self.contents = None
		self.coverpicurl = None
		self.detailurl = None
		self.intimeline = None
		self.site_key = None
		self.tags = None
		self.title = None

	def getapiname(self):
		return 'taobao.sp.content.graphic.publish'
