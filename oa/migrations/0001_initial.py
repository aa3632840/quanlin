# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'oa_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'oa', ['Group'])

        # Adding model 'Person'
        db.create_table(u'oa_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('qq_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('alipay_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Group'], null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'oa', ['Person'])

        # Adding model 'DeviceType'
        db.create_table(u'oa_devicetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'oa', ['DeviceType'])

        # Adding model 'Device'
        db.create_table(u'oa_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('device_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.DeviceType'])),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('buy_date', self.gf('django.db.models.fields.DateField')()),
            ('use_date', self.gf('django.db.models.fields.DateField')()),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'oa', ['Device'])

        # Adding M2M table for field user on 'Device'
        m2m_table_name = db.shorten_name(u'oa_device_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('device', models.ForeignKey(orm[u'oa.device'], null=False)),
            ('person', models.ForeignKey(orm[u'oa.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['device_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'oa_group')

        # Deleting model 'Person'
        db.delete_table(u'oa_person')

        # Deleting model 'DeviceType'
        db.delete_table(u'oa_devicetype')

        # Deleting model 'Device'
        db.delete_table(u'oa_device')

        # Removing M2M table for field user on 'Device'
        db.delete_table(db.shorten_name(u'oa_device_user'))


    models = {
        u'oa.device': {
            'Meta': {'object_name': 'Device'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'buy_date': ('django.db.models.fields.DateField', [], {}),
            'device_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.DeviceType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'use_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['oa.Person']", 'symmetrical': 'False'})
        },
        u'oa.devicetype': {
            'Meta': {'object_name': 'DeviceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'oa.group': {
            'Meta': {'object_name': 'Group'},
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