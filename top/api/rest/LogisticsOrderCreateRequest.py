'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class LogisticsOrderCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.goods_names = None
		self.goods_quantities = None
		self.is_consign = None
		self.item_values = None
		self.logis_company_code = None
		self.logis_type = None
		self.mail_no = None
		self.receiver_address = None
		self.receiver_mobile_phone = None
		self.receiver_name = None
		self.receiver_telephone = None
		self.receiver_zip_code = None
		self.seller_wangwang_id = None
		self.sender_address = None
		self.sender_mobile_phone = None
		self.sender_name = None
		self.sender_telephone = None
		self.sender_zip_code = None
		self.shipping = None
		self.trade_id = None

	def getapiname(self):
		return 'taobao.logistics.order.create'
