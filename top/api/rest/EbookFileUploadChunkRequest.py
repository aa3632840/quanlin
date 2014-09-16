'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class EbookFileUploadChunkRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.chunk_count = None
		self.chunk_data = None
		self.chunk_md5 = None
		self.file_id = None
		self.file_name = None
		self.file_size = None
		self.sequence = None

	def getapiname(self):
		return 'taobao.ebook.file.upload.chunk'

	def getMultipartParas(self):
		return ['chunk_data']
