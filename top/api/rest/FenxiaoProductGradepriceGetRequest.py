'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoProductGradepriceGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None
		self.sku_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.fenxiao.product.gradeprice.get'
