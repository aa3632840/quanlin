'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class HotelRoomImgUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.gid = None
		self.pic = None
		self.position = None

	def getapiname(self):
		return 'taobao.hotel.room.img.upload'

	def getMultipartParas(self):
		return ['pic']
