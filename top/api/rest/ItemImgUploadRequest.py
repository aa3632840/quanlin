'''
Created by auto_sdk on 2014-09-08 16:48:01
'''
from top.api.base import RestApi
class ItemImgUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.image = None
		self.is_major = None
		self.num_iid = None
		self.position = None

	def getapiname(self):
		return 'taobao.item.img.upload'

	def getMultipartParas(self):
		return ['image']