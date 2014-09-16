'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class JushitaJdpTaskUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.error_message = None
		self.execute_host = None
		self.id = None
		self.next_execute_time = None
		self.now_sync_time = None
		self.params = None
		self.status = None
		self.type = None
		self.version = None

	def getapiname(self):
		return 'taobao.jushita.jdp.task.update'
