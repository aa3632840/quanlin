'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class PromotionmiscItemActivityAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.decrease_amount = None
		self.discount_rate = None
		self.end_time = None
		self.is_decrease_money = None
		self.is_discount = None
		self.is_user_tag = None
		self.name = None
		self.participate_range = None
		self.start_time = None
		self.user_tag = None

	def getapiname(self):
		return 'taobao.promotionmisc.item.activity.add'
