# -*- coding: utf-8 -*-  
from models import Person,DeviceType,Device,Group
import xadmin
from xadmin import views

class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "泉林本色", "content": "<h3> 泉林本色OA系统 </h3>"},
        ],
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': Person}, {'model':Device}, {'title': "公司WIKI", 'url': "http://wiki.quanlinbense.com"}]},
            {"type": "addform", "model": Person},
        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)

class DeviceInline(object):
    model = Device
    extra = 2


class PersonAdmin(object):
    list_display = ('name','group','position','phone_num','qq_num','alipay_num','email')
    # list_editable= ('group','position','phone_num','qq_num','alipay_num','email')
    # inlines = [DeviceInline]

class DeviceAdmin(object) :
    list_display = ('name','device_type','buy_date','use_date','user','serial_number')
    list_editable= ('use_date')
    style_fields = {'user': 'checkbox-inline'}
    list_filter = ['device_type','user']
    # search_fields = ['device_type']
    # raw_id_fields = ("user",)

class GroupAdmin(object):
    pass

xadmin.site.register(Person, PersonAdmin) 
xadmin.site.register(DeviceType) 
xadmin.site.register(Device,DeviceAdmin) 
xadmin.site.register(Group,GroupAdmin) 