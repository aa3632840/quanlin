# -*- coding: utf-8 -*-
from models import *
import xadmin
from xadmin.plugins.batch import BatchChangeAction
import json


# class VirClassInline(object):
#     model = VirtualFeild
#     extra = 2


class RealClassInline(object):
    model = RealFeild
    extra = 2


# class VirClassMapInline(object):
#     model = Virtual2RealAdapterFieldMap
#     extra = 2


class RealFieldInline(object):
    model = RealFieldAlias
    extra = 2


# class VirtuasClassAdmin(object):
#     inlines = [VirClassInline]


# class VirtualClassMapAdmin(object):
#     inlines = [VirClassMapInline]


class RealClassMapAdmin(object):
    inlines = [RealClassInline]


class PersonAdmin(object):
    list_display = (
        'name', 'position', 'phone_num',
        'qq_num', 'alipay_num', 'email')
    actions = [BatchChangeAction, ]
    # inlines = [DeviceInline]


def make_save_2_real(object, request, queryset):
    for vir_data in queryset:
        vir_data.save_2_real()
make_save_2_real.short_description = u"批量插入数据"


def make_all_merge_2_match(object, request, queryset):
    for vir_data in queryset:
        vir_data.do_merge_2_objects()
make_all_merge_2_match.short_description = u"批量合并数据"

def make_refresh_virtual_data_match(object, request, queryset):
    for vir_data in queryset:
        vir_data.save_matching_objects_jsons()
make_refresh_virtual_data_match.short_description = u"批量刷新匹配数据"

def make_cover_virtual_data_match(object, request, queryset):
    for vir_data in queryset:
        vir_data.do_cover_2_matching_objects()
make_cover_virtual_data_match.short_description = u"批量覆盖数据"

class VirtualDataAdmin(object):
    list_display = (
        'data_adapter', 'source_json', 'can_be_restore_real', 'erro_msg', 'matching_objects_count')
    actions = [make_save_2_real,
        make_refresh_virtual_data_match,
        make_all_merge_2_match,make_cover_virtual_data_match ]
    list_filter = ['data_adapter','quick_job', 'matching_objects_count']
    # inlines = [DeviceInline]


class DataAdapterInline(object):
    model = DataFeildAdapter
    extra = 2


class DataAdapterAdmin(object):
    list_display = (
        'name', 'real_class')
    inlines = [DataAdapterInline]

class FieldAdapterAdmin(object):
    #字段适配器
    list_display = (
        'data_adapter', 'real_field', 'order_id')
    # inlines = [DeviceInline]
    raw_id_fields = ('data_adapter',)
    style_fields = {'data_adapter': 'checkbox-inline'}



def get_virtual_data_from_one_line(quick_add_job,field_adapter_list, source_line):

    virtual_data,is_new = VirtualData.objects.get_or_create(
        quick_job=quick_add_job, source_line=source_line, data_adapter=quick_add_job.data_adapter)
    # print virtual_data, is_new
    return virtual_data.init_json_by_field_adapter()



def get_virtual_datas_from_source(quick_add_job, source_text):
    #根据索引字段，来查找是否有重复项
    #重复的和新的都进行备注
    data_adapter = quick_add_job.data_adapter
    field_adapter_list = \
        data_adapter.datafeildadapter_set.order_by('order_id').all()
    virtual_data_list = []
    for source_line in source_text.strip().split('\n'):
        virtual_data = get_virtual_data_from_one_line(quick_add_job, field_adapter_list, source_line)
        virtual_data_list.append(virtual_data)
        # virtual_data.save()
    return virtual_data_list


def make_source_2_virtual_data(object, request, queryset):
    for quick_add_job in queryset:
        source_text = quick_add_job.source_text
        virtual_data_list = get_virtual_datas_from_source(
            quick_add_job, source_text)
        for virtual_data in virtual_data_list:
            virtual_data.save()

make_source_2_virtual_data.short_description = u"保存到虚拟数据"


class QuickAddJobAdmin(object):
    list_display = (
        'name', 'data_adapter')
    actions = [make_source_2_virtual_data, ]
    # inlines = [DeviceInline]


class RealFieldAdmin(object):
    # list_display = (
    #     'name', 'data_adapter')
    # actions = [make_source_2_virtual_data, ]
    inlines = [RealFieldInline]


# xadmin.site.register(Person, PersonAdmin)
# xadmin.site.register(VirtualClass, VirtuasClassAdmin)
# xadmin.site.register(VirtualFeild)
xadmin.site.register(VirtualData, VirtualDataAdmin)
# xadmin.site.register(Virtual2RealAdapterClassMap, VirtualClassMapAdmin)
# xadmin.site.register(Virtual2RealAdapterFieldMap)
xadmin.site.register(RealClass, RealClassMapAdmin)
xadmin.site.register(RealFeild, RealFieldAdmin)
xadmin.site.register(DataAdapter, DataAdapterAdmin)
xadmin.site.register(DataFeildAdapter, FieldAdapterAdmin)
xadmin.site.register(QuickAddJob, QuickAddJobAdmin)
xadmin.site.register(RealFieldAlias)

