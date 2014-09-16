'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class WaimaiItemPicUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.picbytes = None

	def getapiname(self):
		return 'taobao.waimai.item.pic.upload'

	def getMultipartParas(self):
		return ['picbytes']
