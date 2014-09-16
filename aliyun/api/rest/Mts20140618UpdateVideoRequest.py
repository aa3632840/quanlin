'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from aliyun.api.base import RestApi
class Mts20140618UpdateVideoRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.CoverUrl = None
		self.Description = None
		self.MediaId = None
		self.Tags = None
		self.Title = None

	def getapiname(self):
		return 'mts.aliyuncs.com.UpdateVideo.2014-06-18'
