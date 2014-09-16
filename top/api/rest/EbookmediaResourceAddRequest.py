'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class EbookmediaResourceAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auction_id = None
		self.file_id = None
		self.str_file_id = None
		self.suffix = None
		self.type = None

	def getapiname(self):
		return 'taobao.ebookmedia.resource.add'
