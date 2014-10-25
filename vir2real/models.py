# -*- coding: utf-8 -*-
from django.db import models
from operator import contains
from oa.models import Person
from quanlin.models import *
import json


class RealClass(models.Model):
    """虚拟类"""
    name = models.CharField(u'名字', max_length=50)
    discription = models.CharField(u'描述', max_length=50, blank=True, null=True)
    has_generate_fields = models.BooleanField(u'是否已生成字段', default=False)

    def is_class_registration(self):
        return contains(globals(), self.name)

    def get_real_class_type(self):
        if contains(globals(), self.name):
            return globals()[self.name]

    def get_real_field_names(self):
        return [real_field.name for real_field in self.realfeild_set.all() ]

    def save(self, *args, **kwargs):
        """保存所有真字段到真类"""
        if self.is_class_registration():

            clz = globals()[self.name]
            print clz
            _xmeta = getattr(clz, '_meta', None)
            print _xmeta
            if _xmeta:
                self.discription = _xmeta.verbose_name
                print self.discription
                self.has_generate_fields = True
                self.realfeilds = []
                super(RealClass, self).save(*args, **kwargs)
                print 111
                real_local_fields = _xmeta.local_fields
                for real_field_attrs in real_local_fields:
                    print 444
                    real_field, created = RealFeild.objects.get_or_create(
                        name=real_field_attrs.name, pclass=self)
                    print 555
                    real_field.init(self,real_field_attrs)
                    print 333
                    real_field.save()
                    print 222
                    print '-'*40

    class Meta:
        verbose_name = u'真类'
        verbose_name_plural = u'真类'

    def __unicode__(self):
        return self.name


class RealFeild(models.Model):
    """真字段"""
    TYPE_INT = 'IntegerField'
    TYPE_CHAR = 'TYPE_CHAR'
    TYPE_DATE = 'TYPE_DATE'
    TYPE_FLOAT = 'TYPE_FLOAT'
    TYPE_DOUBLE = 'TYPE_DOUBLE'

    TYPE_CHOICES = (
        (TYPE_INT, TYPE_INT),
        (TYPE_CHAR, TYPE_CHAR),
        (TYPE_INT, TYPE_DATE),
        (TYPE_INT, TYPE_FLOAT),
        (TYPE_INT, TYPE_DOUBLE),
    )
    name = models.CharField(u'名字', max_length=50)
    pclass = models.ForeignKey(RealClass, verbose_name=u'所属真类')
    discription = models.CharField(u'描述', max_length=50, blank=True, null=True)
    null = models.BooleanField(u'空?', max_length=50,default=True)
    type = models.CharField(
        u'字段类型', max_length=50)

    def init(self, pclass, real_field_attrs):
        self.name = real_field_attrs.name
        self.type = real_field_attrs.__class__.__name__
        self.discription = real_field_attrs.verbose_name
        self.null = real_field_attrs.null
        self.pclass = pclass
        self.init_field_alias(real_field_attrs)

    def init_field_alias(self, real_field_attrs):
        #初始化别名
        for alias_choice, alias_choice_descrition in real_field_attrs.choices:
            RealFieldAlias.objects.get_or_create(
                real_field=self,
                alias_key=alias_choice_descrition,
                alias_choice=alias_choice)

    def save(self, *args, **kwargs):
        super(RealFeild,self).save(*args, **kwargs)


    def get_real_value_from_alias(self, data):
        #根据别名来取得正确的值
        if self.realfieldalias_set.count() == 0:
            return data
        else:
            for alias in self.realfieldalias_set.all():
                if data in[alias.alias_key, alias.alias_choice]:
                    return alias.alias_choice
            return None

    def __unicode__(self):
        return '%s-%s' % (self.pclass.discription, self.discription)

    class Meta:
        verbose_name = u'真字段'
        verbose_name_plural = u'真字段'


class RealFieldAlias(models.Model):
    real_field = models.ForeignKey(RealFeild, verbose_name=u'所属字段')
    alias_key = models.CharField(u'别名', max_length=50)
    alias_choice = models.CharField(u'对应CHOICES值', max_length=50)

    class Meta:
        verbose_name = u'字段匹配别名'
        verbose_name_plural = u'字段匹配别名'

    def __unicode__(self):
        return '%s-%s-%s' % (self.real_field, self.alias_key, self.alias_choice)


# class VirtualClass(models.Model):
#     """虚拟类"""
#     name = models.CharField(u'名字', max_length=50)
#     discription = models.CharField(u'描述', max_length=50, blank=True, null=True)
#     class Meta:
#         verbose_name = u'虚类'
#         verbose_name_plural = u'虚类'

#     def __unicode__(self):
#         return self.name


