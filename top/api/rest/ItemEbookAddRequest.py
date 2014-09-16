'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class ItemEbookAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.copyright_end = None
		self.copyright_files = None
		self.cover = None
		self.desc = None
		self.isbn = None
		self.name = None
		self.outer_id = None
		self.price = None
		self.probation = None
		self.title = None

	def getapiname(self):
		return 'taobao.item.ebook.add'

	def getMultipartParas(self):
		return ['cover','copyright_files']
