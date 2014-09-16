# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TradeParent'
        db.create_table(u'quanlin_tradeparent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('seller_nick', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('payment', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('out_post_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('post_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('receiver_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_address', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('receiver_zip', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_mobile', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('received_payment', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('discount_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('total_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('alipay_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('buyer_nick', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('buyer_area', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('yfx_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('yfx_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('yfx_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('step_paid_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mark_desc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('send_time', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('shipping_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('adjust_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('cod_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('trade_from', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('cod_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('commission_fee', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('receiver_district', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('point_fee', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=50, null=True, blank=True)),
            ('alipay_id', self.gf('django.db.models.fields.CharField')(default=0, max_length=50, null=True, blank=True)),
            ('buyer_obtain_point_fee', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('real_point_fee', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('consign_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('pay_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('async_modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_part_consign', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'quanlin', ['TradeParent'])

        # Adding model 'Order'
        db.create_table(u'quanlin_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('buyer_rate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('num_iid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('oid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('outer_iid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('refund_status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('seller_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('adjust_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('discount_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('payment', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('total_fee', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('trade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quanlin.TradeParent'])),
        ))
        db.send_create_signal(u'quanlin', ['Order'])

        # Adding model 'Danpin'
        db.create_table(u'danpin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pinming', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('leixing', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('f5', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_column=u'F5', blank=True)),
            ('tiaoma', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('guige', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('danwei', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('zhongliang', self.gf('django.db.models.fields.FloatField')()),
            ('purchase_price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'quanlin', ['Danpin'])

        # Adding model 'Taocan'
        db.create_table(u'taocan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pinming', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('leixing', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tiaoma', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('guige', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('danwei', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zhongliang', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'quanlin', ['Taocan'])

        # Adding model 'Dingdan'
        db.create_table(u'dingdan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chanpin_baojia', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_baojia_zongjine', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('chanpin_chengjiaojine', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('chanpinchengjiao_danjia', self.gf('django.db.models.fields.FloatField')()),
            ('chanpinzhongliang_xiaoji', self.gf('django.db.models.fields.FloatField')()),
            ('chulizhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dianpumingcheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dingdan_bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dingdan_jingzhong', self.gf('django.db.models.fields.FloatField')()),
            ('dinghuo_shuliang', self.gf('django.db.models.fields.FloatField')()),
            ('fahuo_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('fahuozhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fukuan_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('fukuanzhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('gui_ge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('kuaidi_danhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('kuaidi_gongsi_mingcheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('maijia_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('order_paid_amount', self.gf('django.db.models.fields.FloatField')()),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pingtai_fahuo_zhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('print_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('qianshou_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shendan_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('shouhuo_dizhi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_ren', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_sheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_shi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_xian', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tiaoxingma', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('waibu_danhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('wangdian_pinming', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('in_pocke_post_fee', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('out_pocke_post_fee', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'quanlin', ['Dingdan'])

        # Adding model 'PackageDetail'
        db.create_table(u'quanlin_packagedetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quanlin.Taocan'])),
            ('single_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quanlin.Danpin'])),
            ('single_product_count', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'quanlin', ['PackageDetail'])

        # Adding model 'DingdanDetail'
        db.create_table(u'dingdan_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chanpin_baojia', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_baojia_zongjine', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('chanpin_chengjiaojine', self.gf('django.db.models.fields.FloatField')()),
            ('chanpin_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('chanpinchengjiao_danjia', self.gf('django.db.models.fields.FloatField')()),
            ('chanpinzhongliang_xiaoji', self.gf('django.db.models.fields.FloatField')()),
            ('chulizhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dianpumingcheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dingdan_bianhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dingdan_jingzhong', self.gf('django.db.models.fields.FloatField')()),
            ('dinghuo_shuliang', self.gf('django.db.models.fields.FloatField')()),
            ('fahuo_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('fahuozhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fukuan_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('fukuanzhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('gui_ge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('kuaidi_danhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('kuaidi_gongsi_mingcheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('maijia_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('order_paid_amount', self.gf('django.db.models.fields.FloatField')()),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pingtai_fahuo_zhuangtai', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('print_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('qianshou_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shendan_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('shouhuo_dizhi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_ren', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_sheng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_shi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('shouhuo_xian', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tiaoxingma', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('waibu_danhao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('wangdian_pinming', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('in_pocke_post_fee', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('out_pocke_post_fee', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dingdan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quanlin.Dingdan'])),
            ('danpin_huohao', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('danpin_count', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('danpin_jiage', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'quanlin', ['DingdanDetail'])


    def backwards(self, orm):
        # Deleting model 'TradeParent'
        db.delete_table(u'quanlin_tradeparent')

        # Deleting model 'Order'
        db.delete_table(u'quanlin_order')

        # Deleting model 'Danpin'
        db.delete_table(u'danpin')

        # Deleting model 'Taocan'
        db.delete_table(u'taocan')

        # Deleting model 'Dingdan'
        db.delete_table(u'dingdan')

        # Deleting model 'PackageDetail'
        db.delete_table(u'quanlin_packagedetail')

        # Deleting model 'DingdanDetail'
        db.delete_table(u'dingdan_detail')


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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'step_paid_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trade_from': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_fee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'yfx_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quanlin']