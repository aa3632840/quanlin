'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TbkItemsDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iids = None
		self.track_iids = None

	def getapiname(self):
		return 'taobao.tbk.items.detail.get'
