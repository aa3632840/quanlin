'''
Created by auto_sdk on 2014-09-08 16:48:02
'''
from top.api.base import RestApi
class QtReportUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext_attr = None
		self.gmt_expiry = None
		self.gmt_report = None
		self.gmt_submit = None
		self.is_passed = None
		self.item_desc = None
		self.item_url = None
		self.message = None
		self.nick = None
		self.num_iid = None
		self.qt_code = None
		self.qt_name = None
		self.qt_standard = None
		self.qt_type = None
		self.report_url = None
		self.servcie_item_code = None
		self.sp_name = None
		self.status = None

	def getapiname(self):
		return 'taobao.qt.report.update'
