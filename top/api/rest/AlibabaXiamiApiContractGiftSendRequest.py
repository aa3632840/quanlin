'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class AlibabaXiamiApiContractGiftSendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.comefrom = None
		self.order_id = None
		self.relation_id = None
		self.shop_id = None
		self.type = None

	def getapiname(self):
		return 'alibaba.xiami.api.contract.gift.send'
