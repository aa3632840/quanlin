# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html
from django.db import models

TRADE_NO_CREATE_PAY = 'TRADE_NO_CREATE_PAY'
WAIT_BUYER_PAY = 'WAIT_BUYER_PAY'
SELLER_CONSIGNED_PART = 'SELLER_CONSIGNED_PART'
WAIT_SELLER_SEND_GOODS = 'WAIT_SELLER_SEND_GOODS'
WAIT_BUYER_CONFIRM_GOODS = 'WAIT_BUYER_CONFIRM_GOODS'
TRADE_BUYER_SIGNED = 'TRADE_BUYER_SIGNED'
TRADE_FINISHED = 'TRADE_FINISHED'
TRADE_CLOSED = 'TRADE_CLOSED'
TRADE_CLOSED_BY_TAOBAO = 'TRADE_CLOSED_BY_TAOBAO'
PAY_PENDING = 'PAY_PENDING'
WAIT_PRE_AUTH_CONFIRM = 'WAIT_PRE_AUTH_CONFIRM'


STATUS_CHOICES = (
        (TRADE_NO_CREATE_PAY, '没有创建支付宝交易'),
        (WAIT_BUYER_PAY,'等待买家付款'),
        (SELLER_CONSIGNED_PART,'卖家部分发货'),
        (WAIT_SELLER_SEND_GOODS,'买家已付款，等待发货'),
        (WAIT_BUYER_CONFIRM_GOODS,'等待买家确认收货'),
        (TRADE_BUYER_SIGNED,'买家已签收,货到付款专用'),
        (TRADE_FINISHED,'交易成功'),
        (TRADE_CLOSED,'交易关闭'),
        (TRADE_CLOSED_BY_TAOBAO,'交易被淘宝关闭'),
        (PAY_PENDING,'国际信用卡支付付款确认中'),
        (WAIT_PRE_AUTH_CONFIRM,'0元购合约中'),
     )
