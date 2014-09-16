# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Shipping.address'
        db.add_column(u'quanlin_shipping', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.city'
        db.add_column(u'quanlin_shipping', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.district'
        db.add_column(u'quanlin_shipping', 'district',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.state'
        db.add_column(u'quanlin_shipping', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.receiver_mobile'
        db.add_column(u'quanlin_shipping', 'receiver_mobile',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.receiver_name'
        db.add_column(u'quanlin_shipping', 'receiver_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.receiver_phone'
        db.add_column(u'quanlin_shipping', 'receiver_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.tid'
        db.add_column(u'quanlin_shipping', 'tid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.company_name'
        db.add_column(u'quanlin_shipping', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.out_sid'
        db.add_column(u'quanlin_shipping', 'out_sid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Shipping.trade'
        db.add_column(u'quanlin_shipping', 'trade',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quanlin.TradeParent'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Shipping.address'
        db.delete_column(u'quanlin_shipping', 'address')

        # Deleting field 'Shipping.city'
        db.delete_column(u'quanlin_shipping', 'city')

        # Deleting field 'Shipping.district'
        db.delete_column(u'quanlin_shipping', 'district')

        # Deleting field 'Shipping.state'
        db.delete_column(u'quanlin_shipping', 'state')

        # Deleting field 'Shipping.receiver_mobile'
        db.delete_column(u'quanlin_shipping', 'receiver_mobile')

        # Deleting field 'Shipping.receiver_name'
        db.delete_column(u'quanlin_shipping', 'receiver_name')

        # Deleting field 'Shipping.receiver_phone'
        db.delete_column(u'quanlin_shipping', 'receiver_phone')

        # Deleting field 'Shipping.tid'
        db.delete_column(u'quanlin_shipping', 'tid')

        # Deleting field 'Shipping.company_name'
        db.delete_column(u'quanlin_shipping', 'company_name')

        # Deleting field 'Shipping.out_sid'
        db.delete_column(u'quanlin_shipping', 'out_sid')

        # Deleting field 'Shipping.trade'
        db.delete_column(u'quanlin_shipping', 'trade_id')


    models = {
        u'quanlin.danpin': {
            'Meta': {'object_name': 'Danpin', 'db_table': "u'danpin'"},
            'bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'danwei': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'f5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'F5'", 'blank': 'True'}),
            'guige': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leixing': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pinming': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'purchase_price': ('django.db.models.fields.FloatField', [], {}),
            'tiaoma': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zhongliang': ('django.db.models.fields.FloatField', [], {})
        },
        u'quanlin.dingdan': {
            'Meta': {'object_name': 'Dingdan', 'db_table': "u'dingdan'"},
            'chanpin_baojia': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_baojia_zongjine': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chanpin_chengjiaojine': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chanpinchengjiao_danjia': ('django.db.models.fields.FloatField', [], {}),
            'chanpinzhongliang_xiaoji': ('django.db.models.fields.FloatField', [], {}),
            'chulizhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dianpumingcheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dingdan_bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dingdan_jingzhong': ('django.db.models.fields.FloatField', [], {}),
            'dinghuo_shuliang': ('django.db.models.fields.FloatField', [], {}),
            'fahuo_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fahuozhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fukuan_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fukuanzhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gui_ge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_pocke_post_fee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'kuaidi_danhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'kuaidi_gongsi_mingcheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'maijia_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order_paid_amount': ('django.db.models.fields.FloatField', [], {}),
            'out_pocke_post_fee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pingtai_fahuo_zhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'print_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'qianshou_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shendan_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'shouhuo_dizhi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_ren': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_sheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_shi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_xian': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tiaoxingma': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'waibu_danhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wangdian_pinming': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'quanlin.dingdandetail': {
            'Meta': {'object_name': 'DingdanDetail', 'db_table': "u'dingdan_detail'"},
            'chanpin_baojia': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_baojia_zongjine': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chanpin_chengjiaojine': ('django.db.models.fields.FloatField', [], {}),
            'chanpin_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chanpinchengjiao_danjia': ('django.db.models.fields.FloatField', [], {}),
            'chanpinzhongliang_xiaoji': ('django.db.models.fields.FloatField', [], {}),
            'chulizhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'danpin_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'danpin_huohao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'danpin_jiage': ('django.db.models.fields.FloatField', [], {}),
            'dianpumingcheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dingdan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quanlin.Dingdan']"}),
            'dingdan_bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dingdan_jingzhong': ('django.db.models.fields.FloatField', [], {}),
            'dinghuo_shuliang': ('django.db.models.fields.FloatField', [], {}),
            'fahuo_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fahuozhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fukuan_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fukuanzhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gui_ge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_pocke_post_fee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'kuaidi_danhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'kuaidi_gongsi_mingcheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'maijia_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order_paid_amount': ('django.db.models.fields.FloatField', [], {}),
            'out_pocke_post_fee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pingtai_fahuo_zhuangtai': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'print_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'qianshou_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shendan_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'shouhuo_dizhi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_ren': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_sheng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_shi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'shouhuo_xian': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tiaoxingma': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'waibu_danhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wangdian_pinming': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'quanlin.order': {
            'Meta': {'object_name': 'Order'},
            'adjust_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'buyer_rate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'discount_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'num_iid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'oid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'outer_iid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payment': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'refund_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'seller_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'trade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quanlin.TradeParent']"})
        },
        u'quanlin.packagedetail': {
            'Meta': {'object_name': 'PackageDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package_product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quanlin.Taocan']"}),
            'single_product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quanlin.Danpin']"}),
            'single_product_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        },
        u'quanlin.shipping': {
            'Meta': {'object_name': 'Shipping'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'buyer_nick': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'out_sid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'receiver_mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'receiver_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'receiver_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quanlin.TradeParent']", 'null': 'True', 'blank': 'True'})
        },
        u'quanlin.taocan': {
            'Meta': {'object_name': 'Taocan', 'db_table': "u'taocan'"},
            'bianhao': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'danwei': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'guige': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leixing': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pinming': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tiaoma': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zhongliang': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'quanlin.tradeparent': {
            'Meta': {'object_name': 'TradeParent'},
            'adjust_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'alipay_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'alipay_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'async_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'buyer_area': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'buyer_nick': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'buyer_obtain_point_fee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'cod_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cod_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'commission_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'consign_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'discount_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_part_consign': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mark_desc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'out_post_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'pay_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'payment': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'point_fee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'post_fee': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'real_point_fee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'received_payment': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'receiver_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'receiver_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receiver_zip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'seller_nick': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'send_time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shipping_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shop': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'step_paid_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trade_from': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trade_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quanlin']