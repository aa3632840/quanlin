# -*- coding: utf-8 -*-  
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    """组别"""
    name = models.CharField('名称', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u'组别'
        verbose_name_plural = u"组别"


class Person(models.Model):
    """员工"""
    MALE = 1
    FEMALE = 0

    GENDER_CHOICES = (
        (MALE, u"男"),
        (FEMALE,u"女")
    )

    name = models.CharField('姓名', max_length=50)
    birthday = models.DateField('出生日期',blank=True,null=True)
    gender = models.IntegerField('性别', max_length=1,choices=GENDER_CHOICES,default=FEMALE)
    position = models.CharField('职位', max_length=50,blank=True,null=True)
    phone_num = models.CharField('电话', max_length=50,blank=True, null=True)
    qq_num = models.CharField('QQ', max_length=50,blank=True, null=True)
    email = models.CharField('邮箱', max_length=50,blank=True, null=True)
    alipay_num = models.CharField('支付宝', max_length=50,blank=True,null=True)
    group = models.ForeignKey(Group,verbose_name=u'组别',blank=True,null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u'员工'
        verbose_name_plural = u"员工"


class DeviceType(models.Model):
    """设备类型"""
    type_name = models.CharField('类型', max_length=50)
    
    def __unicode__(self):
        return self.type_name

    class Meta:
        verbose_name=u'设备类型'
        verbose_name_plural = u"设备类型"


class Device(models.Model):
    """设备"""
    
    name = models.CharField('型号', max_length=50)
    brand = models.CharField('品牌', blank=True,null=True,max_length=50)
    device_type = models.ForeignKey(DeviceType,verbose_name=u'类型')
    serial_number = models.CharField('SN码', max_length=50,blank=True,null=True)
    user = models.ManyToManyField(Person,verbose_name=u'使用者')
    buy_date = models.DateField('购买时间')
    use_date = models.DateField('领用时间')
    remark = models.CharField('备注', max_length=255,blank=True,null=True)
    

    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u'设备'
        verbose_name_plural = u"设备"





