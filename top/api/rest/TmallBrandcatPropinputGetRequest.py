'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class TmallBrandcatPropinputGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.brand_id = None
		self.cid = None
		self.pid = None

	def getapiname(self):
		return 'tmall.brandcat.propinput.get'