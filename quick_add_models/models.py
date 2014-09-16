from django.db import models


class QuickAddJob(models.Model):
    name = models.CharField('任务名称', max_length=50)
    relation = models.CharField('关联对象', max_length=50)
    source_data = models.TextField()


class VirtualClass(models.Model):

    class Meta:
        verbose_name = 'VirtualClass'
        verbose_name_plural = 'VirtualClasss'

    def __unicode__(self):
        return self.name


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

    ip = models.CharField('IP地址', max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'员工'
        verbose_name_plural = u"员工"