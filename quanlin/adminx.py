# -*- coding: utf-8 -*-  
import xadmin
from xadmin import views
from models import Dingdan,Taocan, Danpin,DingdanDetail
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
# from django.contrib import admin

class DingdanAdmin(object):

    # list_filter = ['dianpumingcheng','kuaidi_gongsi_mingcheng','chulizhuangtai','fukuanzhuangtai','fahuozhuangtai']
    list_filter = ['fukuan_date']

    list_display = ( 'waibu_danhao', 'dianpumingcheng','kuaidi_gongsi_mingcheng','kuaidi_danhao',
    	'fukuan_date','chanpin_bianhao',
        'dinghuo_shuliang', 'Orders_detail')
    # inlines = [DingDanInline]
    search_fields = ['waibu_danhao']
    # date_hierarchy = 'fukuan_date'

class DingdanDetailAdmin(object):

    list_filter = ['danpin_huohao']

    list_display = ('dingdan','dingdan_bianhao', 'danpin_huohao','danpin_count','danpin_jiage')
    # inlines = [DingDanInline]
    # search_fields = ['waibu_danhao']
    # date_hierarchy = 'fukuan_date'


xadmin.site.register(DingdanDetail, DingdanDetailAdmin)
xadmin.site.register(Dingdan, DingdanAdmin)



