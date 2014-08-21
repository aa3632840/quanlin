# -*- coding: utf-8 -*-  
from django.contrib import admin
from quanlin.models import Dingdan,Taocan, Danpin,TaocanDetail

class DingDanInline(admin.TabularInline ):
    model = Dingdan
    extra = 3

class TaocanDetailAdmin(admin.ModelAdmin):
    pass

class TaocanAdmin(admin.ModelAdmin):
    # inlines = [
    #     Danpin,
    # ]
    pass
class DanpinAdmin(admin.ModelAdmin):
    pass

class DingDanAdmin(admin.ModelAdmin):

    # fieldsets = [
    #     ('订单编号',               {'fields': ['dingdan_bianhao']}),
    #     # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # list_max_show_all = 20000
    list_per_page = 300
    list_filter = ['dianpumingcheng','kuaidi_gongsi_mingcheng','chulizhuangtai','fukuanzhuangtai','fahuozhuangtai']
    list_display = ( 'waibu_danhao', 'dianpumingcheng','kuaidi_gongsi_mingcheng','kuaidi_danhao','chanpin_bianhao',
        'Orders_detail', 	'dinghuo_shuliang','pay_Month')
    # inlines = [DingDanInline]
    search_fields = ['dingdan_bianhao','fukuan_date']
    date_hierarchy = 'fukuan_date'


    
admin.site.register(Dingdan, DingDanAdmin)
admin.site.register(Taocan, TaocanAdmin)
admin.site.register(Danpin, DanpinAdmin)
# admin.site.register(TaocanDetail, TaocanDetailAdmin)