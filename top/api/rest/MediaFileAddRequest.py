'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class MediaFileAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_code = None
		self.dir_id = None
		self.ext = None
		self.file_data = None
		self.name = None

	def getapiname(self):
		return 'taobao.media.file.add'

	def getMultipartParas(self):
		return ['file_data']
