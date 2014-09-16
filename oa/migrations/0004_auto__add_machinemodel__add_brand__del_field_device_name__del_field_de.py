# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MachineModel'
        db.create_table(u'oa_machinemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('device_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.DeviceType'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Brand'])),
        ))
        db.send_create_signal(u'oa', ['MachineModel'])

        # Adding model 'Brand'
        db.create_table(u'oa_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'oa', ['Brand'])

        # Deleting field 'Device.name'
        db.delete_column(u'oa_device', 'name')

        # Deleting field 'DeviceType.type_name'
        db.delete_column(u'oa_devicetype', 'type_name')

        # Adding field 'DeviceType.name'
        db.add_column(u'oa_devicetype', 'name',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=50),
                      keep_default=False)

        # Adding M2M table for field brand on 'DeviceType'
        m2m_table_name = db.shorten_name(u'oa_devicetype_brand')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('devicetype', models.ForeignKey(orm[u'oa.devicetype'], null=False)),
            ('brand', models.ForeignKey(orm[u'oa.brand'], null=False))
        ))
        db.create_unique(m2m_table_name, ['devicetype_id', 'brand_id'])


    def backwards(self, orm):
        # Deleting model 'MachineModel'
        db.delete_table(u'oa_machinemodel')

        # Deleting model 'Brand'
        db.delete_table(u'oa_brand')

        # Adding field 'Device.name'
        db.add_column(u'oa_device', 'name',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=50),
                      keep_default=False)

        # Adding field 'DeviceType.type_name'
        db.add_column(u'oa_devicetype', 'type_name',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=50),
                      keep_default=False)

        # Deleting field 'DeviceType.name'
        db.delete_column(u'oa_devicetype', 'name')

        # Removing M2M table for field brand on 'DeviceType'
        db.delete_table(db.shorten_name(u'oa_devicetype_brand'))


    models = {
        u'oa.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.device': {
            'Meta': {'object_name': 'Device'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'buy_date': ('django.db.models.fields.DateField', [], {}),
            'device_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.DeviceType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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