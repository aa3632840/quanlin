'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class ItemEbookUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cover = None
		self.desc = None
		self.item_id = None
		self.outer_id = None
		self.price = None
		self.probation = None
		self.title = None

	def getapiname(self):
		return 'taobao.item.ebook.update'

	def getMultipartParas(self):
		return ['cover']
