'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WlbItemSynchronizeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext_entity_id = None
		self.ext_entity_type = None
		self.item_id = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.wlb.item.synchronize'
