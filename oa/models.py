# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.


class Group(models.Model):
    """组别"""
    name = models.CharField('名称', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'组别'
        verbose_name_plural = u"组别"


class Person(models.Model):
    """员工"""
    MALE = 1
    FEMALE = 0

    GENDER_CHOICES = (
        (MALE, u"男"),
        (FEMALE, u"女")
    )

    name = models.CharField('姓名', max_length=50)
    birthday = models.DateField('出生日期', blank=True, null=True)
    gender = models.IntegerField(
        '性别', max_length=1,
        choices=GENDER_CHOICES,
        default=FEMALE)
    position = models.CharField(
        '职位', max_length=50, blank=True, null=True)
    phone_num = models.CharField('电话', max_length=50, blank=True, null=True)
    qq_num = models.CharField('QQ', max_length=50, blank=True, null=True)
    email = models.CharField('邮箱', max_length=50, blank=True, null=True)
    alipay_num = models.CharField('支付宝', max_length=50, blank=True, null=True)
    group = models.ForeignKey(Group, verbose_name=u'组别', blank=True, null=True)
    ip = models.CharField('IP地址', max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'员工'
        verbose_name_plural = u"员工"


class Brand(models.Model):
    """品牌"""
    name = models.CharField('名称', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'品牌'
        verbose_name_plural = u"品牌"


class DeviceType(models.Model):
    """设备类型"""
    name = models.CharField('名称', max_length=50)
    brand = models.ManyToManyField(Brand, verbose_name=u'品牌')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'设备类型'
        verbose_name_plural = u"设备类型"


class MachineModel(models.Model):
    """机器型号"""
    name = models.CharField('机器型号', max_length=50)
    device_type = models.ForeignKey(DeviceType, verbose_name=u'类型')
    brand = models.ForeignKey(Brand, verbose_name=u'品牌')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'机器型号'
        verbose_name_plural = u"机器型号"


class Device(models.Model):
    """设备"""
    brand = models.ForeignKey(
        Brand, verbose_name='品牌', blank=True, null=True)
    device_type = models.ForeignKey(DeviceType, verbose_name=u'类型')
    machine_model = models.ForeignKey(MachineModel, verbose_name=u'型号')
    serial_number = models.CharField(
        'SN码', max_length=50, blank=True, null=True)
    user = models.ManyToManyField(
        Person, blank=True, null=True, verbose_name=u'使用者')
    buy_date = models.DateField('购买时间')
    use_date = models.DateField('领用时间')
    remark = models.CharField('备注', max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.brand = self.machine_model.brand
        self.device_type = self.machine_model.device_type
        super(Device, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s-%s' % ('设备', self.id)
        # return str(self.machine_model)

    class Meta:
        verbose_name = u'设备'
        verbose_name_plural = u"设备"
