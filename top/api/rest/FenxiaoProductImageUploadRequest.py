'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class FenxiaoProductImageUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image = None
		self.pic_path = None
		self.position = None
		self.product_id = None
		self.properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.image.upload'

	def getMultipartParas(self):
		return ['image']