# class VirtualFeild(models.Model):
#     """虚拟字段"""
#     TYPE_INT = 'TYPE_INT'
#     TYPE_CHAR = 'TYPE_CHAR'
#     TYPE_DATE = 'TYPE_DATE'
#     TYPE_FLOAT = 'TYPE_FLOAT'
#     TYPE_DOUBLE = 'TYPE_DOUBLE'

#     TYPE_CHOICES = (
#         (TYPE_INT, TYPE_INT),
#         (TYPE_CHAR, TYPE_CHAR),
#         (TYPE_INT, TYPE_DATE),
#         (TYPE_INT, TYPE_FLOAT),
#         (TYPE_INT, TYPE_DOUBLE),
#     )
#     name = models.CharField(u'名字', max_length=50)
#     pclass = models.ForeignKey(VirtualClass, verbose_name=u'所属类')
#     type = models.CharField(
#         u'字段类型', max_length=50, default=TYPE_CHAR, choices=TYPE_CHOICES)

#     def __unicode__(self):
#         return '%s-%s' % (self.pclass.name, self.name)

#     class Meta:
#         verbose_name = u'虚字段'
#         verbose_name_plural = u'虚字段'


class DataAdapter(models.Model):
    """数据适配器"""
    name = models.CharField(u'名称', max_length=50)
    real_class = models.ForeignKey(RealClass, verbose_name='实类')

    def save(self, *args, **kwargs):
        super(DataAdapter, self).save(*args, **kwargs)

    def get_details_discription(self):
        dirscription = ''
        for field_detail in self.datafeildadapter_set.all():
            dirscription = '%s\n%s-->%s' % (
                dirscription,  field_detail.order_id, field_detail)
        return dirscription

    def get_real_class_type(self):
        return self.real_class.get_real_class_type()   

    class Meta:
        verbose_name = u'适配器'
        verbose_name_plural = u'适配器'

    def __unicode__(self):
        return '%s' % (self.name)


class DataFeildAdapter(models.Model):
    """字段对应"""
    data_adapter = models.ForeignKey(
        DataAdapter, verbose_name=u'所属适配器')
    real_field = models.ForeignKey(RealFeild, verbose_name=u'字段')
    order_id = models.IntegerField(u'排序ID', max_length=5)
    is_index = models.BooleanField(u'是否为索引', default=False)

    class Meta:
        verbose_name = u'子适配器'
        verbose_name_plural = u'子适配器'

    def __unicode__(self):
        return '%s to %s' % (self.data_adapter, self.real_field)


# class Virtual2RealAdapterClassMap(models.Model):
#     """虚表对应"""
#     virtual_class = models.ForeignKey(VirtualClass, verbose_name='虚拟类名')
#     real_class_name = models.CharField(u'真实类名', max_length=50)

#     def is_class_registration(self):
#         return contains(globals(), self.real_class_name)

#     def save(self, *args, **kwargs):
#         if self.is_class_registration():
#             super(Virtual2RealAdapterClassMap, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name = '虚表对应'
#         verbose_name_plural = '虚表对应'

#     def __unicode__(self):
#         return '%s to %s' % (self.virtual_class, self.real_class_name)


# class Virtual2RealAdapterFieldMap(models.Model):
#     """虚字段对应"""
#     class_map = models.ForeignKey(
#         Virtual2RealAdapterClassMap, verbose_name='所属虚拟CLASS_MAP')
#     virtual_field = models.ForeignKey(VirtualFeild, verbose_name='虚拟字段')
#     real_field_name = models.CharField(u'真实字段', max_length=50)
#     order_id = models.IntegerField(u'排序字段',max_length=5)

#     class Meta:
#         verbose_name = u'虚字段对应'
#         verbose_name_plural = u'虚字段对应'

#     def __unicode__(self):
#         return '%s to %s' % (self.virtual_field, self.real_field_name)



# class Person(models.Model):
#     """员工"""
#     MALE = 1
#     FEMALE = 0

#     GENDER_CHOICES = (
#         (MALE, u"男"),
#         (FEMALE, u"女")
#     )

#     name = models.CharField('姓名', max_length=50)
#     birthday = models.DateField('出生日期', blank=True, null=True)
#     gender = models.IntegerField(
#         '性别', max_length=1,
#         choices=GENDER_CHOICES,
#         default=FEMALE)
#     position = models.CharField(
#         '职位', max_length=50, blank=True, null=True)
#     phone_num = models.CharField('电话', max_length=50, blank=True, null=True)
#     qq_num = models.CharField('QQ', max_length=50, blank=True, null=True)
#     email = models.CharField('邮箱', max_length=50, blank=True, null=True)
#     alipay_num = models.CharField('支付宝', max_length=50, blank=True, null=True)


