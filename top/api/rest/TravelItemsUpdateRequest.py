'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TravelItemsUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.add_combo_price_calendar = None
		self.approve_status = None
		self.auction_point = None
		self.choose_logis = None
		self.cid = None
		self.city = None
		self.combo_price_calendar = None
		self.desc = None
		self.duration = None
		self.empty_fields = None
		self.expirydate = None
		self.fee_include = None
		self.fee_not_include = None
		self.flight_info = None
		self.gathering_place = None
		self.has_discount = None
		self.has_invoice = None
		self.has_showcase = None
		self.hotel_info = None
		self.image = None
		self.input_pids = None
		self.input_str = None
		self.is_tdcy = None
		self.item_id = None
		self.merchant = None
		self.network_id = None
		self.num = None
		self.onsale_auto_refund_ratio = None
		self.order_info = None
		self.outer_id = None
		self.own_expense = None
		self.pic_path = None
		self.price = None
		self.props = None
		self.prov = None
		self.refund_ratio = None
		self.refund_regulation = None
		self.remove_combo_price_calendar = None
		self.remove_props = None
		self.second_kill = None
		self.seller_cids = None
		self.shoping_info = None
		self.sku_prices = None
		self.sku_properties = None
		self.sku_quantities = None
		self.sub_stock = None
		self.ticket_info = None
		self.title = None
		self.update_combo_price_calendar = None
		self.update_or_add_props = None
		self.verification = None

	def getapiname(self):
		return 'taobao.travel.items.update'

	def getMultipartParas(self):
		return ['image']
