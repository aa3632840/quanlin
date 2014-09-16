# -*- coding: utf-8 -*-  
from django_cron import CronJobBase, Schedule
from quanlin.models import Dingdan,DingdanDetail,TradeParent,Order,Shipping
from lxml import etree
import json
import top.api
import datetime
import pickle

appkey = '21008274'
secret = '7975defa67b6ddae14e10d324eaedbf4'
sessionkey = '700001015396275a071b4d2e4577db9567f950815adb624098a163fadfe389107ac81962098388851'



class TaobaoDownTradeCronJob(CronJobBase):
    code = 'quanlin.down_trade_engins.TaobaoDownTradeCronJob'    # a unique code
    RUN_EVERY_MINS = 0.01 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)


    

    def do(self):
        self.down_all_shippings()
        # self.down_all_trades()

        # resp = None

        #测试 get_orders_from_dict
        # print self.get_orders_from_dict(resp,test=True)

        #测试get_trade_from_dict
        # print self.get_trade_from_dict(None, test=True)

        #测试 get_trade_from_resp
        # trade_list = self.get_trades_from_resp(None,test=True)
        # for trade in trade_list :
        #     print trade
        # print trade_list
        # self.insert_trade_2_models(trade_list)

    def insert_trade_2_models(self,trade_list):
        for trade in trade_list:
            tid = trade.tid
            
            pauseTrades = TradeParent.objects.filter(tid=tid)

            #如果有多条，则删除多条，并只留下这一个
            if pauseTrades.count() > 1:
                print u'%s 清除脏数据' %tid
                pauseTrades.delete()
                trade.save()
            elif pauseTrades.count() == 1:
                pause_trade = pauseTrades[0]

                #比对修改时间，如果trade比较新，则替换
                # print cmp( trade,pause_trade) 
                if cmp( trade,pause_trade) > 0 :
                    print u'%s 比较新' %tid
                    pause_trade.delete()
                    trade.save()
                #如果 trade无改变或者比较旧，则用数据库里的当最新的
                else:
                    # print u'%s 旧数据,不执行插入' %tid
                    trade = pause_trade
                    trade.orders = []
            else:
                    #如果没有此数据，则插入
                    print u'新数据插入 %s' %tid
                    trade.save()

            orders = trade.orders
            for order in orders:
                order.trade = trade
                order.save()
            # trade.order_set = trade.orders
         

    def get_orders_from_dict(self,orders_dict,trade=None,test=False):
        """生成 Orders"""
        if test:
            with open('bak\\order.pickle', 'rb') as f:
                orders_dict = pickle.load(f)       
        if orders_dict:
            orders = []

            for order_map in orders_dict:
                # print '*'* 40
                order = Order()
                for order_key in order_map:
                    value = order_map[order_key]
                    if hasattr(order, order_key):
                        # print '                     setattr(%s,%s)' %(order_key,value)
                        setattr(order, order_key, order_map[order_key])
                    else:
                        # print 'xxxxxxxxx order trade_key not exits==>',order_key
                        pass
                if trade: order.trade= trade
                orders.append(order)
            return orders

    def get_trade_from_dict(self,trade_dict,test=False):
        if test:
            with open('bak\\trade.pickle', 'rb') as f:
                trade_dict = pickle.load(f)
                print trade_dict
        # print '-'* 40
        trade = TradeParent()
        for trade_key in trade_dict:

            value = trade_dict[trade_key] 
            if trade_key == 'type' : trade_key = 'trade_type'

            if hasattr(trade, trade_key):
                # print 'setattr == %s==>%s ' %(trade_key,value)
                setattr(trade, trade_key, value)

            if trade_key== 'orders':
                orders_dict = trade_dict['orders']['order']
                trade.orders = self.get_orders_from_dict(orders_dict,trade=trade)

        return trade

    def get_trades_from_resp(self,resp_dict=None,resp_dict_file=None,shop=None,test=False):
        """将数据插入到数据库Trade中"""
        if test :
            with open('bak\\page_1.pickle', 'rb') as f:
                resp_dict = pickle.load(f)

        if resp_dict_file:
            with open(resp_dict_file, 'rb') as f:
                resp_dict = pickle.load(f)

        # print(str(resp_dict))
        trades_sold_get_response = resp_dict['trades_sold_get_response']
        total_results = trades_sold_get_response['total_results']
        trade_map_list = trades_sold_get_response['trades']['trade']
        print len(trade_map_list)

        trade_list = []
        for trade_map in trade_map_list:
            #生成 Trades
            trade = self.get_trade_from_dict(trade_map)
            if shop : trade.shop = shop
            trade_list.append(trade)        
        return trade_list

    def get_shipping_from_dict(self,shipping_dict):
        """解析shipping"""
        # print '*'*40
        shipping = Shipping()
        for shipping_key in shipping_dict:
            value = shipping_dict[shipping_key]

            if shipping_key == 'location':

                location_dict= shipping_dict['location']
                for location_key in location_dict:
                    value= location_dict[location_key]
                    if hasattr(shipping, location_key):
                        # print '                     setattr %s == >%s ' %(location_key,value)
                        setattr(shipping, location_key, value)
            else:
                    if hasattr(shipping, shipping_key):
                        # print ' setattr %s == >%s' %(shipping_key,value)
                        setattr(shipping, shipping_key, value)
        trades = TradeParent.objects.filter(tid=shipping.tid).all()
        if trades.count()==1:
            shipping.trade = trades[0]
        return shipping

    def get_shippings_from_dict(self,resp):
            shippings_dict = resp['logistics_orders_detail_get_response']['shippings']['shipping']
            shipping_list= []
            for shipping_dict in shippings_dict:
                # print '-'*40
                shipping = self.get_shipping_from_dict(shipping_dict)

                if hasattr(shipping, 'out_sid') and shipping.out_sid is not None:
                    shipping_list.append(shipping)

            return shipping_list

    def get_page_count(self,total_results,page_size):
        """计算页数"""
        return total_results/page_size+1

    def insert_shipping_2_models(self, shippings):
        """插入shippings"""
        print len(shippings)
        for shipping in shippings:
            same_shippings= Shipping.objects.filter(out_sid=shipping.out_sid)

            if same_shippings.count()==0:
                print u'保存新数据 %s' %shipping.out_sid
                shipping.save()
            elif same_shippings.count()==1:
                print u'旧数据，不作任何操作 %s' %shipping.out_sid
                # shipping.save()
            elif same_shippings.count()>1:
                print u'删除重复数据，并添加新数据 %s' %shipping.out_sid
                same_shippings.delete()
                shipping.save()

    def down_all_shippings(self):
        req= top.api.LogisticsOrdersDetailGetRequest()
        req.set_app_info(top.appinfo(appkey,secret))

        get_total_result_fields="total_results"
        req_fields="tid,order_code,company_name,out_sid,buyer_nick,receiver_name,receiver_mobile,receiver_phone,receiver_location"
        req.start_created="2014-06-16 00:00:00"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print 'get shipping from %s to %s' %(req.start_created,now) 
        req.end_created= now
        req.page_size=10
        req.page_no= 1
        req.fields = get_total_result_fields
        try:
            resp= req.getResponse(sessionkey)
            print resp
            logistics_orders_detail_get_response = resp['logistics_orders_detail_get_response']
            total_results = logistics_orders_detail_get_response['total_results']
            print total_results
            page_nums = self.get_page_count(total_results, req.page_size)
            print 'page_nums',page_nums
            for page_no in range(1,page_nums+1):
                req.page_no= page_no
                # req.tid='798622968678334'
                req.fields = req_fields
                resp= req.getResponse(sessionkey)
                shipping_list = self.get_shippings_from_dict(resp)

                self.insert_shipping_2_models(shipping_list)
                            

            # print(resp)
        except Exception,e:
            print(e)

    def down_all_trades(self):
        """下载所有订单"""
        top.setDefaultAppInfo(appkey,secret)
        req = top.api.TradesSoldGetRequest()
        req.start_created= "2014-06-16 00:00:00"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print 'get trades from %s to %s' %(req.start_created,now) 
        req.end_created= now
        req.page_no= 1
        req.page_size= 50
        get_fields="seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time,end_time,modified,consign_time,buyer_obtain_point_fee,point_fee,real_point_fee,received_payment,commission_fee,pic_path,num_iid,num_iid,num,price,cod_fee,cod_status,shipping_type,receiver_name,receiver_state,receiver_city,receiver_district,receiver_address,receiver_zip,receiver_mobile,receiver_phone,orders.title,orders.pic_path,orders.price,orders.num,orders.iid,orders.num_iid,orders.sku_id,orders.refund_status,orders.status,orders.oid,orders.total_fee,orders.payment,orders.discount_fee,orders.adjust_fee,orders.sku_properties_name,orders.item_meal_name,orders.buyer_rate,orders.seller_rate,orders.outer_iid,orders.outer_sku_id,orders.refund_id,orders.seller_type"
        req.fields = 'total_results'

        try:
            resp= req.getResponse(sessionkey)

            print resp
            trades_sold_get_response = resp['trades_sold_get_response']

            #共有多少条订单
            total_results = trades_sold_get_response['total_results']

            req.fields = get_fields

            #分页
            page_nums = total_results/req.page_size+1
            pickle_files = []
            for i in range(page_nums):
                req.page_no= i+1
                print 'loading trades page No.%s'  %req.page_no
                pickle_fname = 'bak\\page_%s.pickle' %req.page_no
                rep = req.getResponse(sessionkey)

                with open(pickle_fname, 'wb') as f:
                    pickle.dump(rep, f, pickle.HIGHEST_PROTOCOL)
                    pickle_files.append(pickle_fname)


            for pickle_f in pickle_files:
                trade_list = self.get_trades_from_resp(resp_dict_file=pickle_f,shop=TradeParent.SHOP_TM)
                self.insert_trade_2_models(trade_list)
    
                # self.insert_into_trade_model(rep)

        except Exception,e:
            print(e)
