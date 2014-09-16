'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoDealerRequisitionorderModifyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dealer_order_id = None
		self.delete_detail_ids = None
		self.detail_id_prices = None
		self.detail_id_quantities = None
		self.new_post_fee = None

	def getapiname(self):
		return 'taobao.fenxiao.dealer.requisitionorder.modify'
