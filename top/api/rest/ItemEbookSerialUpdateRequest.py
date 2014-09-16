'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class ItemEbookSerialUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.author = None
		self.cid = None
		self.cover = None
		self.desc = None
		self.item_id = None
		self.name = None
		self.outer_id = None
		self.price = None
		self.relation_link = None
		self.title = None

	def getapiname(self):
		return 'taobao.item.ebook.serial.update'

	def getMultipartParas(self):
		return ['cover']
