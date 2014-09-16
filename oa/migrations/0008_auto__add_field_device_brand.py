# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Device.brand'
        db.add_column(u'oa_device', 'brand',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Brand'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Device.brand'
        db.delete_column(u'oa_device', 'brand_id')


    models = {
        u'oa.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.device': {
            'Meta': {'object_name': 'Device'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Brand']", 'null': 'True', 'blank': 'True'}),
            'buy_date': ('django.db.models.fields.DateField', [], {}),
            'device_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.DeviceType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.MachineModel']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'use_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oa.Person']", 'symmetrical': 'False'})
        },
        u'oa.devicetype': {
            'Meta': {'object_name': 'DeviceType'},
            'brand': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oa.Brand']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.machinemodel': {
            'Meta': {'object_name': 'MachineModel'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Brand']"}),
            'device_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.DeviceType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.person': {
            'Meta': {'object_name': 'Person'},
            'alipay_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'qq_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['oa']