class TradeParent(models.Model):
    """订单父类"""


    GUARANTEE_TRADE = 'GUARANTEE_TRADE' #一口价、拍卖
    AUTO_DELIVERY = 'AUTO_DELIVERY' #自动发货
    EC = 'EC' # 直冲
    COD = 'COD' #货到付款
    STEP = 'STEP' #万人团

    SHOP_TM = "天猫"
    SHOP_YHD = "一号店"
    SHOP_JD = "京东"
    SHOP_JH = "建行善融"
    SHOP_RYG = "工行融E购"

    SHOP_CHOICES = (
        (SHOP_TM,SHOP_TM),
        (SHOP_YHD,SHOP_YHD),
        (SHOP_JD,SHOP_JD),
        (SHOP_JH,SHOP_JH),
        (SHOP_RYG,SHOP_RYG),

        )
    TYPE_CHOICES = (
        (GUARANTEE_TRADE,'一口价、拍卖'),
        (AUTO_DELIVERY,'自动发货'),
        (EC,'直冲'),
        (COD,'货到付款'),
        (STEP,'万人团'),
        )

    tid = models.CharField('交易编号 父订单的交易编号',blank=True,null=True,max_length=50)
    seller_nick = models.CharField('卖家昵称', max_length=50)
    payment = models.FloatField('实付金额',blank=True,null=True,default=0)
    out_post_fee = models.FloatField('实付邮费',blank=True,null=True,default=0)
    post_fee = models.FloatField('实收邮费',blank=True,null=True,default=0)
    receiver_name = models.CharField('收货人的姓名',blank=True,null=True, max_length=50)
    receiver_state = models.CharField('收货人的所在省份',blank=True,null=True, max_length=50)
    receiver_address = models.CharField('收货人的详细地址',blank=True,null=True, max_length=250)
    receiver_zip = models.CharField('收货人的邮编',blank=True,null=True, max_length=50)
    receiver_mobile =   models.CharField('收货人的手机号码',blank=True,null=True, max_length=50)
    receiver_phone =   models.CharField('收货人的电话号码',blank=True,null=True, max_length=50)
    received_payment = models.FloatField('卖家实际收到的支付宝打款金额',blank=True,null=True)
    status = models.CharField('交易状态',blank=True,null=True, max_length=50,choices=STATUS_CHOICES)
    shop = models.CharField('店铺',blank=True,null=True, max_length=50,choices=SHOP_CHOICES)
    title = models.CharField('交易标题',blank=True,null=True, max_length=50)
    trade_type = models.CharField('交易类型',blank=True,null=True, max_length=50,choices=TYPE_CHOICES)
    price = models.FloatField('商品价格',blank=True,null=True,default=0)
    discount_fee = models.FloatField('系统优惠金额',blank=True,null=True,default=0)
    total_fee = models.CharField('商品金额',blank=True,null=True, max_length=50)
    alipay_no = models.CharField('支付宝交易号',blank=True,null=True, max_length=50)
    buyer_nick  = models.CharField('买家昵称',blank=True,null=True, max_length=50)
    buyer_area  = models.CharField('买家下单的地区',blank=True,null=True, max_length=50)
    yfx_fee = models.CharField('订单的运费险，单位为元',blank=True,null=True, max_length=50)
    yfx_id  = models.CharField('运费险支付号',blank=True,null=True, max_length=50)
    yfx_type  = models.CharField('运费险类型',blank=True,null=True, max_length=50)
    step_paid_fee = models.CharField('分阶段付款的已付金额（万人团订单已付金额)',blank=True,null=True, max_length=50)
    mark_desc = models.CharField('订单出现异常问题的时候，给予用户的描述,没有异常的时候，此值为空',blank=True,null=True, max_length=50)
    send_time = models.CharField('订单将在此时间前发出，主要用于预售订单',blank=True,null=True, max_length=50)
    shipping_type = models.CharField('创建交易时的物流方式',blank=True,null=True, max_length=50)
    adjust_fee  = models.CharField('卖家手工调整金额',blank=True,null=True, max_length=50)
    cod_fee = models.CharField('货到付款服务费',blank=True,null=True, max_length=50)
    trade_from  = models.CharField('交易内部来源',blank=True,null=True, max_length=50)
    cod_status  = models.CharField('货到付款物流状态',blank=True,null=True, max_length=50)
    commission_fee  = models.CharField('交易佣金',blank=True,null=True, max_length=50)
    receiver_city = models.CharField('收货人所在城市',blank=True,null=True, max_length=50)
    receiver_district = models.CharField('收货人所在地区',blank=True,null=True, max_length=50)
    
    num = models.IntegerField('商品购买数量',blank=True,null=True,default=0)
    # num_iid = models.IntegerField('商品数字编号',blank=True,null=True, max_length=50)
    point_fee = models.IntegerField('买家使用积分',blank=True,null=True,default=0, max_length=50)
    alipay_id = models.CharField('买家的支付宝id号',blank=True,null=True,default=0, max_length=50)
    buyer_obtain_point_fee  = models.IntegerField('买家获得积分',blank=True,null=True,default=0)
    real_point_fee  = models.IntegerField('买家实际使用积分',blank=True,null=True,default=0)
    consign_time  = models.DateTimeField('卖家发货时间',blank=True,null=True)
    created = models.DateTimeField('交易创建时间',blank=True,null=True)
    pay_time  = models.DateTimeField('付款时间',blank=True,null=True)
    modified  = models.DateTimeField('交易修改时间',blank=True,null=True)
    end_time  = models.DateTimeField('交易结束时间',blank=True,null=True)
    async_modified  = models.DateTimeField('同步到卖家库的时间',blank=True,null=True)
    is_part_consign = models.CharField('是否是多次发货的订单',blank=True,null=True, max_length=50)

    def  __cmp__(self,obj):
        if self.modified and obj.modified:
            cmp_result = cmp(str(self.modified),str(obj.modified))
            # print 'compare',str(self.modified),str(obj.modified),cmp_result
            return cmp_result
        else:
            return -1

    def __unicode__(self):
        return u'主订单%s' %self.tid

    class Meta:
        verbose_name = u"主订单"
        verbose_name_plural = u"主订单"

class Shipping(models.Model):
    """物流"""
    buyer_nick= models.CharField('买家昵称',blank=True,null=True,max_length=100)
    address= models.CharField('买家地址',blank=True,null=True,max_length=100)
    city= models.CharField('收货市',blank=True,null=True,max_length=100)
    district= models.CharField('收货区',blank=True,null=True,max_length=100)
    state= models.CharField('收货省',blank=True,null=True,max_length=100)
    receiver_mobile= models.CharField('收货人手机号',blank=True,null=True,max_length=100)
    receiver_name= models.CharField('收货人姓名',blank=True,null=True,max_length=100)
    receiver_phone= models.CharField('收货人电话',blank=True,null=True,max_length=100)
    tid= models.CharField('交易ID',blank=True,null=True,max_length=100)
    company_name= models.CharField('快递公司',blank=True,null=True,max_length=100)
    post_fee= models.FloatField('快递费用',blank=True,null=True,max_length=11)
    weight= models.FloatField('重量',blank=True,null=True,max_length=11)
    out_sid= models.CharField('快递单号', blank=True, null=True, max_length=100)
    trade = models.ForeignKey(TradeParent, verbose_name='主订单编号', null=True, blank=True)
    created = models.DateTimeField('运单创建时间', blank=True, null=True)
    modified = models.DateTimeField('运单修改时间', blank=True, null=True)
    # is_verify = models.NullBooleanField('审核结果',default=False)

    def get_trade_status(self):
        if self.trade is not  None:
            for status,verbose_name in STATUS_CHOICES:
                if status == self.trade.status:
                    return verbose_name
        return 'None'
    get_trade_status.short_description = u'订单状态'

    def __unicode__(self):
        return '%s-%s' %(self.company_name,self.out_sid)

    class Meta:
        verbose_name = u"快递"
        verbose_name_plural = u"快递"

