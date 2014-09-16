'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class MediaFileGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_code = None
		self.dir_id = None
		self.end_date = None
		self.file_id = None
		self.name = None
		self.order_by = None
		self.page_no = None
		self.page_size = None
		self.start_date = None
		self.urls = None

	def getapiname(self):
		return 'taobao.media.file.get'
