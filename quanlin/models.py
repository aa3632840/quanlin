# -*- coding: utf-8 -*-  
from __future__ import unicode_literals
from django.utils.html import format_html
from django.db import models

class Danpin(models.Model):

    bianhao = models.CharField(max_length=255, blank=True)
    pinming = models.CharField(max_length=255, blank=True)
    leixing = models.CharField(max_length=255, blank=True)
    f5 = models.CharField(db_column='F5', max_length=255, blank=True) # Field name made lowercase.
    tiaoma = models.CharField(max_length=255, blank=True)
    guige = models.CharField(max_length=255, blank=True)
    danwei = models.CharField(max_length=255, blank=True)
    zhongliang = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.bianhao

    class Meta:
        verbose_name = "单品"
        verbose_name_plural = "单品"
        # app_label = u"泉林本色"
        db_table = 'danpin'        

class TaocanDetail(models.Model):
    danpin = models.ForeignKey(Danpin)
    count = models.IntegerField(max_length=5)
    
    def __unicode__(self):
        return "detail %s_*_%s" %(self.danpin,self.count)


class Taocan(models.Model):

    bianhao = models.CharField(max_length=255, blank=True)
    pinming = models.CharField(max_length=255, blank=True)
    leixing = models.CharField(max_length=255, blank=True)
    tiaoma = models.CharField(max_length=255, blank=True)
    guige = models.CharField(max_length=255, blank=True)
    danwei = models.CharField(max_length=255, blank=True)
    zhongliang = models.CharField(max_length=255, blank=True)
    taocandetail = models.ManyToManyField(TaocanDetail)
    
    def addTaocanDetail(self,danpin=None,count=0):
        if danpin <> None and count >0 :
            tc_detail = TaocanDetail.objects.get_or_create(danpin=danpin,count=count)[0]
            self.taocandetail.add(tc_detail)


    def __unicode__(self):
        return self.bianhao

    class Meta:
        verbose_name = "套餐"
        verbose_name_plural = "套餐"
        # app_label = u"泉林本色"
        db_table = 'taocan'


class TaocanMap(models.Model):

    taocan_tiaoma = models.CharField(max_length=255, blank=True)
    danpin_tiaoma = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        # 
        db_table = 'taocan_map'   

class Dingdan(models.Model):
    dingdan_bianhao = models.CharField(max_length=255, blank=True)
    waibu_danhao = models.CharField(max_length=255, blank=True)
    dianpumingcheng = models.CharField(max_length=255, blank=True)
    chulizhuangtai = models.CharField(max_length=255, blank=True)
    fukuanzhuangtai = models.CharField(max_length=255, blank=True)
    fahuozhuangtai = models.CharField(max_length=255, blank=True)
    phone_num = models.CharField(max_length=255, blank=True)
    pingtai_fahuo_zhuangtai = models.CharField(max_length=255, blank=True)
    kuaidi_gongsi_mingcheng = models.CharField(max_length=255, blank=True)
    kuaidi_danhao = models.CharField(max_length=255, blank=True)
    dingdan_jingzhong = models.FloatField(blank=True, null=True)
    fukuan_date = models.DateTimeField(blank=True, null=True)
    shendan_date = models.DateTimeField(blank=True, null=True)
    print_date = models.DateTimeField(blank=True, null=True)
    fahuo_date = models.DateTimeField(blank=True, null=True)
    maijia_id = models.CharField(max_length=255, blank=True)
    shouhuo_ren = models.CharField(max_length=255, blank=True)
    shouhuo_dizhi = models.CharField(max_length=255, blank=True)
    shouhuo_sheng = models.CharField(max_length=255, blank=True)
    shouhuo_shi = models.CharField(max_length=255, blank=True)
    shouhuo_xian = models.CharField(max_length=255, blank=True)
    chanpin_bianhao = models.CharField(max_length=255, blank=True)
    tiaoxingma = models.CharField(max_length=255, blank=True)
    chanpin_name = models.CharField(max_length=255, blank=True)
    gui_ge = models.CharField(max_length=255, blank=True)
    wangdian_pinming = models.CharField(max_length=255, blank=True)
    dinghuo_shuliang = models.FloatField(blank=True, null=True)
    chanpin_baojia = models.FloatField(blank=True, null=True)
    chanpin_baojia_zongjine = models.FloatField(blank=True, null=True)
    chanpin_chengjiaojine = models.FloatField(blank=True, null=True)
    chanpinchengjiao_danjia = models.FloatField(blank=True, null=True)
    chanpinzhongliang_xiaoji = models.FloatField(blank=True, null=True)
    qianshou_time = models.CharField(max_length=255, blank=True)


    def pay_Month(self):
        if self.fukuan_date <> None :
            return self.fukuan_date.strftime("%Y-%m-%d %H:%I:%S")
    pay_Month.short_description = u'支付日期'



    def Orders_detail(self):
        taocan_set = Taocan.objects.filter(bianhao=self.chanpin_bianhao)
        if taocan_set.count()>0:
            taocan = taocan_set[0]

        else:
            return u''

        taocandetail = taocan.taocandetail.all()

        fmt_html = '<div>'
        brstr = '<br>'
        for detail in taocandetail:
            fmt_html = fmt_html +            u'<span>单品:</span><span >%s</span><span>数量:</span><span >%s</span>%s' %(detail.danpin,                 
                detail.count*self.dinghuo_shuliang,brstr)

        fmt_html = fmt_html + '</div>'
        # return u'%s' %fmt_html
        return format_html(fmt_html)
    Orders_detail.short_description = u'套装明细'

    def colored_name(self):
        return format_html('<div><span width:20px>{0}</span><span width:20px>{0}</span><br>{1}<br>{2}</span><span>{0}<br>{1}<br>{2}</span></div>',
                           self.kuaidi_danhao,
                           self.chulizhuangtai,
                           self.chanpin_name)
                # return format_html('<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>',
                #            self.kuaidi_danhao,
                #            self.chulizhuangtai,
                #            self.chanpin_name)



    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
        # app_label = u"泉林本色"
        db_table = 'dingdan'
        #ordering = 'dingdan_bianhao'




def syncTaocan():
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    t_maps = TaocanMap.objects.all()
    print t_maps.count()
    for t_map in t_maps:
        tcs = Taocan.objects.filter(tiaoma=t_map.taocan_tiaoma)
        for t in tcs:
            dps = Danpin.objects.filter(tiaoma=t_map.danpin_tiaoma)

            for dp in dps:
                t.addTaocanDetail(dp,t_map.count)

    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
# >>> from quanlin.models import * ;syncTaocan()
# >>> 