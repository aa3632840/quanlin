# -*- coding: utf-8 -*-  
from django_cron import CronJobBase, Schedule
from django.utils import timezone
from models import Dingdan,DingdanDetail,TradeParent,Order
from lxml import etree

class EchoTarget(object):

    def __init__(self):
        self.trades = []
        self.cur_trade = None
        self.cur_tag = None
        self.cur_order = None

    def start(self, tag, attrib):
        if tag == 'trade' :
            self.cur_trade = TradeParent()
            # print("start %s %r" % (tag, dict(attrib)))
        if tag == 'orders' :
            self.cur_trade.orders = []

        if tag == 'order':
             self.cur_order = Order()
        # print("start %s %r" % (tag, dict(attrib)))
        self.cur_tag = tag

    def end(self, tag):

        if tag == 'trade' :
            self.trades.append(self.cur_trade)
            # print("end %s" % tag)
            self.cur_trade = None

        elif tag == 'order' :
            self.cur_order.trade = self.cur_trade
            self.cur_trade.orders.append(self.cur_order)
            self.cur_order = None

        self.cur_tag = None
        

    def data(self, data):

        if self.cur_tag and hasattr(self.cur_order, self.cur_tag):
            setattr(self.cur_order, self.cur_tag, data)

        elif self.cur_tag and hasattr(self.cur_trade, self.cur_tag):
            setattr(self.cur_trade, self.cur_tag, data)
        # print("data %r" % data)

    def comment(self, text):
        print("comment %s" % text)

    def close(self):
        print("close")
        return "closed!"

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.01 # every 2 hours
    MIN_NUM_FAILURES = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'quanlin.my_cron_job'    # a unique code

    def do(self):

         cur_time = timezone.datetime.now()
         print cur_time
         # self.parse_xml_2_database()

    def parse_xml_2_database(self):
        ql_url = 'http://gw.api.taobao.com/router/rest?sign=073CA56B452401FFEDE229858015BB24&timestamp=2014-09-08+14%3A39%3A47&v=2.0&app_key=21008274&method=taobao.trades.sold.get&partner_id=top-apitools&session=700001015396275a071b4d2e4577db9567f950815adb624098a163fadfe389107ac81962098388851&format=xml&page_size=50000&start_created=2014-06-01+00%3A00%3A00&end_created=2014-10-01+00%3A00%3A00&fields=seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time,end_time,modified,consign_time,buyer_obtain_point_fee,point_fee,real_point_fee,received_payment,commission_fee,pic_path,num_iid,num_iid,num,price,cod_fee,cod_status,shipping_type,receiver_name,receiver_state,receiver_city,receiver_district,receiver_address,receiver_zip,receiver_mobile,receiver_phone,orders.title,orders.pic_path,orders.price,orders.num,orders.iid,orders.num_iid,orders.sku_id,orders.refund_status,orders.status,orders.oid,orders.total_fee,orders.payment,orders.discount_fee,orders.adjust_fee,orders.sku_properties_name,orders.item_meal_name,orders.buyer_rate,orders.seller_rate,orders.outer_iid,orders.outer_sku_id,orders.refund_id,orders.seller_type'
        import urllib
        # urllib.urlretrieve(ql_url, 'all2.xml')

        # xmlStr = open('tmall_all.xml', mode='r').read()
        xmlStr = open('all2.xml', mode='r').read()
        # xmlStr = open('quanlin.xml', mode='r').read()
        # print xmlStr
        parser = etree.XMLParser(target=EchoTarget())
        result = etree.XML(xmlStr, parser)
        print len(parser.target.trades)
        trade_list = parser.target.trades
        for trade in trade_list:
            tid = trade.tid
            orders = trade.orders
            pauseTrades = TradeParent.objects.filter(tid=tid)


            #如果有多条，则删除多条，并只留下这一个
            if pauseTrades.count() > 1:
                pauseTrades.delete()
                trade.save()
            elif pauseTrades.count() == 1:
                pause_trade = pauseTrades[0]

                #比对修改时间，如果trade比较新，则替换
                if cmp( trade,pause_trade) > 0 :
                    print u'%s 比较新' %tid
                    pause_trade.delete()
                    trade.save()
                #如果 trade无改变或者比较旧，则用数据库里的当最新的
                else:
                    # print u'xml比较旧'
                    trade = pause_trade
            else:
                    #如果没有此数据，则插入
                    trade.save()
            for order in orders:
                order.trade = trade
                order.save()
            # trade.order_set = trade.orders
         
        
    def sync_dingdan_details(self):
         """更新订单详情"""
         dds = Dingdan.objects.all()
         for dd in dds:
            print dd
            print dd.saveOrderDetails()
         print cur_time