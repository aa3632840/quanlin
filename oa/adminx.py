# -*- coding: utf-8 -*-
from models import Person
from models import DeviceType
from models import Device
from models import Group
from models import MachineModel
from models import Brand
import xadmin
from xadmin import views
from xadmin.plugins.batch import BatchChangeAction


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "泉林本色", "content": "\
            <h3> 泉林本色OA系统 </h3>"},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
                "btns": [
                    {'model': Person}, {'model': Device},
                    {'title': "公司WIKI", 'url': "http://wiki.quanlinbense.com"}
                    ]},
            {"type": "addform", "model": Person},
        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)


class DeviceInline(object):
    model = Device
    extra = 2


class PersonAdmin(object):
    list_display = (
        'name', 'group', 'position', 'phone_num',
        'qq_num', 'alipay_num', 'email')
    actions = [BatchChangeAction, ]
    # inlines = [DeviceInline]


def make_save(object, request, queryset):
    for obj in queryset:
        obj.save()
make_save.short_description = u"批量保存"


class DeviceAdmin(object):

    list_display = (
        'machine_model', 'user',  'device_type', 'use_date', 'brand')
    list_editable = ('use_date')
    style_fields = {'user': 'checkbox-inline'}
    list_filter = ['device_type', 'user']
    raw_id_fields = ('device_type',)
    actions = [make_save, BatchChangeAction]
    # search_fields = ['user']
    # raw_id_fields = ("user",)


class GroupAdmin(object):
    # relfield_style = 'fk-ajax'
    actions = [BatchChangeAction, ]
    pass

xadmin.site.register(Person, PersonAdmin)
xadmin.site.register(DeviceType)
xadmin.site.register(Device, DeviceAdmin)
xadmin.site.register(Group, GroupAdmin)
xadmin.site.register(MachineModel)
xadmin.site.register(Brand)
