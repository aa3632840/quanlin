# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VirtualClass'
        db.create_table(u'vir2real_virtualclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualClass'])

        # Adding model 'VirtualFeild'
        db.create_table(u'vir2real_virtualfeild', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualClass'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='TYPE_CHAR', max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualFeild'])

        # Adding model 'Virtual2RealAdapterClassMap'
        db.create_table(u'vir2real_virtual2realadapterclassmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('virtual_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualClass'])),
            ('real_class_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['Virtual2RealAdapterClassMap'])

        # Adding model 'Virtual2RealAdapterFieldMap'
        db.create_table(u'vir2real_virtual2realadapterfieldmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.Virtual2RealAdapterClassMap'])),
            ('virtual_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualFeild'])),
            ('real_field_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['Virtual2RealAdapterFieldMap'])

        # Adding model 'VirtualData'
        db.create_table(u'vir2real_virtualdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('virtual_real_map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.Virtual2RealAdapterClassMap'])),
            ('source_line', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('can_be_restore_real', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('erro_msg', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualData'])

        # Adding model 'Person'
        db.create_table(u'vir2real_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('qq_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('alipay_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['Person'])


    def backwards(self, orm):
        # Deleting model 'VirtualClass'
        db.delete_table(u'vir2real_virtualclass')

        # Deleting model 'VirtualFeild'
        db.delete_table(u'vir2real_virtualfeild')

        # Deleting model 'Virtual2RealAdapterClassMap'
        db.delete_table(u'vir2real_virtual2realadapterclassmap')

        # Deleting model 'Virtual2RealAdapterFieldMap'
        db.delete_table(u'vir2real_virtual2realadapterfieldmap')

        # Deleting model 'VirtualData'
        db.delete_table(u'vir2real_virtualdata')

        # Deleting model 'Person'
        db.delete_table(u'vir2real_person')


    models = {
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
            'real_field_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'virtual_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualFeild']"})
        },
        u'vir2real.virtualclass': {
            'Meta': {'object_name': 'VirtualClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.virtualdata': {
            'Meta': {'object_name': 'VirtualData'},
            'can_be_restore_real': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'erro_msg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_line': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'virtual_real_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.Virtual2RealAdapterClassMap']"})
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