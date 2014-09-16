'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FavoriteSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.collect_type = None
		self.page_no = None

	def getapiname(self):
		return 'taobao.favorite.search'
