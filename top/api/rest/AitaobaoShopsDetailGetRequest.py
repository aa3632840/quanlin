'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AitaobaoShopsDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.seller_nicks = None
		self.sids = None

	def getapiname(self):
		return 'taobao.aitaobao.shops.detail.get'
