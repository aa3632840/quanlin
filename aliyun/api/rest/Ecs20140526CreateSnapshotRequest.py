'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from aliyun.api.base import RestApi
class Ecs20140526CreateSnapshotRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ClientToken = None
		self.Description = None
		self.DiskId = None
		self.SnapshotName = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.CreateSnapshot.2014-05-26'
