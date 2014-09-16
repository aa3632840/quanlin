'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TbkItemsConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.nick = None
		self.num_iids = None
		self.outer_code = None
		self.pid = None
		self.refer_type = None
		self.track_iids = None

	def getapiname(self):
		return 'taobao.tbk.items.convert'
