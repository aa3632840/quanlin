'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class InventoryOccupyAdjustRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_unique_code = None
		self.items = None
		self.operate_time = None
		self.tb_order_type = None

	def getapiname(self):
		return 'taobao.inventory.occupy.adjust'
