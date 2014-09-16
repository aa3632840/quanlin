'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AitaobaoShopsRelateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.max_count = None
		self.seller_id = None
		self.seller_nick = None
		self.shop_type = None
		self.sort = None

	def getapiname(self):
		return 'taobao.aitaobao.shops.relate.get'
