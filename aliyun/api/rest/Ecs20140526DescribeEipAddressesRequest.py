'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from aliyun.api.base import RestApi
class Ecs20140526DescribeEipAddressesRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.AllocationId = None
		self.EipAddress = None
		self.PageNumber = None
		self.PageSize = None
		self.RegionId = None
		self.Status = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DescribeEipAddresses.2014-05-26'
