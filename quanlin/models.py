# -*- coding: utf-8 -*-  
from __future__ import unicode_literals
from django.utils.html import format_html
from django.db import models

#单品
class Danpin(models.Model):
    bianhao         = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品编号')
    pinming         = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'品名')
    leixing            = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'类型')
    f5                   = models.CharField(db_column='F5', max_length=255, blank=True,null=True,verbose_name=u'') 
    tiaoma           = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'条码')
    guige             = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'规格')
    danwei          = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单位')
    zhongliang    = models.FloatField( blank=True,null=True,verbose_name=u'重量')


    def __unicode__(self):
        return self.bianhao

    class Meta:
        verbose_name = u"单品"
        verbose_name_plural = u"单品"

        db_table = 'danpin'
       
        
#套餐产品
class Taocan(models.Model):

    bianhao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'套餐编号')
    pinming = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'品名')
    leixing = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'类型')
    tiaoma = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'条码')
    guige = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'规格')
    danwei = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单位')
    zhongliang = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'重量')
    
    def addTaocanDetail(self,danpin=None,count=0):
        if danpin <> None and count >0 :
            tc_detail = TaocanDetail.objects.get_or_create(danpin=danpin,count=count)[0]
            self.taocandetail.add(tc_detail)


    def __unicode__(self):
        return self.bianhao

    class Meta:
        verbose_name = u"套餐"
        verbose_name_plural = u"套餐"
        
        db_table = 'taocan'



# 套餐明细 被 packageDetail替代
# class TaocanDetail(models.Model):
#     danpin = models.ForeignKey(Danpin,verbose_name=u'单品')
#     count = models.IntegerField(max_length=5,verbose_name=u'单品个数')


#     class Meta:
#         verbose_name = "套餐明细"
#        

# #套餐MAP  套餐明细 被 packageDetail替代
# class TaocanMap(models.Model):

#     taocan_tiaoma = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'套餐条码')
#     danpin_tiaoma = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品条码')
#     count = models.IntegerField( blank=True,null=True,verbose_name=u'单品个数')


#     def save2pkgDetails(self):

#         package_product      = Taocan.objects.get(tiaoma=self.taocan_tiaoma)
#         single_product          = Danpin.objects.get(tiaoma=self.danpin_tiaoma)

#         pkgDetail = PackageDetail(package_product=package_product,single_product=single_product,
#                 single_product_count=self.count)
#         pkgDetail.save()
#     class Meta:
#         # verbose_name_plural = u"TaocanMap"

#         # db_table = 'TaocanMap'

#                                 db_table = 'taocan_map'   

#订单抽象类
class DingdanPtr(models.Model):
    dingdan_bianhao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'订单编号')
    waibu_danhao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'外部单号')
    dianpumingcheng = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'店铺')
    chulizhuangtai = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'处理状态')
    fukuanzhuangtai = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'付款状态')
    fahuozhuangtai = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'发货状态')
    phone_num = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'电话')
    pingtai_fahuo_zhuangtai = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'平台发货状态')
    kuaidi_gongsi_mingcheng = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'快递公司')
    kuaidi_danhao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'快递单号')
    dingdan_jingzhong = models.FloatField( blank=True,null=True,verbose_name=u'订单净重')
    fukuan_date = models.DateTimeField( blank=True,null=True,verbose_name=u'付款时间')
    shendan_date = models.DateTimeField( blank=True,null=True,verbose_name=u'审核时间')
    print_date = models.DateTimeField( blank=True,null=True,verbose_name=u'打印时间')
    fahuo_date = models.DateTimeField( blank=True,null=True,verbose_name=u'发货时间')
    maijia_id = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'买家ID')
    shouhuo_ren = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'收货人')
    shouhuo_dizhi = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'收货地址')
    shouhuo_sheng = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'省')
    shouhuo_shi = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'市')
    shouhuo_xian = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'县')
    chanpin_bianhao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'产品编号')
    tiaoxingma = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'条码')
    chanpin_name = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'产品名称')
    gui_ge = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'规格')
    wangdian_pinming = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'网店品名')
    dinghuo_shuliang = models.FloatField( blank=True,null=True,verbose_name=u'订货数量')
    chanpin_baojia = models.FloatField( blank=True,null=True,verbose_name=u'产品报价')
    chanpin_baojia_zongjine = models.FloatField( blank=True,null=True,verbose_name=u'产品报价总金额')
    chanpin_chengjiaojine = models.FloatField( blank=True,null=True,verbose_name=u'产品成交额')
    chanpinchengjiao_danjia = models.FloatField( blank=True,null=True,verbose_name=u'产品成交单价')
    chanpinzhongliang_xiaoji = models.FloatField( blank=True,null=True,verbose_name=u'产品重量小计')
    qianshou_time = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'签收时间')
    class Meta:
        abstract=True

