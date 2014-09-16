'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class JipiaoPoliciesstatusUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.airline = None
		self.arr_airport = None
		self.dep_airport = None
		self.out_product_ids = None
		self.policy_ids = None
		self.publish_date = None
		self.source = None
		self.type = None

	def getapiname(self):
		return 'taobao.jipiao.policiesstatus.update'
