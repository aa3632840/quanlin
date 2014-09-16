'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from aliyun.api.base import RestApi
class Ecs20130110ModifyInstanceAttributeRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.HostName = None
		self.InstanceId = None
		self.InstanceName = None
		self.Password = None
		self.SecurityGroupId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyInstanceAttribute.2013-01-10'