class Order(models.Model):
    """子订单"""

    buyer_rate = models.CharField('买家是否已评价',blank=True,null=True,max_length=100)
    num_iid = models.CharField('商品数字ID',blank=True,null=True,max_length=100)
    oid = models.CharField('子订单编号',blank=True,null=True,max_length=100)
    outer_iid = models.CharField('商家外部条码',blank=True,null=True,max_length=100)
    refund_status = models.CharField('退款状态',blank=True,null=True,max_length=100)
    seller_type = models.CharField('卖家类型',blank=True,null=True,max_length=100)
    status = models.CharField('订单状态',blank=True,null=True,max_length=100,choices=STATUS_CHOICES)
    title = models.CharField('商品标题',blank=True,null=True,max_length=200)
    num = models.IntegerField('购买数量',default=0,blank=True,null=True)
    adjust_fee = models.FloatField('手工调整金额',default=0,blank=True,null=True)
    discount_fee = models.FloatField('子订单级订单优惠金额',default=0,blank=True,null=True)
    payment = models.FloatField('子订单实付金额',default=0,blank=True,null=True)
    price = models.FloatField('商品价格',default=0,blank=True,null=True)
    total_fee = models.FloatField('应付金额',default=0,blank=True,null=True)
    trade = models.ForeignKey(TradeParent, verbose_name='主订单编号')

    def __unicode__(self):
        return 'Order %s' %self.oid

    class Meta:
        verbose_name = u"子订单"
        verbose_name_plural = u"子订单"

class Danpin(models.Model):
    """单品"""
    bianhao         = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品编号')
    pinming         = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'品名')
    leixing            = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'类型')
    f5                   = models.CharField(db_column='F5', max_length=255, blank=True,null=True,verbose_name=u'') 
    tiaoma           = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'条码')
    guige             = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'规格')
    danwei          = models.CharField(max_length=20, blank=True,null=True,verbose_name=u'单位')
    zhongliang    = models.FloatField( verbose_name=u'重量')
    purchase_price    = models.FloatField( verbose_name=u'进价')



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

    def get_purchase_price(self):
        """套餐进价"""
        pkgProduct_details = self.packagedetail_set.all()
        #单品费用比率 = 单品数量*单品进价 / 套餐进价
        taocan_all_amount = 0
        
        for detail in pkgProduct_details :
            #单品金额=单品进价 * 单品个数
            single_all_amount = detail.single_product.purchase_price * detail.single_product_count
            #套餐进价 = 多个（单品数量*单品进价)
            taocan_all_amount= taocan_all_amount + single_all_amount

        return taocan_all_amount

    def get_signPro_ratio(self):

        pkgProduct_details = self.packagedetail_set.all()
        
        #单品费用比率 = 单品数量*单品进价 / 套餐进价

        xmap = {}
        taocan_all_amount = 0
        
        for detail in pkgProduct_details :
            #单品金额=单品进价 * 单品个数
            single_all_amount = detail.single_product.purchase_price * detail.single_product_count
            xmap[detail.single_product] = single_all_amount
            #套餐进价 = 多个（单品数量*单品进价)
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
    in_pocke_post_fee            = models.FloatField(blank=True,null=True,verbose_name=u'实收快递费')
    out_pocke_post_fee          = models.FloatField(blank=True,null=True,verbose_name=u'实付快递费')


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


        print self.tiaoxingma
        if pkg_pros.count() == 0 :
            single_product = Danpin.objects.get(tiaoma=self.tiaoxingma)
            order_detail = DingdanDetail()
            order_detail.initInfos(self,single_product.bianhao,self.dinghuo_shuliang,self.chanpin_chengjiaojine )
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
        self.in_pocke_post_fee = ptrDingdan.in_pocke_post_fee
        self.out_pocke_post_fee = ptrDingdan.out_pocke_post_fee





    dingdan = models.ForeignKey(Dingdan,verbose_name=u'订单')
    
    danpin_huohao = models.CharField(max_length=255, blank=True,null=True,verbose_name=u'单品货号')
    danpin_count = models.IntegerField(null=True,verbose_name=u'单品数量')
    danpin_jiage = models.FloatField( verbose_name=u'单品分拆价格')

    def __unicode__(self) :
        return 'Order_Detail %s' % self.dingdan_bianhao
    class Meta:
        verbose_name             = u"订单详情"
        verbose_name_plural  = u"订单详情"
        
        db_table                        = 'dingdan_detail'
        # ordering = ['fukuan_date']


