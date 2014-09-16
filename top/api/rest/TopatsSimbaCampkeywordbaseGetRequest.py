'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class TopatsSimbaCampkeywordbaseGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.search_type = None
		self.source = None
		self.time_slot = None

	def getapiname(self):
		return 'taobao.topats.simba.campkeywordbase.get'
