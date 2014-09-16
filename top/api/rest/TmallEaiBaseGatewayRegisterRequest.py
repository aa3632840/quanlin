'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TmallEaiBaseGatewayRegisterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.call_back_url = None
		self.char_set = None
		self.city = None
		self.content_type = None
		self.description = None
		self.district = None
		self.email = None
		self.max_flow = None
		self.mobile = None
		self.notify_type = None
		self.principal = None
		self.telephone = None
		self.topic = None
		self.topic_group = None
		self.url_protocal = None
		self.user_type = None

	def getapiname(self):
		return 'tmall.eai.base.gateway.register'
