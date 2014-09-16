# -*- coding: utf-8 -*-
from django.contrib import admin
from oa.models import Device,DeviceType


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('machine_model',  'device_type', 'brand')
    pass
    # list_filter = ['dianpumingcheng','kuaidi_gongsi_mingcheng','chulizhuangtai','fukuanzhuangtai','fahuozhuangtai']
    # list_display = ( 'waibu_danhao', 'dianpumingcheng','kuaidi_gongsi_mingcheng','kuaidi_danhao','chanpin_bianhao',
    #     'Orders_detail', 	'dinghuo_shuliang','pay_Month')
    # # inlines = [DingDanInline]
    # search_fields = ['dingdan_bianhao','fukuan_date']
    # date_hierarchy = 'fukuan_date'


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType)
# admin.site.register(TaocanDetail, TaocanDetailAdmin)