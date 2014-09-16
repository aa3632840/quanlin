'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AitaobaoItemsBuyConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buy_now = None
		self._from = None
		self.open_iid = None
		self.pid = None
		self.quantity = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.aitaobao.items.buy.convert'

	def getTranslateParas(self):
		return {'_from':'from'}
