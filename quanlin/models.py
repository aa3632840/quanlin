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
    zhongliang    = models.FloatField( verbose_name=u'重量')
    purchase_price    = models.FloatField( verbose_name=u'重量')



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

    def get_signPro_ratio(self):

        pkgProduct_details = self.packagedetail_set.all()
        
        #单品费用比率 = 单品数量*单品进价 / 套餐进价

        xmap = {}
        taocan_all_amount = 0
        
        for detail in pkgProduct_details :
            #单品金额=单品进价 * 单品个数
            single_all_amount = detail.single_product.purchase_price * detail.single_product_count
            xmap[detail.single_product] = single_all_amount
            #套餐进价 = 多个（单品数量*单品进价）
            taocan_all_amount = taocan_all_amount + single_all_amount
        
        # print pkgProduct_details
        # print xmap
        ratioMap = {}
        for signPro in xmap :
            if taocan_all_amount <> 0 :
                ratioMap[signPro] = xmap[signPro] / taocan_all_amount
            else:
                ratioMap[signPro] = 1

        
    
        return ratioMap

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
    chanpin_baojia                   = models.FloatField( verbose_name=u'产品报价')
    chanpin_baojia_zongjine   = models.FloatField( verbose_name=u'产品报价总金额')
    chanpin_bianhao               = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'产品编号')
    chanpin_chengjiaojine       = models.FloatField( verbose_name=u'产品成交额')
    chanpin_name                   = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'产品名称')
    chanpinchengjiao_danjia   = models.FloatField( verbose_name=u'产品成交单价')
    chanpinzhongliang_xiaoji   = models.FloatField( verbose_name=u'产品重量小计')
    chulizhuangtai                    = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'处理状态')
    dianpumingcheng              = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'店铺')
    dingdan_bianhao                = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'订单编号')
    dingdan_jingzhong             = models.FloatField( verbose_name=u'订单净重')
    dinghuo_shuliang               = models.FloatField( verbose_name=u'订货数量')
    fahuo_date                         = models.DateTimeField( null=True,verbose_name=u'发货时间')
    fahuozhuangtai                  = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'发货状态' )
    fukuan_date                       = models.DateTimeField( verbose_name=u'付款时间')
    fukuanzhuangtai                = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'付款状态')
    gui_ge                                = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'规格')
    kuaidi_danhao                    = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'快递单号')
    kuaidi_gongsi_mingcheng = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'快递公司')
    maijia_id                             = models.CharField( max_length=255, blank=True,null=True,verbose_name=u'买家ID')
    order_paid_amount            = models.FloatField( verbose_name=u'订单实收金额')
    phone_num                        = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'电话')
    pingtai_fahuo_zhuangtai    = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'平台发货状态')
    print_date                           = models.DateTimeField( blank=True,null=True,verbose_name=u'打印时间')
    qianshou_time                   = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'签收时间')
    shendan_date                    = models.DateTimeField( blank=True,null=True,verbose_name=u'审核时间')
    shouhuo_dizhi                    = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'收货地址')
    shouhuo_ren                      = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'收货人')
    shouhuo_sheng                 = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'省')
    shouhuo_shi                      = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'市')
    shouhuo_xian                    = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'县')
    tiaoxingma                         = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'条码')
    waibu_danhao                   = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'外部单号')
    wangdian_pinming            = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'网店品名')
    class Meta:
        abstract = True

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

        taocandetail = taocan.packagedetail_set.all()

        fmt_html = '<div>'
        brstr = '<br>'
        for detail in taocandetail:
            fmt_html = fmt_html +            u'<span>单品:</span><span >%s</span><span>数量:</span><span >%s</span>%s' %(detail.danpin,                 
                detail.count*self.dinghuo_shuliang,brstr)

        fmt_html = fmt_html + '</div>'
        # return u'%s' %fmt_html
        return format_html(fmt_html)
    Orders_detail.short_description = u'套装明细'


    def can_be_save2orderDetails(self):
        return self.fukuanzhuangtai == u'已付款'

    # 获取对应的 单品名称，个数，单价
    def getOrderDetails(self):
        if not self.can_be_save2orderDetails():
            return []
        pkg_pros = Taocan.objects.filter(tiaoma=self.tiaoxingma)



        if pkg_pros.count() == 0 :
            # print self.tiaoxingma
            single_product = Danpin.objects.get(tiaoma=self.tiaoxingma)
            order_detail = DingdanDetail()
            order_detail.initInfos( self,single_product.bianhao,self.dinghuo_shuliang,self.chanpin_chengjiaojine )
            return [order_detail]
        
        else :            
            order_detail_list =  []
            taocan = pkg_pros[0]
            tc_details = taocan.packagedetail_set.all() 
            #套餐内单品比率
            pkgProduct_detail_ratioMap = taocan.get_signPro_ratio()
            detailMap = {}

            

            for detail in tc_details :
                single_product = detail.single_product
                order_detail = DingdanDetail()
                #订单内单品的数量
                single_product_Allcount = detail.single_product_count * self.dinghuo_shuliang
                #订单内单品对应的实收款=套餐实收价*套餐单品比率
                single_product_all_amount = self.chanpin_chengjiaojine * pkgProduct_detail_ratioMap[single_product]

                order_detail.initInfos(self,single_product,single_product_Allcount,single_product_all_amount)
                order_detail_list.append(order_detail)

        return order_detail_list

    def saveOrderDetails(self):
        DingdanDetail.objects.filter(dingdan=self).delete()
        order_details = self.getOrderDetails()
        self.dingdandetail_set = order_details

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

        self.danpin_count = danpin_count
        self.danpin_huohao = danpin_huohao
        self.danpin_jiage = danpin_jiage

        self.chanpin_baojia = ptrDingdan.chanpin_baojia
        self.chanpin_baojia_zongjine = ptrDingdan.chanpin_baojia_zongjine
        self.chanpin_bianhao = ptrDingdan.chanpin_bianhao
        self.chanpin_chengjiaojine = ptrDingdan.chanpin_chengjiaojine
        self.chanpin_name = ptrDingdan.chanpin_name
        self.chanpinchengjiao_danjia = ptrDingdan.chanpinchengjiao_danjia
        self.chanpinzhongliang_xiaoji = ptrDingdan.chanpinzhongliang_xiaoji
        self.chulizhuangtai = ptrDingdan.chulizhuangtai
        self.dianpumingcheng = ptrDingdan.dianpumingcheng
        self.dingdan = ptrDingdan
        self.dingdan_bianhao = ptrDingdan.dingdan_bianhao
        self.dingdan_jingzhong = ptrDingdan.dingdan_jingzhong
        self.dinghuo_shuliang = ptrDingdan.dinghuo_shuliang
        self.fahuo_date = ptrDingdan.fahuo_date
        self.fahuozhuangtai = ptrDingdan.fahuozhuangtai
        self.fukuan_date = ptrDingdan.fukuan_date
        self.fukuanzhuangtai = ptrDingdan.fukuanzhuangtai
        self.gui_ge = ptrDingdan.gui_ge
        self.kuaidi_danhao = ptrDingdan.kuaidi_danhao
        self.kuaidi_gongsi_mingcheng = ptrDingdan.kuaidi_gongsi_mingcheng
        self.maijia_id = ptrDingdan.maijia_id
        self.order_paid_amount = ptrDingdan.order_paid_amount
        self.phone_num = ptrDingdan.phone_num
        self.pingtai_fahuo_zhuangtai = ptrDingdan.pingtai_fahuo_zhuangtai
        self.print_date = ptrDingdan.print_date
        self.qianshou_time = ptrDingdan.qianshou_time
        self.shendan_date = ptrDingdan.shendan_date
        self.shouhuo_dizhi = ptrDingdan.shouhuo_dizhi
        self.shouhuo_ren = ptrDingdan.shouhuo_ren
        self.shouhuo_sheng = ptrDingdan.shouhuo_sheng
        self.shouhuo_shi = ptrDingdan.shouhuo_shi
        self.shouhuo_xian = ptrDingdan.shouhuo_xian
        self.tiaoxingma = ptrDingdan.tiaoxingma
        self.waibu_danhao = ptrDingdan.waibu_danhao
        self.wangdian_pinming = ptrDingdan.wangdian_pinming




    dingdan = models.ForeignKey(Dingdan,verbose_name=u'订单')
    
    danpin_huohao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品货号')
    danpin_count = models.IntegerField(null=True,verbose_name=u'单品数量')
    danpin_jiage = models.FloatField( verbose_name=u'单品价格')

    def __unicode__(self) :
        return 'Order_Detail %s' % self.dingdan_bianhao
    class Meta:
        verbose_name             = u"订单详情"
        verbose_name_plural  = u"订单详情"
        
        db_table                        = 'dingdan_detail'
        # ordering = ['fukuan_date']


