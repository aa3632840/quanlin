'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoProductSkuAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.agent_cost_price = None
		self.dealer_cost_price = None
		self.product_id = None
		self.properties = None
		self.quantity = None
		self.sku_number = None
		self.standard_price = None

	def getapiname(self):
		return 'taobao.fenxiao.product.sku.add'
