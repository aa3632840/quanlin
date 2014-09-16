'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WaimaiShopUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address = None
		self.name = None
		self.phone = None
		self.pic_url = None
		self.posx = None
		self.posy = None
		self.shopid = None
		self.shopoutid = None

	def getapiname(self):
		return 'taobao.waimai.shop.update'