class QuickAddJob(models.Model):

    name = models.CharField(u'任务名称', max_length=50)
    data_adapter = models.ForeignKey(DataAdapter, verbose_name=u'适配器')
    data_adapter_details = models.TextField(u'适配器详情', blank=True, null=True)
    source_text = models.TextField(u'源内容', blank=True, null=True)

    class Meta:
        verbose_name = u"批量添加任务"
        verbose_name_plural = u"批量添加任务"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.data_adapter_details = self.data_adapter.get_details_discription()
        super(QuickAddJob, self).save(*args, **kwargs)


class VirtualData(models.Model):
    data_adapter = models.ForeignKey(
        DataAdapter, verbose_name=u'适配器')
    quick_job = models.ForeignKey(
        QuickAddJob, verbose_name=u'任务名称', blank=True, null=True)
    source_json = models.TextField(u'Json')

    source_line = models.TextField(u'原始数据', max_length=255)
    can_be_restore_real = models.BooleanField(u'可转化否', default=True)
    matching_objects_count = models.IntegerField(u'匹配条数', max_length=5, default=0)
    matching_objects = models.TextField(u'匹配数据', blank=True, null=True)

    erro_msg = models.CharField(u'错误日志', max_length=255, null=True, blank=True)

    def get_field_adapter_list(self):
        return self.data_adapter.datafeildadapter_set.all()

    def get_matching_object_text(self, clzobj):
        #获取匹配的对象的json text格式
        object_json = {}
        real_field_name_list = \
            self.data_adapter.real_class.get_real_field_names()
        for real_field_name in real_field_name_list:
            if hasattr(clzobj, real_field_name):
                object_json[real_field_name] = str(getattr(clzobj, real_field_name))
        return json.dumps(object_json, ensure_ascii=False)

    def get_matching_objects_list(self):
        #寻找所有匹配的对象
        clz = self.data_adapter.get_real_class_type()
        kw = {}
        json_dict = self.get_json_dict()
        for field_adapter in self.get_field_adapter_list():
            if field_adapter.is_index:
                real_fname = field_adapter.real_field.name
                kw[real_fname] = json_dict[real_fname]
        clz_objs = clz.objects.filter(*(), **kw).all()
        return clz_objs

    def get_matching_objects_jsons(self):
        clz_objs = self.get_matching_objects_list()
        match_objects_json = ''
        for clzobj in clz_objs:
            match_objects_json = '%s%s\n' % \
                (match_objects_json, self.get_matching_object_text(clzobj))

        return clz_objs.count(), match_objects_json

    def do_cover_2_matching_objects(self):
        match_clz_objs = self.get_matching_objects_list()
        json_dict = self.get_json_dict()
        for clz_obj in match_clz_objs:
            clz_obj.delete()
        self.save_2_real()

    def do_merge_2_objects(self):
        match_clz_objs = self.get_matching_objects_list()
        json_dict = self.get_json_dict()
        for clz_obj in match_clz_objs:
            for attr in json_dict:
                setattr(clz_obj, attr, json_dict[attr])
            clz_obj.save()

    def save_matching_objects_jsons(self):
        #获取所有匹配对象的json
        self.matching_objects_count ,self.matching_objects = self.get_matching_objects_jsons()
        self.save()
        

    def init_json_by_field_adapter(self):
        #根据一行来返回 json
        field_adapter_list = self.get_field_adapter_list()
        source_line = self.source_line
        json_dict = {}
        datas = source_line.strip().split('\t')
        for idx, field_adapter in enumerate(field_adapter_list):
            value = field_adapter.real_field.get_real_value_from_alias(datas[idx])
            if value:
                json_dict[field_adapter.real_field.name] = value
                self.source_json = json.dumps(
                    json_dict, ensure_ascii=False, sort_keys=True)
            else:
                self.can_be_restore_real = False
                self.source_json = ''
                self.erro_msg = u'第%s个值“%s”匹配失败' % (idx, datas[idx])
                break
        return self

    def get_json_dict(self):
        return json.loads(self.source_json)

    def save_2_real(self):
        #直接插入
        if self.can_be_restore_real:
            real_clz = self.data_adapter.real_class.get_real_class_type()
            data_dict = json.loads(self.source_json)
            real_obj = real_clz()
            print data_dict
            for attr_name in data_dict:
                print attr_name, data_dict[attr_name]
                setattr(real_obj, attr_name, data_dict[attr_name])
            real_obj.save()




    class Meta:
        verbose_name = u'虚数据'
        verbose_name_plural = u'虚数据'

    def __unicode__(self):
        return '%s' % self.id