#订单
class Dingdan(DingdanPtr):

    def pay_Month(self):
        if self.fukuan_date <> None :
            return self.fukuan_date.strftime('%Y-%m-%d %H:%M:%S')
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

    def getDingdanDetails(self):
        taocan = Taocan.objects.get(tiaoma=self.tiaoxingma)
        tc_details = taocan.packagedetail_set.all() 

        detailMap = {}
        for detail in tc_details:
            detailMap[detail.danpin] = [detail.count * self.dinghuo_shuliang,0]
             

    def getOrderDetails(self):
        # datas = {'AC330':['5','56.4'],'BK180':['4','43.33']}
        datas = self.getDingdanDetails()
        for data in datas:
            details = DingdanDetail()
            details.initInfos(self,data,datas[data][0],datas[data][1])
            details.save()



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
        verbose_name = u"订单"
        verbose_name_plural = u"订单"
        db_table = 'dingdan'


#套餐明细表，对应 单品与数量
class PackageDetail(models.Model) :
    package_product                   = models.ForeignKey(Taocan,verbose_name=u'套餐')
    single_product                       = models.ForeignKey(Danpin,verbose_name=u'单品')
    single_product_count             =  models.IntegerField(max_length=5,verbose_name=u'单品个数')

    class Meta :
        verbose_name             = u"套餐明细"
        verbose_name_plural   = u"套餐明细"

#订单明细
class DingdanDetail(DingdanPtr) :
    def initInfos(self,ptrDingdan,danpin_huohao,danpin_count,danpin_jiage):

        self.danpin_huohao = danpin_huohao
        self.danpin_count = danpin_count
        self.danpin_jiage = danpin_jiage
        self.dingdan = ptrDingdan
        self.dingdan_bianhao = ptrDingdan.dingdan_bianhao
        self.waibu_danhao = ptrDingdan.waibu_danhao
        self.dianpumingcheng = ptrDingdan.dianpumingcheng
        self.chulizhuangtai = ptrDingdan.chulizhuangtai
        self.fukuanzhuangtai = ptrDingdan.fukuanzhuangtai
        self.fahuozhuangtai = ptrDingdan.fahuozhuangtai
        self.phone_num = ptrDingdan.phone_num
        self.pingtai_fahuo_zhuangtai = ptrDingdan.pingtai_fahuo_zhuangtai
        self.kuaidi_gongsi_mingcheng = ptrDingdan.kuaidi_gongsi_mingcheng
        self.kuaidi_danhao = ptrDingdan.kuaidi_danhao
        self.dingdan_jingzhong = ptrDingdan.dingdan_jingzhong
        self.fukuan_date = ptrDingdan.fukuan_date
        self.shendan_date = ptrDingdan.shendan_date
        self.print_date = ptrDingdan.print_date
        self.fahuo_date = ptrDingdan.fahuo_date
        self.maijia_id = ptrDingdan.maijia_id
        self.shouhuo_ren = ptrDingdan.shouhuo_ren
        self.shouhuo_dizhi = ptrDingdan.shouhuo_dizhi
        self.shouhuo_sheng = ptrDingdan.shouhuo_sheng
        self.shouhuo_shi = ptrDingdan.shouhuo_shi
        self.shouhuo_xian = ptrDingdan.shouhuo_xian
        self.chanpin_bianhao = ptrDingdan.chanpin_bianhao
        self.tiaoxingma = ptrDingdan.tiaoxingma
        self.chanpin_name = ptrDingdan.chanpin_name
        self.gui_ge = ptrDingdan.gui_ge
        self.wangdian_pinming = ptrDingdan.wangdian_pinming
        self.dinghuo_shuliang = ptrDingdan.dinghuo_shuliang
        self.chanpin_baojia = ptrDingdan.chanpin_baojia
        self.chanpin_baojia_zongjine = ptrDingdan.chanpin_baojia_zongjine
        self.chanpin_chengjiaojine = ptrDingdan.chanpin_chengjiaojine
        self.chanpinchengjiao_danjia = ptrDingdan.chanpinchengjiao_danjia
        self.chanpinzhongliang_xiaoji = ptrDingdan.chanpinzhongliang_xiaoji
        self.qianshou_time = ptrDingdan.qianshou_time
   




    dingdan = models.ForeignKey(Dingdan,verbose_name=u'订单')
    
    danpin_huohao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品货号')
    danpin_count = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品数量')
    danpin_jiage =  models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品价格')


    class Meta:
        verbose_name             = u"订单详情"
        verbose_name_plural  = u"订单详情"
        
        db_table                        = 'dingdan_detail'
        # ordering = ['fukuan_date']


