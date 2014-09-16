'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from aliyun.api.base import RestApi
class Mts20140618CreateTranscodeJobRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.MediaId = None
		self.TemplateId = None

	def getapiname(self):
		return 'mts.aliyuncs.com.CreateTranscodeJob.2014-06-18'
