'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class ItemrecommendItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.item_id = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.itemrecommend.items.get'
