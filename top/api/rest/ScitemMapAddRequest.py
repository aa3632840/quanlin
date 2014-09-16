'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class ScitemMapAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.need_check = None
		self.outer_code = None
		self.sc_item_id = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.scitem.map.add'
