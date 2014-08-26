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
    list_filter = ['fukuan_date','dianpumingcheng']

    list_display = ( 'waibu_danhao', 'dianpumingcheng','kuaidi_gongsi_mingcheng','kuaidi_danhao',
    	'fukuan_date','chanpin_bianhao',
        'dinghuo_shuliang', 'Orders_detail')
    # inlines = [DingDanInline]
    search_fields = ['dingdan_bianhao','waibu_danhao','tiaoxingma']
    # date_hierarchy = 'fukuan_date'

class DingdanDetailAdmin(object):

    list_filter = ['danpin_huohao','fukuan_date']

    # excloud = 'dingdan'
    list_display = ('dianpumingcheng','waibu_danhao',
         'danpin_huohao','danpin_count','danpin_jiage','fukuan_date',
         'fahuo_date','order_paid_amount',
         'kuaidi_gongsi_mingcheng','kuaidi_danhao',
         'chanpin_bianhao',
         'fahuozhuangtai','pingtai_fahuo_zhuangtai',
         'phone_num')
    # inlines = [DingDanInline]
    search_fields = ['dingdan_bianhao','waibu_danhao','dianpumingcheng']
    # date_hierarchy = 'fukuan_date'


xadmin.site.register(DingdanDetail, DingdanDetailAdmin)
xadmin.site.register(Dingdan, DingdanAdmin)



