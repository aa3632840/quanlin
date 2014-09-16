'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AitaobaoItemsRelateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.fields = None
		self.max_count = None
		self.num_iid = None
		self.relate_type = None
		self.seller_id = None
		self.shop_type = None
		self.sort = None
		self.track_iid = None

	def getapiname(self):
		return 'taobao.aitaobao.items.relate.get'
