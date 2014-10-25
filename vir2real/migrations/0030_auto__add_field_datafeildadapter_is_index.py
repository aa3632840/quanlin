# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataFeildAdapter.is_index'
        db.add_column(u'vir2real_datafeildadapter', 'is_index',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataFeildAdapter.is_index'
        db.delete_column(u'vir2real_datafeildadapter', 'is_index')


    models = {
        u'vir2real.dataadapter': {
            'Meta': {'object_name': 'DataAdapter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'real_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealClass']"})
        },
        u'vir2real.datafeildadapter': {
            'Meta': {'object_name': 'DataFeildAdapter'},
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'real_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealFeild']"})
        },
        u'vir2real.person': {
            'Meta': {'object_name': 'Person'},
            'alipay_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'qq_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'vir2real.quickaddjob': {
            'Meta': {'object_name': 'QuickAddJob'},
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            'data_adapter_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'vir2real.realclass': {
            'Meta': {'object_name': 'RealClass'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'has_generate_fields': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.realfeild': {
            'Meta': {'object_name': 'RealFeild'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'null': ('django.db.models.fields.BooleanField', [], {'max_length': '50'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealClass']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.realfieldalias': {
            'Meta': {'object_name': 'RealFieldAlias'},
            'alias_choice': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'alias_key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'real_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealFeild']"})
        },
        u'vir2real.virtual2realadapterclassmap': {
            'Meta': {'object_name': 'Virtual2RealAdapterClassMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'real_class_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'virtual_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualClass']"})
        },
        u'vir2real.virtual2realadapterfieldmap': {
            'Meta': {'object_name': 'Virtual2RealAdapterFieldMap'},
            'class_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.Virtual2RealAdapterClassMap']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'real_field_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'virtual_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualFeild']"})
        },
        u'vir2real.virtualclass': {
            'Meta': {'object_name': 'VirtualClass'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.virtualdata': {
            'Meta': {'object_name': 'VirtualData'},
            'can_be_restore_real': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            'erro_msg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quick_job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.QuickAddJob']", 'null': 'True', 'blank': 'True'}),
            'source_json': ('django.db.models.fields.TextField', [], {}),
            'source_line': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        u'vir2real.virtualfeild': {
            'Meta': {'object_name': 'VirtualFeild'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualClass']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'TYPE_CHAR'", 'max_length': '50'})
        }
    }

    complete_apps = ['vir2real']