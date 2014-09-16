'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class ItemEbookSerialAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.author = None
		self.cid = None
		self.copyright_end = None
		self.copyright_files = None
		self.cover = None
		self.desc = None
		self.name = None
		self.outer_id = None
		self.price = None
		self.relation_link = None
		self.sell_way = None
		self.title = None

	def getapiname(self):
		return 'taobao.item.ebook.serial.add'

	def getMultipartParas(self):
		return ['cover','copyright_files']
