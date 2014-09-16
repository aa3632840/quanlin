'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class PromotionmiscMjsActivityGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None

	def getapiname(self):
		return 'taobao.promotionmisc.mjs.activity.get'
