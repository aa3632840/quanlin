'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TripJipiaoNsearchOwSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.arr_city_code = None
		self.cabin_class = None
		self.dep_city_code = None
		self.dep_date = None
		self.flight_no = None
		self.passenger_num = None
		self.pid = None
		self.search_type = None
		self.supply_itinerary = None

	def getapiname(self):
		return 'taobao.trip.jipiao.nsearch.ow.search'
