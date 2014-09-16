'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class EbookmediaChapterAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auction_id = None
		self.book_price = None
		self.content = None
		self.content_url = None
		self.cp_cid = None
		self.is_free = None
		self.pre_tbid = None
		self.price_count = None
		self.status = None
		self.title = None
		self.volume_id = None
		self.word_count = None

	def getapiname(self):
		return 'taobao.ebookmedia.chapter.add'
