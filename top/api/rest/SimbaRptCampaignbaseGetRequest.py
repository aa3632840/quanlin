'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class SimbaRptCampaignbaseGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.end_time = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.search_type = None
		self.source = None
		self.start_time = None
		self.subway_token = None

	def getapiname(self):
		return 'taobao.simba.rpt.campaignbase.get'
